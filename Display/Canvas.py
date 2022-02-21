import tkinter as tk

class Canvas:

    def __init__(self, main, width, height, color, expand=False):
        self.main = main
        self.width = width
        self.height = height
        self.color = color
        self.expand = expand

    def create(self):
        self.canvases = tk.Canvas(self.main, width=self.width, height=self.height, highlightthickness=0, bg=self.color)
        self.canvases.pack(side="left", expand=self.expand)
        return self.canvases
    
    def get_canvas(self):
        return self.canvases