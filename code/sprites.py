from pygame import key, sprite, Surface
from pygame.locals import *

from constants import PlayerAttributes
from misc import clamp, drag, stands_on_platform


class SimpleSprite(sprite.Sprite):
    def __init__(self, size:tuple):
        super().__init__()
        self.image = Surface(size)
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.controlled = False
        self.size = size


class Platform(SimpleSprite):
    def __init__(self, size:tuple=(128,16)):
        super().__init__(size)


class CharacterSprite(SimpleSprite):
    def __init__(self, size:tuple):
        super().__init__(size)
        self.dx = 0
        self.dy = 0


class Player(CharacterSprite):
    def __init__(self, attributes:PlayerAttributes):
        super().__init__(attributes.SIZE.value)
        self.attributes = attributes
        self.rect.center = self.attributes.START_POS.value
        self._on_ladder = False
        self.on_platform = False

    def update(self):
        self._get_input()
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

    def _get_input(self):
        keys = key.get_pressed()
        if keys[K_UP] and self._on_ladder:
            self.dy -= self.attributes.CLIMB_ACCELERATION.value
            self.dy = clamp(self.dy, -self.attributes.MAX_CLIMB_SPEED.value, 0)
        elif keys[K_DOWN] and self._on_ladder:
            self.dy += self.attributes.CLIMB_ACCELERATION.value
            self.dy = clamp(self.dy, 0, self.attributes.MAX_CLIMB_SPEED.value)
        elif keys[K_RIGHT]:
            self.dx += self.attributes.RUN_ACCELERATION.value
            self.dx = clamp(self.dx, 0, self.attributes.MAX_RUN_SPEED.value)
        elif keys[K_LEFT]:
            self.dx -= self.attributes.RUN_ACCELERATION.value
            self.dx = clamp(self.dx, -self.attributes.MAX_RUN_SPEED.value, 0)
        # elif keys[K_SPACE]:
        #     self.dy -= self.attributes.JUMP_ACCELERATION.value
        else:
            drag(self)

    def _check_on_platform(self, platforms):
        platform = sprite.spritecollideany(self, platforms, collided=stands_on_platform)
        if platform:
            self.rect.bottom = platform.rect.top - 1
            self.dy = 0
            return True
        return False
