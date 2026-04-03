# pygame/__init__.py - Fake PyGame package

from ._view import _view
from .locals import *

# Màu sắc
class Color:
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    BLUE = (0,0,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    PURPLE = (255,0,255)
    YELLOW = (255,255,0)

# Hằng số
QUIT = 12
KEYDOWN = 2
KEYUP = 3

class Rect:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.x = left
        self.y = top
    
    def get_rect(self):
        return self

class Surface:
    def __init__(self, size):
        self.size = size
        self.width = size[0] if isinstance(size, (list, tuple)) else size
        self.height = size[1] if isinstance(size, (list, tuple)) and len(size) > 1 else size
    
    def fill(self, color):
        pass
    
    def get_size(self):
        return (self.width, self.height)
    
    def convert(self):
        return self
    
    def blit(self, source, dest):
        pass
    
    def set_colorkey(self, color):
        pass
    
    def set_alpha(self, alpha):
        pass

class Sprite:
    def __init__(self):
        self.rect = Rect(0, 0, 0, 0)

class RenderPlain:
    def __init__(self):
        self.sprites = []
    
    def add(self, sprite):
        self.sprites.append(sprite)
    
    def draw(self, screen):
        pass
    
    def __iter__(self):
        return iter(self.sprites)

class sprite:
    Sprite = Sprite
    RenderPlain = RenderPlain
    
    def spritecollide(self, sprite, group, dokill):
        return []

class display:
    _screen = None
    
    @staticmethod
    def set_mode(size):
        display._screen = Surface(size)
        return display._screen
    
    @staticmethod
    def set_caption(title):
        pass
    
    @staticmethod
    def set_icon(icon):
        pass
    
    @staticmethod
    def flip():
        pass

class image:
    @staticmethod
    def load(filename):
        return Surface([30, 30])
    
    @staticmethod
    def get_rect():
        return Rect(0, 0, 30, 30)

class font:
    _fonts = {}
    
    @staticmethod
    def init():
        pass
    
    class Font:
        def __init__(self, fontfile, size):
            self.fontfile = fontfile
            self.size = size
        
        def render(self, text, antialias, color):
            return Surface([len(text) * 8, 16])

class mixer:
    @staticmethod
    def init():
        pass
    
    class music:
        @staticmethod
        def load(filename):
            pass
        
        @staticmethod
        def play(loops, start):
            pass

class time:
    class Clock:
        def __init__(self):
            import time
            self.last_tick = time.time()
        
        def tick(self, fps):
            import time
            time.sleep(1.0 / fps)

class event:
    @staticmethod
    def get():
        return []

class key:
    K_LEFT = 276
    K_RIGHT = 275
    K_UP = 273
    K_DOWN = 274
    K_ESCAPE = 27
    K_RETURN = 13

class draw:
    @staticmethod
    def ellipse(surface, color, rect):
        pass

def init():
    pass

def quit():
    pass
