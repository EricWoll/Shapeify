from .Shape import Shapes
from Structs.Struct import Triangle as Tri

class Triangle(Shapes):

    shape_type = 'Oval'
    shape_amount = 0

    def __init__(self, canvas, coorditanes: Tri, color, outline='', tag=None) -> None:
        self.coordinates = coorditanes
        super().__init__(canvas, color, outline, tag)

    def load(self):
        Triangle.shape_amount += 1
        self.make_tag(Triangle.shape_type, Triangle.shape_amount)
    
    def create(self):
        self.canvas.create_oval(self.coordinates, outline = self.outline, fill = self.color)