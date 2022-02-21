from .Base import Shapes

class Oval(Shapes):

    def create(self):
        self.tag = Shapes.make_tag("oval")

        self.oval = self.canvas.create_oval(self.x,self.y, self.x+100, self.y+100,
        fill=self.color, tags=self.tag, outline=self.outline)
        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.oval)
    
    def make(canvas):
        o2 = Oval(width=Shapes.width, height=Shapes.height, canvas=canvas)
        o2.create()
        return o2

    def load(self):
        self.tag = Shapes.make_tag("oval")
        
        x1,y1, x2, y2 = self.coords
        self.oval = self.canvas.create_oval(x1[1:],y1, x2,y2[:-2],
        fill=self.color, tags=self.tag, outline=self.outline)

        self.tag_bind()
        self.shape_id = self.canvas.gettags(self.oval)