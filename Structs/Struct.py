from dataclasses import dataclass

@dataclass
class Geometry:
    '''struct '''
    width: int
    height: int
    x_pos: int = 0
    y_pos: int = 0

@dataclass
class Resizeable:
    ''' struct '''
    width: bool = True
    height: bool = True

@dataclass
class Rectangle:
    ''' struct '''
    x1: int
    y1: int
    x2: int
    y2: int

class Oval:
    ''' struct '''
    x1: int
    y1: int
    x2: int
    y2: int

@dataclass
class Triangle:
    ''' struct '''
    x1: int
    y1: int
    x2: int
    y2: int
    x3: int
    y3: int

@dataclass
class Polygon:
    ''' struct '''
    x1: int
    y1: int
    x2: int
    y2: int
    x3: int
    y3: int
    x4: int
    y4: int
    x5: int
    y5: int