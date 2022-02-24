from .Shape import Shapes
from Structs.Struct import Rectangle as Rect

class Rectangle(Shapes):

    shape_type = 'Rectangle'
    shape_amount = 0

    def __init__(self, canvas, coorditanes: Rect, color, outline='', tag=None) -> None:
        self.coordinates = coorditanes
        super().__init__(canvas, color, outline, tag)

    def load(self):
        Rectangle.shape_amount += 1
        self.make_tag(Rectangle.shape_type, Rectangle.shape_amount)
    
    def create(self):
        self.canvas.create_rectangle(self.coordinates, outline = self.outline, fill = self.color)