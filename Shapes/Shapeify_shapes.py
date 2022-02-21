from tkinter import colorchooser
from Display import Menu

width = 800
height = 600
selected = False

class Shapes:

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
        global shape_id
        self.start_x = event.x
        self.start_y = event.y
        self.id = self.canvas.find_closest(event.x, event.y)
        shape_id = self.id
        self.selected()
        
    def selected(self):
        global shape_name
        if Shapes.old_id != self.id or selected == False:
            shape_name = self.get_id()

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
        if selected: 
            canvas.delete(shape_id)
            Selector.delete(canvas)
            Shapes.shape_list.remove(shape_name)

    def bring_forward(canvas):
        if not selected: pass
        else:
            index1 = Shapes.shape_list.index(shape_name)
            if index1 != len(Shapes.shape_list)-1:
                above_name = Shapes.shape_list[index1+1]
                index2 = Shapes.shape_list.index(above_name)

                # can = canvas.get_canvas()
                canvas.tag_raise(shape_id, above_name)

                Shapes.shape_list[index1], Shapes.shape_list[index2] = \
                    Shapes.shape_list[index2], Shapes.shape_list[index1]

    def send_backward(canvas):
        if not selected: pass
        else:
            index1 = Shapes.shape_list.index(shape_name)
            if index1 != 0:
                below_name = Shapes.shape_list[index1-1]
                index2 = Shapes.shape_list.index(below_name)
    
                # can = canvas.get_canvas()
                canvas.tag_lower(shape_id, below_name)
    
                Shapes.shape_list[index1], Shapes.shape_list[index2] = \
                    Shapes.shape_list[index2], Shapes.shape_list[index1]
    
    def make_tag(word):
        tag = f'{word}{Shapes.tag_num}'
        Shapes.tag_num+=1
        Shapes.shape_list.append(tag)
        return tag

    def change_color(canvas):
        if selected:
            chooser = colorchooser.askcolor()[1]
            canvas.itemconfig(shape_name, fill=chooser)

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


class Selector():

    selector_num = 0
    selector_list = []

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.tag = f'selector{Selector.selector_num}'
        self.num = Selector.selector_num
        Selector.selector_num +=2

    def create(self, coord_connect):
        global selected
        selected = True
        self.coord_connect = coord_connect
        self.selector = self.canvas.create_oval(self.x+5, self.y+5, self.x-5, self.y-5,
        fill="black", tags= self.tag)
        self.tag_bind()
        self.selector_id = self.canvas.gettags(self.selector)
        Selector.selector_list.append(self.selector_id)

    def move(x,y, canvas):
        for item in range(0, len(Selector.selector_list)):
            canvas.move(Selector.selector_list[item], x,y)

    def delete(canvas):
        global selected, shape_id, shape_name
        for item in range(0, len(Selector.selector_list)):
            canvas.delete(Selector.selector_list[item])
        Selector.selector_list.clear()
        Selector.selector_num = 0
        selected = False
    
    def tag_bind(self):
        self.canvas.tag_bind(f'{self.tag}', "<Button-1>", self.on_click)
        self.canvas.tag_bind(f'{self.tag}', "<B1-Motion>", self.on_motion)

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    # used in tag_bind
    def on_motion(self, event):
        x = event.x - self.start_x
        y = event.y - self.start_y

        self.canvas.move(self.tag, x,y)

        shape_coords = self.canvas.coords(shape_id)

        shape_coords[self.num] += x
        shape_coords[self.num+1] +=y

        self.canvas.coords(shape_id, shape_coords)

        self.start_x = event.x
        self.start_y = event.y

class Rectangle(Shapes):

    def create(self):
        self.tag = Shapes.make_tag("rectangle")

        self.rectangle = self.canvas.create_rectangle(self.x,self.y, self.x+100, self.y+100,
        fill=self.color, tags=self.tag, outline=self.outline)
        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.rectangle)

    def make(canvas):
        r2 = Rectangle(width=width, height=height, canvas=canvas)
        r2.create()
        return r2
    
    def load(self):
        self.tag = Shapes.make_tag("rectangle")
        
        x1,y1, x2, y2 = self.coords
        self.rectangle = self.canvas.create_rectangle(x1[1:],y1, x2,y2[:-2],
        fill=self.color, tags=self.tag, outline=self.outline)

        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.rectangle)


class Oval(Shapes):

    def create(self):
        self.tag = Shapes.make_tag("oval")

        self.oval = self.canvas.create_oval(self.x,self.y, self.x+100, self.y+100,
        fill=self.color, tags=self.tag, outline=self.outline)
        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.oval)
    
    def make(canvas):
        o2 = Oval(width=width, height=height, canvas=canvas)
        o2.create()
        return o2

    def load(self):
        self.tag = Shapes.make_tag("oval")
        
        x1,y1, x2, y2 = self.coords
        self.oval = self.canvas.create_oval(x1[1:],y1, x2,y2[:-2],
        fill=self.color, tags=self.tag, outline=self.outline)

        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.oval)



class Triangle(Shapes):

    def create(self):
        self.tag = Shapes.make_tag("triangle")

        self.triangle = self.canvas.create_polygon(self.x,self.y, self.x-50,self.y+50, self.x+50,self.y+50, 
        fill=self.color, tags=self.tag, outline=self.outline)
        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.triangle)
    
    def make(canvas):
        t2 = Triangle(width=width, height=height, canvas=canvas)
        t2.create()
        return t2
    
    def load(self):
        self.tag = Shapes.make_tag("triangle")
        
        x1,y1, x2, y2, x3,y3 = self.coords
        self.triangle = self.canvas.create_polygon(x1[1:],y1, x2,y2, x3,y3[:-2],
        fill=self.color, tags=self.tag, outline=self.outline)

        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.triangle)
        

class Polygon(Shapes):

    def create(self):
        self.tag = Shapes.make_tag("polygon")

        self.polygon = self.canvas.create_polygon(self.x,self.y, self.x-25,self.y+10, self.x-25,self.y+20,
        self.x,self.y+30, self.x+20,self.y+15, fill=self.color, tags=self.tag, outline=self.outline)
        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.polygon)

    def make(canvas):
        p2 = Polygon(width=width, height=height, canvas=canvas)
        p2.create()
        return p2
    
    def load(self):
        self.tag = Shapes.make_tag("polygon")
        
        x1,y1, x2, y2, x3,y3, x4,y4, x5,y5 = self.coords
        self.polygon = self.canvas.create_polygon(x1[1:],y1, x2,y2, x3,y3, x4,y4, x5,y5[:-2],
        fill=self.color, tags=self.tag, outline=self.outline)

        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.polygon)