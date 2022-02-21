from .Base import Shapes

class Polygon(Shapes):

    def create(self):
        self.tag = Shapes.make_tag("polygon")

        self.polygon = self.canvas.create_polygon(self.x,self.y, self.x-25,self.y+10, self.x-25,self.y+20,
        self.x,self.y+30, self.x+20,self.y+15, fill=self.color, tags=self.tag, outline=self.outline)
        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.polygon)

    def make(canvas):
        p2 = Polygon(width=Shapes.width, height=Shapes.height, canvas=canvas)
        p2.create()
        return p2
    
    def load(self):
        self.tag = Shapes.make_tag("polygon")
        
        x1,y1, x2, y2, x3,y3, x4,y4, x5,y5 = self.coords
        self.polygon = self.canvas.create_polygon(x1[1:],y1, x2,y2, x3,y3, x4,y4, x5,y5[:-2],
        fill=self.color, tags=self.tag, outline=self.outline)

        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.polygon)