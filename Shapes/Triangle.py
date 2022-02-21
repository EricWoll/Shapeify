from .Base import Shapes

class Triangle(Shapes):

    def create(self):
        self.tag = Shapes.make_tag("triangle")

        self.triangle = self.canvas.create_polygon(self.x,self.y, self.x-50,self.y+50, self.x+50,self.y+50, 
        fill=self.color, tags=self.tag, outline=self.outline)
        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.triangle)
    
    def make(canvas):
        t2 = Triangle(width=Shapes.width, height=Shapes.height, canvas=canvas)
        t2.create()
        return t2
    
    def load(self):
        self.tag = Shapes.make_tag("triangle")
        
        x1,y1, x2, y2, x3,y3 = self.coords
        self.triangle = self.canvas.create_polygon(x1[1:],y1, x2,y2, x3,y3[:-2],
        fill=self.color, tags=self.tag, outline=self.outline)

        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.triangle)