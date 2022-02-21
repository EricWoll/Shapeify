import tkinter as tk
import Initialize as Init

def main():
        width = 800
        height = 600

        main_win = Init.OnStart.create_main_win()

        button_canvas, shapes_canvas = Init.OnStart.create_canvas(main_win, width, height)
        Init.OnStart.create_buttons(button_canvas, shapes_canvas, main_win)

        tk.mainloop()

if __name__ == "__main__":
    main()