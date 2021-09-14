from pygame import key, sprite, Surface
from pygame.locals import *


GRAVITY_ACCELERATION = 0.05

PLAYER_RUN_ACCELERATION = 0.1
PLAYER_CLIMB_ACCELERATION = 0.1
PLAYER_RUN_SPEED = 2
PLAYER_CLIMB_SPEED = 1
PLAYER_JUMP_ACCELERATION = 0.5



class Platform(sprite.Sprite):
    def __init__(self, size:tuple=(128,16)):
        super().__init__()
        self.image = Surface(size)
        self.image.fill("white")
        self.rect = self.image.get_rect()


class Player(Platform):
    def __init__(self, size:tuple=(16,32)):
        super().__init__(size)
        self._dx = 0
        self._dy = 0
    
    def update(self):
        self._get_input()
        self.rect.centerx += self._dx
        self.rect.centery += self._dy
    
    def _get_input(self):
        keys = key.get_pressed()
        if not any(keys):
            self._apply_gravity()
        if keys[K_UP]:
            self._dy -= PLAYER_CLIMB_ACCELERATION
        elif keys[K_DOWN]:            
            self._dy += PLAYER_CLIMB_ACCELERATION
        if keys[K_RIGHT]:
            self._dx += PLAYER_RUN_ACCELERATION
        elif keys[K_LEFT]:            
            self._dx -= PLAYER_RUN_ACCELERATION
        if keys[K_SPACE]:
            self._dy -= PLAYER_JUMP_ACCELERATION
    
    def _apply_gravity(self):
        self._dx = 0
        self._dy += GRAVITY_ACCELERATION
