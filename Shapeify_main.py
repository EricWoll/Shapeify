import Shapeify_canvas as C
import Shapeify_shapes as Sp
import Shapeify_save as Sv


class OnStart:

# creates all startup canvases 
    def create_canvas(main, width, height):
        
        button_canvas = C.Canvases(main, 30, height, "grey")
        shapes_canvas = C.Canvases(main, width, height, "white")

        button_canvas.create()
        shapes_canvas.create()
        return button_canvas, shapes_canvas

# creates all startup buttons
    def create_buttons(button_canvas, shapes_canvas, main_window):

        rectangle_button = C.My_Buttons(button_canvas, "rectangle_button","Rectangle", "white", 
        lambda event: Sp.Rectangle.make(shapes_canvas))
        rectangle_button.create()

        oval_button = C.My_Buttons(button_canvas, "oval_button", "Oval", "white",
        lambda event: Sp.Oval.make(shapes_canvas))
        oval_button.create()

        triangle_button = C.My_Buttons(button_canvas, "triangle_button", "Triangle", "white",
        lambda event: Sp.Triangle.make(shapes_canvas))
        triangle_button.create()

        polygon_button = C.My_Buttons(button_canvas, "polygon_button", "Polygon", "white",
        lambda event: Sp.Polygon.make(shapes_canvas))
        polygon_button.create()

        save_button = C.My_Buttons(button_canvas, "save_button", "Save", "white",
        lambda event: Sv.File.save(main_window, shapes_canvas, Sp.Shapes.shape_list))
        save_button.create()

        open_button = C.My_Buttons(button_canvas, "open_button", "Open", "white",
        lambda event: Sv.File.open(main_window, shapes_canvas))
        open_button.create()

    # creates main window
    def create_main_win():
        main_win = C.Windows("main_win", "Shapeify", "grey")
        main_win.create()
        return main_win.get_window()


# is main loop
class Shapeify:
    def main():
        width = 800
        height = 600

        main_win = OnStart.create_main_win()

        button_canvas, shapes_canvas = OnStart.create_canvas(main_win, width, height)
        OnStart.create_buttons(button_canvas, shapes_canvas, main_win)

        C.tk.mainloop()

if __name__ == "__main__":
    Shapeify.main()
    print("END OF PROGRAM")