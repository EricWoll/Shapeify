class Selector():

    selector_num = 0
    selector_list = []
    parent_shape_id = 0

    selected = False

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.tag = f'selector{Selector.selector_num}'
        self.num = Selector.selector_num
        Selector.selector_num +=2

    def create(self, coord_connect):
        Selector.selected = True
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
        for item in range(0, len(Selector.selector_list)):
            canvas.delete(Selector.selector_list[item])
        Selector.selector_list.clear()
        Selector.selector_num = 0
        Selector.selected = False
    
    def tag_bind(self):
        self.canvas.tag_bind(f'{self.tag}', "<Button-1>", self.on_click)
        self.canvas.tag_bind(f'{self.tag}', "<B1-Motion>", self.on_motion)

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def assign_id(shape_id):
        Selector.parent_shape_id = shape_id

    # used in tag_bind
    def on_motion(self, event):
        x = event.x - self.start_x
        y = event.y - self.start_y

        self.canvas.move(self.tag, x,y)

        shape_coords = self.canvas.coords(self.parent_shape_id)

        shape_coords[self.num] += x
        shape_coords[self.num+1] +=y

        self.canvas.coords(self.parent_shape_id, shape_coords)

        self.start_x = event.x
        self.start_y = event.y