from tkinter import colorchooser
from Display import Menu
from .Selector import Selector

class Shapes:

    shape_id = int

    width = 800
    height = 600
    shape_name = ''
    selected = False

    tag_num = 0
    old_id = None
    shape_list = []

    def __init__(self, canvas, width=None, height=None, load=False, coord_points=None, color=None, outline=''):
        if not load:
            self.width = width
            self.height = height
            self.x = width//2
            self.y = height//2
            self.color = "red"
        else:
            self.coords = coord_points
            self.color = color

        self.canvas = canvas.get_canvas()
        self.outline = outline
    
    def tag_bind(self):
        self.canvas.tag_bind(f'{self.tag}', "<Button-1>", self.on_click)
        self.canvas.tag_bind(f'{self.tag}', "<B1-Motion>", self.on_motion)
        self.shapes_menu()
    
    def shapes_menu(self):
        shapes_menu_name_list = ["Delete", 'Deselect', 'Bring Forward', 'Send Backward', 'Change Color', 'Add Outline', 'Remove Outline']
        shapes_menue_function_list = [  lambda: Shapes.delete_shape(self.canvas),
                                        lambda: Selector.delete(self.canvas),
                                        lambda: Shapes.bring_forward(self.canvas),
                                        lambda: Shapes.send_backward(self.canvas),
                                        lambda: Shapes.change_color(self.canvas),
                                        lambda: self.add_outline(),
                                        lambda: self.remove_outline()
                                        ]
        shape_menu = Menu(self.canvas, shapes_menu_name_list, shapes_menue_function_list, "Button-3", is_canvas=False, shape_tag=self.tag)
        shape_menu.create_canvas_menu()
    
    def add_outline(self):
        self.canvas.itemconfig(self.tag, outline='black')
        self.outline = 'black'

    def remove_outline(self):
        self.canvas.itemconfig(self.tag, outline='')
        self.outline = ''
    
    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.id = self.canvas.find_closest(event.x, event.y)
        Shapes.shape_id = self.id
        self.selected()
        Selector.assign_id(Shapes.shape_id)
        
    def selected(self):
        if Shapes.old_id != self.id or Selector.selected == False:
            Shapes.shape_name = self.get_id()

            Selector.delete(self.canvas)

            x_position = []
            y_position = []
            self.coords = self.canvas.coords(self.id)

            for x in range(0, len(self.coords), 2):
                x_position.append(self.coords[x])
            for y in range(1, len(self.coords), 2):
                y_position.append(self.coords[y])

            for num in range(0, len(x_position)):
                selector = Selector(self.canvas, x_position[num], y_position[num])
                coord_connect = [x_position[num], y_position[num]]
                selector.create(coord_connect)

            Shapes.old_id = self.id
    
    def on_motion(self, event):
        x = event.x - self.start_x
        y = event.y - self.start_y

        self.canvas.move(self.id, x,y)
        Selector.move(x,y, self.canvas)

        self.start_x = event.x
        self.start_y = event.y

    def get_id(self):
        return self.tag
    
    def get_amount_of_positions(self):
        i = 0
        for _ in range(0, len(self.coords), 2):
            i+=1
        return i

    def delete_shape(canvas):
        if Selector.selected and Shapes.shape_name != '': 
            canvas.delete(Shapes.shape_id)
            Selector.delete(canvas)
            Shapes.shape_list.remove(Shapes.shape_name)

    def bring_forward(canvas):
        if not Selector.selected and Shapes.shape_name != '': pass
        else:
            index1 = Shapes.shape_list.index(Shapes.shape_name)
            if index1 != len(Shapes.shape_list)-1:
                above_name = Shapes.shape_list[index1+1]
                index2 = Shapes.shape_list.index(above_name)

                # can = canvas.get_canvas()
                canvas.tag_raise(Shapes.shape_id, above_name)

                Shapes.shape_list[index1], Shapes.shape_list[index2] = \
                    Shapes.shape_list[index2], Shapes.shape_list[index1]

    def send_backward(canvas):
        if not Selector.selected and Shapes.shape_name != '': pass
        else:
            index1 = Shapes.shape_list.index(Shapes.shape_name)
            if index1 != 0:
                below_name = Shapes.shape_list[index1-1]
                index2 = Shapes.shape_list.index(below_name)
    
                # can = canvas.get_canvas()
                canvas.tag_lower(Shapes.shape_id, below_name)
    
                Shapes.shape_list[index1], Shapes.shape_list[index2] = \
                    Shapes.shape_list[index2], Shapes.shape_list[index1]
    
    def make_tag(word):
        tag = f'{word}{Shapes.tag_num}'
        Shapes.tag_num+=1
        Shapes.shape_list.append(tag)
        return tag

    def change_color(canvas):
        if Selector.selected and Shapes.shape_name != '':
            chooser = colorchooser.askcolor()[1]
            canvas.itemconfig(Shapes.shape_name, fill=chooser)

    # extracted from "on_move". Reason: Can't "select" without a mouse input.
    def test_move_shape(self, x, y):
        self.canvas.move(self.tag, x,y)
    
    # coppied from 'change_color', removed 'colorchooser.askcolor()[1]'
    def test_change_color(self, color):
        self.canvas.itemconfig(self.tag, fill=color)
    
    def debug_get_fill(self):
        return self.canvas.itemcget(self.tag , "fill")
    
    def debug_get_coords(self):
        return self.canvas.coords(self.tag)
    
    # coppied from 'delete_shape', removed 'Selector.delete'
    def test_delete_shape(self):
        self.canvas.delete(self.tag)
        Shapes.shape_list.remove(self.tag)