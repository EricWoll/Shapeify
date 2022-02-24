import tkinter as tk

class TagDuplicate(Exception):
    '''Raised when there is a duplaicate tag Raised'''

class Shapes:

    tag_list = []

    def __init__(self, canvas, color, outline ='', tag = None) -> None:
        self.canvas = canvas
        self.color = color
        self.outline = outline
        self.tag = tag

    def make_tag(self, shape_type, shape_type_count):
        if self.tag == None:
            self.tag = f'{shape_type} ({shape_type_count})'
        else:
            if self.tag in Shapes.tag_list:
                raise TagDuplicate(f'There was a Duplicate tag: {self.tag}')