import tkinter as tk
from Structs.Struct import Geometry, Resizeable

class Window:
    '''
    Creates and manages windows
    '''

    def __init__(self, title: str, dimentions: Geometry, resizeable: Resizeable) -> None:
        self.make()
        self.set_title(title)
        self.size_window(dimentions)
        self.is_resizeable(resizeable)

    def make(self) -> None:
        '''
        Creates a Tk() window
        '''
        self.window =  tk.Tk()

    def set_title(self, title) -> None:
        '''
        Adds a custom title to the window

        Arguments:
        - title: the string that the window title gets set to
        '''
        self.window.title(title)

    def size_window(self, dimentions: Geometry, is_centered = False) -> None:
        '''
        Sets the size and position of the Window

        Arguments:
        - dimentions (struct): holds width, height, x position, and y position of the window
        - is_centered: defines whether or not window is centered on user's screen
        '''
        self._find_screen_size()
        
        if is_centered:
            dimentions.x_pos = (self.screen_width//2 - dimentions.width//2)
            dimentions.y_pos = (self.screen_height//2 - dimentions.height//2)

        self.window.geometry(dimentions.width, dimentions.height, dimentions.x_pos, dimentions.y_pos)
    
    def _find_screen_size(self) -> None:
        '''
        Gets the size of the user's screen
        '''
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
    
    def is_resizeable(self, resizeable: Resizeable) -> None:
        '''
        Sets resizeablility of the window

        Arguments:
        - resizeable (struct): holds width and height resizeablility
        '''
        self.resizeable = resizeable
        self.window.resizable(self.resizeable.width, self.resizeable.height)
    
    def win_raise(self, up_to_window = None):
        '''
        Raises window above "up_to_window"

        Arguments:
        - up_to_window: window that current window goes above
        '''
        if up_to_window == None:
            self.window.lift()
        else:
            self.window.lift(up_to_window)
    
    def win_lower(self, down_to_window = None):
        '''
        Lowers window below "down_to_window"

        Arguments:
        - down_to_window: window that current window goes below
        '''
        if down_to_window == None:
            self.window.lower()
        else:
            self.window.lower(down_to_window)
