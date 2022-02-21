from tkinter import filedialog
from re import sub

from Shapes import Oval, Polygon, Rectangle, Triangle

class File:

    pattern = r'[0-9]'

    def save(main_window, canvas, shape_list):
        main_window.filename = filedialog.asksaveasfile(filetypes=[('Text Document', '*.txt')], defaultextension=[('Text Document', '*.txt')])
        try:
            can = canvas.get_canvas()
            with open(main_window.filename.name, "a+") as my_file:
                for item in shape_list:
                    item_coords = can.coords(item)
                    color = can.itemcget(item, "fill")
                    item_name = sub(File.pattern, '', item)
                    outline = can.itemcget(item , "outline")
                    print(f'{item_name}|{color}|{item_coords}|{outline}',file=main_window.filename)
        except (AttributeError):
            print('No File Created')
    
    def open(main_window, shape_canvas):
        main_window.filename = filedialog.askopenfilename(title="Select a File", 
        filetypes=[('Text Document', '*.txt')])
        try:

            with open(main_window.filename, "r") as my_file:

                # Clears shapes canvas
                can = shape_canvas.get_canvas()
                can.delete('all')

                for line in my_file:
                    split_line = line.split('|')
                    shape = split_line[0]
                    color = split_line[1]
                    coords = split_line[2].split(',')
                    outline = split_line[3].strip()

                    # draws rectangles from file
                    if shape == "rectangle":
                        r2 = Rectangle(shape_canvas, load=True, coord_points=coords, color=color, outline=outline)
                        r2.load()

                    # draws oval from file
                    if shape == "oval":
                        o2 = Oval(shape_canvas, load=True, coord_points=coords, color=color, outline=outline)
                        o2.load()

                    # draws triangle from file
                    if shape == "triangle":
                        t2 = Triangle(shape_canvas, load=True, coord_points=coords, color=color, outline=outline)
                        t2.load()

                    # draws polygon from file
                    if shape == "polygon":
                        p2 = Polygon(shape_canvas, load=True, coord_points=coords, color=color, outline=outline)
                        p2.load()
                        
        except FileNotFoundError:
            print('No File Selected')