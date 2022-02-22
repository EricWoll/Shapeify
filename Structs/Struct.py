from dataclasses import dataclass

@dataclass
class Geometry:
    '''struct
    - width: int
    - height: int
    - x_pos: int = 0
    - y_pos: int = 0
    '''
    width: int
    height: int
    x_pos: int = 0
    y_pos: int = 0

@dataclass
class Resizeable:
    ''' struct
    - width: bool = True
    - height: bool = True
    '''
    width: bool = True
    height: bool = True

@dataclass
class Attributes:
    ''' struct
    - attribute: str
    - value: int
    '''
    attribute: str
    value: int