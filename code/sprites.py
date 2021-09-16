from pygame import key, sprite, Surface
from pygame.locals import *

from misc import apply_gravity

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
        self.controlled = False


class Player(Platform):
    def __init__(self, size:tuple=(16,32)):
        super().__init__(size)
        self.dx = 0
        self.dy = 0
    
    @apply_gravity
    def update(self):
        self.controlled = self._get_input()
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
