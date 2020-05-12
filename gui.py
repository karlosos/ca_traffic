import tkinter as tk
import tkinter.messagebox as msg
from math import floor, ceil
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import cv2
import numpy as np

from Simulation import Simulation
from Vec2D import Vec2D
from resizer import fit_tk, array_to_tk
from copy import deepcopy
from PIL import ImageTk, Image
import re
from Cell import Cell
from MeasurmentFlag import MeasurmentFlag
from datetime import datetime


class GUI:
    def __init__(self, master):
        # main window
        self.master = master
        self.master.minsize(900, 500)
        self.master.title("Traffic modelling")

        # Scale
        self.imageId = 0
        self.scale = 1
        # preview image
        self.part_preview = Simulation(50, 50)
        self.part_preview.initialize_map()
        self.preview_desc = tk.Label(self.master, text="Preview of part")
        self.preview_desc.place(x=25, y=25)
        self.preview_image = fit_tk(self.part_preview.colormap, 200, 200)
        self.preview_Label = tk.Label(self.master, image=self.preview_image)
        self.preview_Label.image = self.preview_image
        self.preview_Label.place(x=25, y=50, width=200, height=200)
        # choose part
        self.currentlychosen = -1
        self.preview_scrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.part_options_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE,
                                               yscrollcommand=self.preview_scrollbar.set)
        self.preview_scrollbar.config(command=self.part_options_listbox.yview)
        self.preview_scrollbar.place(x=25, y=255, height=50)
        self.part_options_listbox.place(x=40, y=255, width=180, height=50)
        self.part_options_listbox.insert(0, "generate straight-road")
        self.part_options_listbox.insert(1, "cross-section")
        self.part_options_listbox.insert(2, "cross-section-X")
        self.part_options_listbox.insert(3, "traffic-circle")
        self.part_options_listbox.insert(4, "cross-section-T-up")
        self.part_options_listbox.insert(5, "cross-section-T-down")
        self.part_options_listbox.insert(6, "cross-section-T-left")
        self.part_options_listbox.insert(7, "cross-section-T-right")
        self.part_options_listbox.insert(8, "eraser")
        self.part_options_listbox.insert(9, "Measuring-flag")
        self.load_button = tk.Button(master=self.master, text="Load model", command=self.load_part)
        self.load_button.place(x=25, y=310)
        # straight road generation
        self.straight_road_width_label = tk.Label(self.master, text="Width")
        self.straight_road_length_label = tk.Label(self.master, text="Length")
        self.straight_road_entry_width = tk.Entry(self.master)  # reused for eraser and measurment flag
        self.straight_road_entry_length = tk.Entry(self.master)
        self.straight_road_generate_button = tk.Button(self.master, text="Generate road",
                                                       command=self.generate_straight_road)
        self.straight_road_direction_label = tk.Label(self.master, text="Direction")
        self.straight_road_entry_direction = tk.Entry(self.master)
        # cars generator
        self.cars_label = tk.Label(self.master, text="Cars")
        self.cars_label.place(x=395, y=25)
        self.cars_entry = tk.Entry(self.master)
        self.cars_entry.place(x=430, y=25, width=30)
        self.cars_entry.insert(0,"20")
        # canvas
        self.canvas_relwidth = 0.6
        self.canvas_relheight = 0.7
        self.model_preview = Simulation(500, 500, 50)
        self.model_preview.initialize_map()
        self.canvas_image = array_to_tk(self.model_preview.colormap)
        self.model_preview_desc = tk.Label(self.master, text="Preview of model")
        self.model_preview_desc.place(x=275, y=25)
        self.canvas_vertical_scroll = tk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.canvas_horizontal_scroll = tk.Scrollbar(self.master, orient=tk.HORIZONTAL)
        self.canvas = tk.Canvas(master=self.master, width=self.model_preview.cellmap.shape[1],
                                height=self.model_preview.cellmap.shape[0], borderwidth=5,
                                background='gray', yscrollcommand=self.canvas_vertical_scroll,
                                xscrollcommand=self.canvas_horizontal_scroll,
                                scrollregion=(0, 0, self.model_preview.cellmap.shape[1],
                                              self.model_preview.cellmap.shape[0]))           
        self.canvas_vertical_scroll.config(command=self.canvas.yview)
        self.canvas_horizontal_scroll.config(command=self.canvas.xview)
        self.canvas_vertical_scroll.place(x=275, y=75, relheight=self.canvas_relheight)
        self.canvas_horizontal_scroll.place(x=300, y=50, relwidth=self.canvas_relwidth)
        self.canvas.place(x=300, y=75, relwidth=self.canvas_relwidth, relheight=self.canvas_relheight)
        self.imageId = self.canvas.create_image(0, 0, image=self.canvas_image, anchor=tk.NW)
        self.canvas.bind("<Button-1>", self.place_part)
        self.canvas.bind("<MouseWheel>", self.do_zoom)
        self.canvas.bind("<Motion>", self.mouse_over_canvas)
        self.canvas.bind("<Leave>", self.mouse_leaves_canvas)
        self.start_button = tk.Button(master=self.master, text="Start simulation", command=self.start_simulation)
        self.start_button.place(x=470, y=20)
        # resize map
        self.resize_map_Label = tk.Label(self.master, text="Resize map")
        self.resize_map_Label.place(x=590, y=25)
        self.resize_map_Label_X = tk.Label(self.master, text="x")
        self.resize_map_Label_X.place(x=660, y=25)
        self.resize_map_Entry_X = tk.Entry(self.master)
        self.resize_map_Entry_X.insert(0,str(len(self.model_preview.cellmap)))
        self.resize_map_Entry_X.place(x=675, y=25, width=30, height=20)
        self.resize_map_Label_Y = tk.Label(self.master, text="y")
        self.resize_map_Label_Y.place(x=715, y=25)
        self.resize_map_Entry_Y = tk.Entry(self.master)
        self.resize_map_Entry_Y.insert(0,str(len(self.model_preview.cellmap[0])))
        self.resize_map_Entry_Y.place(x=730, y=25, width=30, height=20)
        self.resize_map_Button = tk.Button(master=self.master, text="Resize Map", command=self.resize_map)
        self.resize_map_Button.place(x=770, y=20)
        # eraser and measurment flag
        self.eraser_resize_button = tk.Button(master=self.master, text="Resize tool", command=self.resize_eraser)  # reused for measurment flag
        self.measurment_flags = []
        self.flagcolor = [0, 255, 255]

    def generate_straight_road(self):
        try:
            tmp = list(x.rstrip().lstrip() for x in self.straight_road_entry_direction.get().split(','))
            assert len(tmp) < 3, msg.showerror("Error", "Too many axes")
            x = int(tmp[0])
            y = int(tmp[1])
            assert -1 <= x <= 1 and -1 <= y <= 1, msg.showerror("Error", "Wrong direction, must be integer <-1:1>")
            direction = Vec2D(x, y)
            width = int(self.straight_road_entry_width.get())
            length = int(self.straight_road_entry_length.get())
            assert 0 < width <= 3 and 0 < length < self.model_preview.cellmap.shape[0] and length < \
                self.model_preview.cellmap.shape[1], msg.showerror("Error", "Invalid length or width")
            if width > 1:
                assert width < length, msg.showerror("Error", "Invalid length or width")
            self.part_preview = Simulation(length, length)

            if direction.equal(Vec2D(1, 1)) or direction.equal(Vec2D(-1, -1)):
                for i in range((width-1), length):
                    for j in range(0, width):
                        self.part_preview.cellmap[i-j, i+j-(width-1)].kind = "road"
                        self.part_preview.cellmap[i-j, i+j-(width-1)].direction.append(direction)
            elif direction.equal(Vec2D(1, -1)) or direction.equal(Vec2D(-1, 1)):
                for i in range((width-1), length):
                    for j in range(0, width):
                        self.part_preview.cellmap[i-j, -i-j-1+(width-1)].kind = "road"
                        self.part_preview.cellmap[i-j, -i-j-1+(width-1)].direction.append(direction)
            elif direction.equal(Vec2D(0, 1)) or direction.equal(Vec2D(0, -1)):
                for i in range(int(length/2) - floor(width/2), int(length/2) + ceil(width/2)):
                    for cell in self.part_preview.cellmap[i, :]:
                        cell.kind = "road"
                        cell.direction.append(direction)
            elif direction.equal(Vec2D(1, 0)) or direction.equal(Vec2D(-1, 0)):
                for i in range(int(length / 2) - floor(width / 2), int(length / 2) + ceil(width / 2)):
                    for cell in self.part_preview.cellmap[:, i]:
                        cell.kind = "road"
                        cell.direction.append(direction)

            self.make_preview()

        except ValueError:
            msg.showerror("Error", "All entered values must be integer numbers")
            return
        except AssertionError:
            return

    def make_preview(self):  # działa
        self.part_preview.initialize_map()
        # image = cv2.cvtColor(self.part_preview.colormap, cv2.COLOR_BGR2RGB)
        f = fit_tk(self.part_preview.colormap, self.preview_Label.winfo_width(), self.preview_Label.winfo_height())
        self.preview_Label.configure(image=f)
        self.preview_Label.image = f

    def load_part(self):  # działa
        self.currentlychosen = self.part_options_listbox.curselection()[0]
        if self.currentlychosen != 0:
            if self.currentlychosen != 8 and self.currentlychosen != 9:
                self.straight_road_width_label.place_forget()
                self.straight_road_entry_width.place_forget()
                self.straight_road_entry_width.delete(0, 'end')
                self.eraser_resize_button.place_forget()
            self.straight_road_length_label.place_forget()
            self.straight_road_entry_length.place_forget()
            self.straight_road_direction_label.place_forget()
            self.straight_road_entry_direction.place_forget()
            self.straight_road_entry_length.delete(0, 'end')
            self.straight_road_entry_direction.delete(0, 'end')
        if self.currentlychosen == 0:
            self.part_preview = Simulation(1, 1)
            self.make_preview()
            self.straight_road_width_label.place(x=25, y=350)
            self.straight_road_entry_width.place(x=100, y=350, width=50, height=25)
            self.straight_road_entry_width.insert(0, "1")
            self.straight_road_length_label.place(x=25, y=400)
            self.straight_road_entry_length.place(x=100, y=400, width=50, height=25)
            self.straight_road_entry_length.insert(0, "1")
            self.straight_road_direction_label.place(x=25, y=450)
            self.straight_road_entry_direction.place(x=100, y=450, width=50, height=25)
            self.straight_road_entry_direction.insert(0, "1,1")
            self.straight_road_generate_button.place(x=175, y=400)

        elif self.currentlychosen == 1:
            array = np.load("cross-section.npy", allow_pickle=True)
            self.part_preview = Simulation(array.shape[0], array.shape[1])
            self.part_preview.cellmap = array
            self.make_preview()
        elif self.currentlychosen == 2:
            array = np.load("cross-section-X.npy", allow_pickle=True)
            self.part_preview = Simulation(array.shape[0], array.shape[1])
            self.part_preview.cellmap = array
            self.make_preview()
        elif self.currentlychosen == 3:
            array = np.load("traffic-circle.npy", allow_pickle=True)
            self.part_preview = Simulation(array.shape[0], array.shape[1])
            self.part_preview.cellmap = array
            self.make_preview()
        elif self.currentlychosen == 4:
            array = np.load("cross-section-T-up.npy", allow_pickle=True)
            self.part_preview = Simulation(array.shape[0], array.shape[1])
            self.part_preview.cellmap = array
            self.make_preview()
        elif self.currentlychosen == 5:
            array = np.load("cross-section-T-down.npy", allow_pickle=True)
            self.part_preview = Simulation(array.shape[0], array.shape[1])
            self.part_preview.cellmap = array
            self.make_preview()
        elif self.currentlychosen == 6:
            array = np.load("cross-section-T-left.npy", allow_pickle=True)
            self.part_preview = Simulation(array.shape[0], array.shape[1])
            self.part_preview.cellmap = array
            self.make_preview()
        elif self.currentlychosen == 7:
            array = np.load("cross-section-T-right.npy", allow_pickle=True)
            self.part_preview = Simulation(array.shape[0], array.shape[1])
            self.part_preview.cellmap = array
            self.make_preview()
        elif self.currentlychosen == 8:
            self.straight_road_width_label.place(x=25, y=350)
            self.straight_road_entry_width.place(x=100, y=350, width=50, height=25)
            self.straight_road_entry_width.insert(0, "50")
            self.part_preview = Simulation(int(self.straight_road_entry_width.get()),
                                           int(self.straight_road_entry_width.get()))
            self.make_preview()
            self.eraser_resize_button.place(x=160, y=350, width=75, height=25)
        elif self.currentlychosen == 9:
            self.straight_road_width_label.place(x=25, y=350)
            self.straight_road_entry_width.place(x=100, y=350, width=50, height=25)
            self.straight_road_entry_width.insert(0, "50")
            self.part_preview = Simulation(int(self.straight_road_entry_width.get()),
                                           int(self.straight_road_entry_width.get()))
            self.part_preview.colormap[:, :] = self.flagcolor
            self.make_preview()
            self.eraser_resize_button.place(x=160, y=350, width=75, height=25)

    def place_part(self, event):
        canvas = event.widget
        row = int(canvas.canvasy(event.y)/self.scale)
        col = int(canvas.canvasx(event.x)/self.scale)
        if self.currentlychosen == 8:
            for y in range(0 if 0 > col-int(self.part_preview.cellmap.shape[0]/2) else col-int(self.part_preview.cellmap.shape[0]/2),
                           self.model_preview.cellmap.shape[0] if self.model_preview.cellmap.shape[0] <
                                                                  col+int(self.part_preview.cellmap.shape[0]/2)
                                                               else col+int(self.part_preview.cellmap.shape[0]/2)):
                for x in range(0 if 0 > row-int(self.part_preview.cellmap.shape[1]/2) else row-int(self.part_preview.cellmap.shape[1]/2),
                               self.model_preview.cellmap.shape[1] if self.model_preview.cellmap.shape[1] <
                               row+int(self.part_preview.cellmap.shape[1]/2) else row+int(self.part_preview.cellmap.shape[1]/2)):
                    self.model_preview.cellmap[x, y] = Cell()
                    self.model_preview.colormap[x, y] = self.model_preview.nonecolor
        elif self.currentlychosen == 9:
            if row + int(self.part_preview.cellmap.shape[1]/2) > self.model_preview.cellmap.shape[1] or \
                        row - int(self.part_preview.cellmap.shape[1]/2) < 0:
                msg.showerror("Flag won't fit vertically")
                return
            if col + int(self.part_preview.cellmap.shape[0]/2) > self.model_preview.cellmap.shape[0] or \
                col - int(self.part_preview.cellmap.shape[0]/2) < 0:
                msg.showerror("Flag won't fit horizontally")
                return

            self.measurment_flags.append(MeasurmentFlag(Vec2D(row, col), int(self.straight_road_entry_width.get())))

            for x in range(row-int(self.part_preview.cellmap.shape[1]/2), row+int(self.part_preview.cellmap.shape[1]/2)):
                for y in range(col-int(self.part_preview.cellmap.shape[0]/2), col+int(self.part_preview.cellmap.shape[0]/2)):
                    if np.array_equal(self.model_preview.colormap[x, y], self.model_preview.nonecolor):
                        self.model_preview.colormap[x, y] = self.flagcolor
            return
        else:
            if row + int(self.part_preview.cellmap.shape[1]/2) > self.model_preview.cellmap.shape[1] or \
                        row - int(self.part_preview.cellmap.shape[1]/2) < 0:
                msg.showerror("Part won't fit vertically")
                return
            if col + int(self.part_preview.cellmap.shape[0]/2) > self.model_preview.cellmap.shape[0] or \
                col - int(self.part_preview.cellmap.shape[0]/2) < 0:
                msg.showerror("Part won't fit horizontally")
                return
            part_preview = deepcopy(self.part_preview)

            for x in range(row-int(self.part_preview.cellmap.shape[1]/2), row+int(part_preview.cellmap.shape[1]/2)):
                for y in range(col-int(self.part_preview.cellmap.shape[0]/2), col+int(part_preview.cellmap.shape[0]/2)):
                    modelcell = self.model_preview.cellmap[x, y]
                    partcell = part_preview.cellmap[x-row+int(part_preview.cellmap.shape[0]/2), y-col+int(part_preview.cellmap.shape[1]/2)]
                    if modelcell.kind is None and partcell.kind is not None:
                        self.model_preview.cellmap[x, y] = partcell
                        self.model_preview.colormap[x, y] = self.model_preview.roadcolor
                    elif modelcell.kind == "road" and partcell.kind == "road":
                        for dire in partcell.direction:
                            if not any(dire.equal(direc) for direc in modelcell.direction):
                                self.model_preview.cellmap[x, y].direction.append(Vec2D(dire.x, dire.y))

        self.model_preview.initialize_map()
        # image = cv2.cvtColor(self.model_preview.colormap, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(self.model_preview.colormap)
        w = int(im.width * self.scale)
        h = int(im.height * self.scale)
        img = im.resize((w, h), Image.ANTIALIAS)
        self.canvas_image = ImageTk.PhotoImage(img)
        self.canvas.itemconfigure(self.imageId, image=self.canvas_image)

    def do_zoom(self, event):
        true_x = self.canvas.canvasx(event.x)
        true_y = self.canvas.canvasy(event.y)
        tmpScale = 1.0
        if event.delta > 0:
            self.scale *= 1.3
            tmpScale *= 1.3
        elif event.delta < 0:
            self.scale /= 1.3
            tmpScale /= 1.3
        # image = cv2.cvtColor(self.model_preview.colormap, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(self.model_preview.colormap)
        w = int(im.width * self.scale)
        h = int(im.height * self.scale)
        img = im.resize((w, h), Image.NEAREST)
        self.canvas_image = ImageTk.PhotoImage(img)
        self.canvas.itemconfigure(self.imageId, image=self.canvas_image)
        self.canvas.scale('all', 0, 0, tmpScale, tmpScale)
        self.canvas.configure(scrollregion=(0, 0, w, h))

    def mouse_over_canvas(self, event):
        canvas = event.widget
        [part_size_x, part_size_y, _] = self.part_preview.colormap.shape
        # row = int(canvas.canvasy(event.y) - part_size_x/2)
        # col = int(canvas.canvasx(event.x) - part_size_y/2)
        row = int(canvas.canvasy(event.y)/self.scale - part_size_x/2)
        col = int(canvas.canvasx(event.x)/self.scale - part_size_y/2)
        model_image = self.model_preview.colormap.copy()
        part_preview_image = self.part_preview.colormap.copy()

        try:
            model_image_crop = model_image[row:row+part_size_x, col:col+part_size_y]
            roads_index = np.logical_not(part_preview_image == self.model_preview.nonecolor)
            model_image_crop[roads_index] = part_preview_image[roads_index]
        except:
            pass

        self.canvas_image = array_to_tk(model_image)

        im = Image.fromarray(model_image)
        w = int(im.width * self.scale)
        h = int(im.height * self.scale)
        img = im.resize((w, h), Image.ANTIALIAS)
        self.canvas_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, image=self.canvas_image, anchor=tk.NW)

    def mouse_leaves_canvas(self, event):
        return

    def start_simulation(self):  # działa
        check_string = self.cars_entry.get()
        if re.match("^[0-9]+$", check_string):
            cars_number = int(check_string)
            if isinstance(cars_number, int) and cars_number > 0:
                cv2.namedWindow("Map", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("Map", 1280, 800)
                self.model_preview.cellmap_outline_roads()
                self.model_preview.initialize_map()
                self.model_preview.find_starting_point()
                datavecs = []
                file_handles = []
                axes = []
                # fig = plt.figure()
                n_vecs = len(self.measurment_flags)
                if n_vecs > 0:
                    # plt.show()
                    now = datetime.now()
                    dt_string = now.strftime("%d-%m-%Y %H;%M;%S")
                    try:
                        # Create target Directory
                        os.mkdir("Measurements\\"+dt_string)
                    except FileExistsError:
                        pass
                    for i in range(n_vecs):
                        # axes.append(fig.add_subplot(n_vecs, 1, i+1))
                        vec = list([0 for _ in range(100)])
                        datavecs.append(vec)
                        file_handles.append(open("Measurements\\" + dt_string + "\\" + str(i) + ".csv", "a"))  # append only write mode
                while True:
                    if len(self.model_preview.cars) < cars_number:
                        self.model_preview.add_car()
                    self.model_preview.step()
                    self.model_preview.print_map("Map")
                    if n_vecs > 0:
                        for i in range(n_vecs):
                            n_slow = 0
                            flag = self.measurment_flags[i]
                            for row in self.model_preview.colormap[flag.pos.x - int(flag.size/2): flag.pos.x + int(flag.size/2), flag.pos.y - int(flag.size/2): flag.pos.y + int(flag.size/2)]:
                                for color in row:
                                    if np.array_equal(color, self.part_preview.slowcolor):
                                        n_slow += 1
                            file_handles[i].write(str(n_slow)+", ")
                            datavecs[i].pop(0)
                            datavecs[i].append(n_slow)
                            # axes[i].clear()
                            # axes[i].plot(datavecs[i])
                        # plt.pause(0.05)

                    k = cv2.waitKey(50)
                    if k == 27:
                        cv2.destroyAllWindows()
                        break

                for i in range(n_vecs):
                    file_handles[i].close()
       
    def resize_map(self):
        x = int(self.resize_map_Entry_X.get())
        y = int(self.resize_map_Entry_Y.get())
        if (x != len(self.model_preview.cellmap)) or (y != len(self.model_preview.cellmap[0])):
            self.canvas.configure(width=x, height=y, scrollregion=(0, 0, y, x))
            if x < len(self.model_preview.cellmap):
                self.model_preview.cellmap = self.model_preview.cellmap[0:x, :]
                self.model_preview.colormap = self.model_preview.colormap[0:x, :, :]
            elif x > len(self.model_preview.cellmap):
                toAdd = x - len(self.model_preview.cellmap)
                row_to_be_added = np.array([list(Cell() for _ in range(len(self.model_preview.cellmap))) for _ in range(toAdd)])
                result = np.vstack((self.model_preview.cellmap, row_to_be_added))
                self.model_preview.cellmap = result
                # colormap
                toAdd = x - len(self.model_preview.colormap)
                b = np.full([len(self.model_preview.colormap)+toAdd, len(self.model_preview.colormap[0]), 3], 255, dtype=np.uint8)
                b[:-toAdd:, :, ] = self.model_preview.colormap
                self.model_preview.colormap = b 
            if y < len(self.model_preview.cellmap[0]):
                self.model_preview.cellmap = self.model_preview.cellmap[:, 0:y]
                self.model_preview.colormap = self.model_preview.colormap[:, 0:y, :]
            elif y > len(self.model_preview.cellmap[0]):
                toAdd = y - len(self.model_preview.cellmap[0])
                column_to_be_added = np.array([list(Cell() for _ in range(toAdd)) for _ in range(len(self.model_preview.cellmap))])
                result = np.column_stack((self.model_preview.cellmap, column_to_be_added)) 
                self.model_preview.cellmap = result
                # colormap
                toAdd = y - len(self.model_preview.colormap[0])
                b = np.full([len(self.model_preview.colormap), len(self.model_preview.colormap[0])+toAdd, 3], 255, dtype=np.uint8)
                b[:, :-toAdd:, ] = self.model_preview.colormap
                self.model_preview.colormap = b 
        else:
            return                    

    def resize_eraser(self):
        try:
            width = int(self.straight_road_entry_width.get())
            assert self.model_preview.cellmap.shape[0] > width > 0 and width < self.model_preview.cellmap.shape[1], \
                msg.showerror("Error", "Incorrect width")
            self.part_preview = Simulation(width, width)
            if self.currentlychosen == 9:
                self.part_preview.colormap[:, :] = self.flagcolor

        except ValueError:
            msg.showerror("Error", "Width must be an integer")
            return

        except AssertionError:
            return


