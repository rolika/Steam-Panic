from pygame import Surface
from text import SimpleText


class Game:
    def __init__(self, screen:Surface):
        self._screen = screen
        midscreen = (screen.get_width()//2, screen.get_height()//2)

        self._title_text = SimpleText("Steam Panic", "m5x7.ttf", 64, "white", midscreen)
    
    def show_title(self):
        return self._title_text.draw(self._screen)