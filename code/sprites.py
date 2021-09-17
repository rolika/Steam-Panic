from pygame import key, sprite, Surface
from pygame.locals import *

from misc import apply_gravity, constrain_to_screen, stands_on_platform


PLAYER_RUN_ACCELERATION = 0.1
PLAYER_CLIMB_ACCELERATION = 0.1
PLAYER_RUN_SPEED = 2
PLAYER_CLIMB_SPEED = 1
PLAYER_JUMP_ACCELERATION = 0.5


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
    def __init__(self, size:tuple=(16,32)):
        super().__init__(size)
        self.on_platform = False

    @constrain_to_screen
    @apply_gravity
    def update(self, platforms):
        self.controlled = self._get_input()
        self.on_platform = self._check_on_platform(platforms)
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        return self

    def _get_input(self):
        keys = key.get_pressed()
        if not any(keys):
            return False
        if keys[K_UP]:
            self.dy -= PLAYER_CLIMB_ACCELERATION
        elif keys[K_DOWN]:
            self.dy += PLAYER_CLIMB_ACCELERATION
        if keys[K_RIGHT]:
            self.dx += PLAYER_RUN_ACCELERATION
        elif keys[K_LEFT]:
            self.dx -= PLAYER_RUN_ACCELERATION
        if keys[K_SPACE]:
            self.dy -= PLAYER_JUMP_ACCELERATION
        return True

    def _check_on_platform(self, platforms):
        platform = sprite.spritecollideany(self, platforms, collided=stands_on_platform)
        if platform:
            self.rect.bottom = platform.rect.top - 1
            self.dy = 0
            return True
        return False
