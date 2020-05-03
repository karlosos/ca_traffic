import tkinter as tk
import tkinter.messagebox as msg
from math import floor, ceil
from tkinter import ALL

import cv2
import numpy as np

from Simulation import Simulation
from Vec2D import Vec2D
from resizer import fit_tk, array_to_tk


class GUI:
    def __init__(self, master):
        # main window
        self.master = master
        self.master.minsize(900, 500)
        self.master.title("Traffic modelling")
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
        self.currentlychosen = 0
        self.preview_scrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.part_options_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE,
                                               yscrollcommand=self.preview_scrollbar.set)
        self.preview_scrollbar.config(command=self.part_options_listbox.yview)
        self.preview_scrollbar.place(x=25, y=255, height=50)
        self.part_options_listbox.place(x=40, y=255, width=180, height=50)
        self.part_options_listbox.insert(0, "generate straight-road")
        self.part_options_listbox.insert(1, "cross-section")
        self.part_options_listbox.insert(2, "cross-section-x")
        self.load_button = tk.Button(master=self.master, text="Load model", command=self.load_part)
        self.load_button.place(x=25, y=310)
        # straight road generation
        self.straight_road_width_label = tk.Label(self.master, text="Width")
        self.straight_road_length_label = tk.Label(self.master, text="Length")
        self.straight_road_entry_width = tk.Entry(self.master)
        self.straight_road_entry_length = tk.Entry(self.master)
        self.straight_road_generate_button = tk.Button(self.master, text="Generate road",
                                                       command=self.generate_straight_road)
        self.straight_road_direction_label = tk.Label(self.master, text="Direction")
        self.straight_road_entry_direction = tk.Entry(self.master)
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
        self.canvas.create_image(0, 0, image=self.canvas_image, anchor=tk.NW)
        self.canvas.bind("<Button-1>", self.place_part)
        self.canvas.bind("<MouseWheel>", self.do_zoom)
        self.start_button = tk.Button(master=self.master, text="Start simulation", command=self.start_simulation)
        self.start_button.place(x=425, y=20)

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
        image = cv2.cvtColor(self.part_preview.colormap, cv2.COLOR_BGR2RGB)
        f = fit_tk(image, self.preview_Label.winfo_width(), self.preview_Label.winfo_height())
        self.preview_Label.configure(image=f)
        self.preview_Label.image = f

    def load_part(self):  # działa
        self.currentlychosen = self.part_options_listbox.curselection()[0]
        if self.currentlychosen != 0:
            self.straight_road_width_label.place_forget()
            self.straight_road_entry_width.place_forget()
            self.straight_road_length_label.place_forget()
            self.straight_road_entry_length.place_forget()
            self.straight_road_direction_label.place_forget()
            self.straight_road_entry_direction.place_forget()
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
            array = np.load("cross-section-x.npy", allow_pickle=True)
            self.part_preview = Simulation(array.shape[0], array.shape[1])
            self.part_preview.cellmap = array
            self.make_preview()

    def place_part(self, event):  # bug
        canvas = event.widget
        row = int(canvas.canvasy(event.y))
        col = int(canvas.canvasx(event.x))
        if row + self.part_preview.cellmap.shape[1] > self.model_preview.cellmap.shape[1]:
            msg.showerror("Error", "Part won't fit vertically")
            return
        if col + self.part_preview.cellmap.shape[0] > self.model_preview.cellmap.shape[0]:
            msg.showerror("Error", "Part won't fit horizontally")
            return

        # self.model_preview.cellmap[row:row+self.part_preview.cellmap.shape[1],
        #                            col:col+self.part_preview.cellmap.shape[0]] = self.part_preview.cellmap
        for x in range(row, row+self.part_preview.cellmap.shape[1]):
            for y in range(col, col+self.part_preview.cellmap.shape[0]):
                modelcell = self.model_preview.cellmap[x, y]
                partcell = self.part_preview.cellmap[x-row, y-col]
                if modelcell.kind is None and partcell.kind is not None:
                    self.model_preview.cellmap[x, y] = partcell
                elif modelcell.kind == "road" and partcell.kind == "road":  # bugs sometimes
                    # self.model_preview.cellmap[x, y].direction.append(self.part_preview.cellmap[x-row, y-col].direction[0])
                    for dire in partcell.direction:
                        if not any(dire.equal(direc) for direc in modelcell.direction):
                            self.model_preview.cellmap[x, y].direction.append(dire)

        selected = []
        for x in range(row, row+self.part_preview.cellmap.shape[1]):
            for y in range(col, col+self.part_preview.cellmap.shape[0]):
                if self.model_preview.cellmap[x, y].kind == "road":
                    for dire in self.model_preview.cellmap[x, y].direction:
                        nextcell = self.model_preview.cellmap[x+dire.x, y+dire.y]
                        if nextcell.kind != "road":
                            selected.append((x, y, dire))
        for x, y, dire in selected:
            self.model_preview.cellmap[x, y].direction.remove(dire)

        self.model_preview.initialize_map()
        self.canvas_image = array_to_tk(self.model_preview.colormap)
        self.canvas.create_image(0, 0, image=self.canvas_image, anchor=tk.NW)

    def do_zoom(self, event):  # nie działa
        factor = 1.001 ** event.delta
        self.canvas.scale(ALL, event.x, event.y, factor, factor)

    def start_simulation(self):  # działa
        cv2.namedWindow("Map", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Map", 1280, 800)
        self.model_preview.cellmap_outline_roads()
        self.model_preview.initialize_map()
        self.model_preview.find_starting_point()
        while True:
            if len(self.model_preview.cars) < 20:
                self.model_preview.add_car()
            self.model_preview.step()
            self.model_preview.print_map("Map")
            k = cv2.waitKey(50)
            if k == 27:
                cv2.destroyAllWindows()
                break









