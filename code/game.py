from pygame import sprite, Surface

from constants import PlayerAttributes
from text import SimpleText
from sprites import Player


class Game:
    def __init__(self, screen:Surface):
        self._screen = screen
        midscreen = (screen.get_width()//2, screen.get_height()//2)

        self._create_containers()

        self._title_text = SimpleText("Steam Panic", "m5x7.ttf", 64, "white")
        self._title_text.rect.center = midscreen

        self._player_sprite = Player(PlayerAttributes)

    def show_title(self):
        self._reset_containers()
        self._text_container.add(self._title_text)
        self._text_container.draw(self._screen)
        self._text_container.update()

    def play(self):
        self._reset_containers()

        self._player_container.add(self._player_sprite)

        self._player_container.draw(self._screen)

        self._player_container.update()
        self._keep_inside(self._player_sprite, self._screen)

    def _create_containers(self):
        self._text_container = sprite.Group()
        self._player_container = sprite.GroupSingle()

    def _reset_containers(self):
        self._text_container.empty()
        self._player_container.empty()
    
    def _keep_inside(self, element:sprite.Sprite, area:Surface):
        if not area.get_rect().contains(element.rect):
            element.rect.clamp_ip(area.get_rect())
