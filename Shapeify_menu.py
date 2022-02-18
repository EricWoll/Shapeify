import tkinter as tk

class MyMenu:

    def __init__(self, main, name_list, function_list, key_bind, is_canvas=True, shape_tag=None, tear_off=0):
        if is_canvas:
            self.main = main
        else:
            self.main = main
            self.shape_tag = shape_tag

        self.is_canvas = is_canvas
        self.name_list = name_list
        self.function_list = function_list
        self.key_bind = key_bind
        self.tear_off = tear_off

    def create_canvas_menu(self):
        self.menu = tk.Menu(master=self.main, tearoff=self.tear_off)
        for item in range(len(self.name_list)):
            self.menu.add_command(label=self.name_list[item], command=self.function_list[item])

        def do_popup(main):
            try:
                abs_coord_x = main.winfo_pointerx()
                abs_coord_y = main.winfo_pointery()
                self.menu.tk_popup(abs_coord_x, abs_coord_y)
            finally:
                self.menu.grab_release()

        # binds to popup
        if self.is_canvas:
            self.main.bind(f"<{self.key_bind}>", lambda event: do_popup(self.main))
        else:
            self.main.tag_bind(f'{self.shape_tag}', f'<{self.key_bind}>', lambda event: do_popup(self.main))   