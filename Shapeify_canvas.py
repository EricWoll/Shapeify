import tkinter as tk

# creates windows
class Windows:

    window_count = 0

    def __init__(self, name, title, color) -> None:
        self.name = name
        self.title = title
        self.color = color

    def create(self) -> None:
        self.name = tk.Tk()
        
        self.name.title(self.title)
        self.name.configure(bg=self.color)

        Windows.window_count += 1
    
    def make(name, title):
        name = Windows(name, title)
        name.create()

    def get_window(self):
        return self.name

# creates canvases
class Canvases:

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

# creates buttons
class My_Buttons:
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