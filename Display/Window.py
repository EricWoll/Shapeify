import tkinter as tk

class Window:

    window_count = 0

    def __init__(self, name, title, color) -> None:
        self.name = name
        self.title = title
        self.color = color

    def create(self) -> None:
        self.name = tk.Tk()
        
        self.name.title(self.title)
        self.name.configure(bg=self.color)

        Window.window_count += 1
    
    def make(name, title):
        name = Window(name, title)
        name.create()

    def get_window(self):
        return self.name