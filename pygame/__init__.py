# pygame/__init__.py - ASCII Terminal version

from ._view import _view
from .locals import *
import os
import sys

# Màu sắc (mã ANSI cho terminal)
class Color:
    BLACK = '\033[30m'
    WHITE = '\033[37m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    PURPLE = '\033[35m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'

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
    
    def collidepoint(self, point):
        x, y = point
        return self.left <= x <= self.left + self.width and self.top <= y <= self.top + self.height
    
    def get_rect(self):
        return self

class Surface:
    def __init__(self, size):
        self.size = size
        self.width = size[0] if isinstance(size, (list, tuple)) else size
        self.height = size[1] if isinstance(size, (list, tuple)) and len(size) > 1 else size
        self._rect = None
        self.buffer = [[' ' for _ in range(self.width)] for _ in range(self.height)]
    
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
    
    def get_rect(self):
        if self._rect is None:
            self._rect = Rect(0, 0, self.width, self.height)
        return self._rect

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
    
    def __len__(self):
        return len(self.sprites)
    
    def remove(self, sprite):
        if sprite in self.sprites:
            self.sprites.remove(sprite)
    
    def empty(self):
        self.sprites = []

class sprite:
    Sprite = Sprite
    RenderPlain = RenderPlain
    
    @staticmethod
    def spritecollide(sprite, group, dokill):
        collisions = []
        if hasattr(group, 'sprites'):
            for s in group.sprites:
                if hasattr(s, 'rect') and hasattr(sprite, 'rect'):
                    if (s.rect.left < sprite.rect.left + sprite.rect.width and
                        s.rect.left + s.rect.width > sprite.rect.left and
                        s.rect.top < sprite.rect.top + sprite.rect.height and
                        s.rect.top + s.rect.height > sprite.rect.top):
                        collisions.append(s)
                        if dokill and hasattr(group, 'remove'):
                            group.remove(s)
        return collisions

class display:
    _screen = None
    
    @staticmethod
    def set_mode(size):
        os.system('clear')
        display._screen = Surface(size)
        return display._screen
    
    @staticmethod
    def set_caption(title):
        print(f"\033]0;{title}\007", end='')
    
    @staticmethod
    def set_icon(icon):
        pass
    
    @staticmethod
    def flip():
        if display._screen:
            sys.stdout.write('\033[H')
            for row in display._screen.buffer:
                print(''.join(row))
            sys.stdout.flush()

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
        import sys
        import select
        if select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1)
            if key == 'a':
                return [type('Event', (), {'type': KEYDOWN, 'key': K_LEFT})()]
            elif key == 'd':
                return [type('Event', (), {'type': KEYDOWN, 'key': K_RIGHT})()]
            elif key == 'w':
                return [type('Event', (), {'type': KEYDOWN, 'key': K_UP})()]
            elif key == 's':
                return [type('Event', (), {'type': KEYDOWN, 'key': K_DOWN})()]
            elif key == 'q':
                return [type('Event', (), {'type': QUIT})()]
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
    font.init()
    mixer.init()

def quit():
    pass

VER = (2, 5, 0)
__version__ = '2.5.0'
