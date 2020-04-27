import tkinter as tk
import tkinter.messagebox as msg
import numpy as np
from resizer import fit_tk, array_to_tk
import cv2
from Simulation import Simulation


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
        self.preview_scrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.part_options_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE,
                                               yscrollcommand=self.preview_scrollbar.set)
        self.preview_scrollbar.config(command=self.part_options_listbox.yview)
        self.preview_scrollbar.place(x=25, y=255, height=50)
        self.part_options_listbox.place(x=40, y=255, width=180, height=50)
        self.part_options_listbox.insert(0, "cross-section")
        self.load_button = tk.Button(master=self.master, text="Load model", command=self.load_part)
        self.load_button.place(x=25, y=310)
        # canvas
        self.canvas_relwidth = 0.6
        self.canvas_relheight = 0.7
        self.model_preview = Simulation(500, 500)
        self.model_preview.initialize_map()
        self.canvas_image = array_to_tk(self.model_preview.colormap)
        self.model_preview_desc = tk.Label(self.master, text="Preview of model")
        self.model_preview_desc.place(x=250, y=25)
        self.canvas_vertical_scroll = tk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.canvas_horizontal_scroll = tk.Scrollbar(self.master, orient=tk.HORIZONTAL)
        self.canvas = tk.Canvas(master=self.master, width=self.model_preview.cellmap.shape[1],
                                height=self.model_preview.cellmap.shape[0], borderwidth=5,
                                background='white', yscrollcommand=self.canvas_vertical_scroll,
                                xscrollcommand=self.canvas_horizontal_scroll)
        self.canvas_vertical_scroll.config(command=self.canvas.yview)
        self.canvas_horizontal_scroll.config(command=self.canvas.xview)
        self.canvas_vertical_scroll.place(x=250, y=75, relheight=self.canvas_relheight)
        self.canvas_horizontal_scroll.place(x=275, y=50, relwidth=self.canvas_relwidth)
        self.canvas.place(x=275, y=75, relwidth=self.canvas_relwidth, relheight=self.canvas_relheight)
        self.canvas.create_image(0, 0, image=self.canvas_image, anchor=tk.NW)
        self.canvas.bind("<Button-1>", self.place_part)

    def make_preview(self):
        self.part_preview.initialize_map()
        image = cv2.cvtColor(self.part_preview.colormap, cv2.COLOR_BGR2RGB)
        f = fit_tk(image, self.preview_Label.winfo_width(), self.preview_Label.winfo_height())
        self.preview_Label.configure(image=f)
        self.preview_Label.image = f

    def load_part(self):
        i = self.part_options_listbox.curselection()[0]
        if i == 0:
            array = np.load("cross-section.npy", allow_pickle=True)
            self.part_preview = Simulation(array.shape[0], array.shape[1])
            self.part_preview.cellmap = array
            self.make_preview()

    def place_part(self, event):
        canvas = event.widget
        row = int(canvas.canvasy(event.y))
        col = int(canvas.canvasx(event.x))
        if row + self.part_preview.cellmap.shape[1] > self.model_preview.cellmap.shape[1]:
            msg.showerror("Part won't fit vertically")
            return
        if col + self.part_preview.cellmap.shape[0] > self.model_preview.cellmap.shape[0]:
            msg.showerror("Part won't fit horizontally")
            return

        self.model_preview.cellmap[row:row+self.part_preview.cellmap.shape[1],
                                   col:col+self.part_preview.cellmap.shape[0]] = self.part_preview.cellmap

        self.model_preview.initialize_map()
        self.canvas_image = array_to_tk(self.model_preview.colormap)
        self.canvas.create_image(0, 0, image=self.canvas_image, anchor=tk.NW)











