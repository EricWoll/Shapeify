from .Shape import Shapes
from Structs.Struct import Polygon as Poly

class Polygon(Shapes):

    shape_type = 'Polygon'
    shape_amount = 0

    def __init__(self, canvas, coorditanes: Poly, color, outline='', tag=None) -> None:
        self.coordinates = coorditanes
        super().__init__(canvas, color, outline, tag)

    def load(self):
        Polygon.shape_amount += 1
        self.make_tag(Polygon.shape_type, Polygon.shape_amount)
    
    def create(self):
        self.canvas.create_polygon(self.coordinates, outline = self.outline, fill = self.color)