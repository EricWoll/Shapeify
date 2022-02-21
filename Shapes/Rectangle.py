from .Base import Shapes

class Rectangle(Shapes):

    def create(self):
        self.tag = Shapes.make_tag("rectangle")

        self.rectangle = self.canvas.create_rectangle(self.x,self.y, self.x+100, self.y+100,
        fill=self.color, tags=self.tag, outline=self.outline)
        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.rectangle)

    def make(canvas):
        r2 = Rectangle(width=Shapes.width, height=Shapes.height, canvas=canvas)
        r2.create()
        return r2
    
    def load(self):
        self.tag = Shapes.make_tag("rectangle")
        
        x1,y1, x2, y2 = self.coords
        self.rectangle = self.canvas.create_rectangle(x1[1:],y1, x2,y2[:-2],
        fill=self.color, tags=self.tag, outline=self.outline)

        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.rectangle)