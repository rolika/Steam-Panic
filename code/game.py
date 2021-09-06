from pygame import sprite, Surface
from text import SimpleText
from sprites import SimpleSprite


class Game:
    def __init__(self, screen:Surface):
        self._screen = screen
        midscreen = (screen.get_width()//2, screen.get_height()//2)

        self._text_container = sprite.Group()
        self._player_container = sprite.GroupSingle()

        self._title_text = SimpleText("Steam Panic", "m5x7.ttf", 64, "white")
        self._title_text.rect.center = midscreen
        
        self._player_sprite = SimpleSprite("Hero_idle.png", [0,0], (16,32))
        self._player_sprite.rect.center = midscreen
    
    def show_title(self):
        self._reset_containers()
        self._text_container.add(self._title_text)
        self._text_container.draw(self._screen)
        return 
    
    def play(self):
        self._reset_containers()
        self._player_container.add(self._player_sprite)
        self._player_container.draw(self._screen)
    
    def _reset_containers(self):        
        self._text_container.empty()
        self._player_container.empty()
