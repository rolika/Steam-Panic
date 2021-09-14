from pygame import sprite, Surface
from text import SimpleText
from sprites import Platform, Player


class Game:
    def __init__(self, screen:Surface):
        self._screen = screen
        midscreen = (screen.get_width()//2, screen.get_height()//2)

        self._create_containers()

        self._title_text = SimpleText("Steam Panic", "m5x7.ttf", 64, "white")
        self._title_text.rect.center = midscreen
        
        self._player_sprite = Player()
        self._player_sprite.rect.center = midscreen

        self._platform_sprite = Platform()
        self._platform_sprite.rect.center = (midscreen[0], self._screen.get_height())
    
    def show_title(self):
        self._reset_containers()
        self._text_container.add(self._title_text)
        self._text_container.draw(self._screen)
        self._text_container.update()
        return 
    
    def play(self):
        self._reset_containers()

        self._player_container.add(self._player_sprite)
        self._platform_container.add(self._platform_sprite)

        self._player_container.draw(self._screen)
        self._platform_container.draw(self._screen)

        self._player_container.update()
        self._platform_container.update()
    
    def _create_containers(self):
        self._text_container = sprite.Group()
        self._player_container = sprite.GroupSingle()
        self._platform_container = sprite.Group()
    
    def _reset_containers(self):        
        self._text_container.empty()
        self._player_container.empty()
        self._platform_container.empty()
