import tkinter as tk

class Button:
    def __init__(self, canvas, name, text, color, function):
        self.canvas = canvas.get_canvas()
        self.name = name
        self.text = text
        self.color = color
        self.function = function
    
    def create(self, selector_win=False):
        self.name = tk.Button(self.canvas, text=self.text, bg=self.color)
        self.name.pack()
        if not selector_win:
            self.name.bind("<Button-1>", self.function)
        else:
            self.name.bind("<ButtonRelease-1>", self.function)