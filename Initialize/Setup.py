import Display as D
import Shapes as Sp
import File as F

class OnStart:

# creates all startup canvases 
    def create_canvas(main, width, height):
        
        button_canvas = D.Canvas(main, 30, height, "grey")
        shapes_canvas = D.Canvas(main, width, height, "white")

        button_canvas.create()
        shapes_canvas.create()
        return button_canvas, shapes_canvas

# creates all startup buttons
    def create_buttons(button_canvas, shapes_canvas, main_window):

        rectangle_button = D.Button(button_canvas, "rectangle_button","Rectangle", "white", 
        lambda event: Sp.Rectangle.make(shapes_canvas))
        rectangle_button.create()

        oval_button = D.Button(button_canvas, "oval_button", "Oval", "white",
        lambda event: Sp.Oval.make(shapes_canvas))
        oval_button.create()

        triangle_button = D.Button(button_canvas, "triangle_button", "Triangle", "white",
        lambda event: Sp.Triangle.make(shapes_canvas))
        triangle_button.create()

        polygon_button = D.Button(button_canvas, "polygon_button", "Polygon", "white",
        lambda event: Sp.Polygon.make(shapes_canvas))
        polygon_button.create()

        save_button = D.Button(button_canvas, "save_button", "Save", "white",
        lambda event: F.File.save(main_window, shapes_canvas, Sp.Shapes.shape_list))
        save_button.create()

        open_button = D.Button(button_canvas, "open_button", "Open", "white",
        lambda event: F.File.open(main_window, shapes_canvas))
        open_button.create()

    # creates main window
    def create_main_win():
        main_win = D.Window("main_win", "Shapeify", "grey")
        main_win.create()
        return main_win.get_window()