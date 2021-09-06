from pygame import sprite
from misc import import_image


class SimpleSprite(sprite.Sprite):
    def __init__(self, img:str, pos:list, size:tuple):
        super().__init__()
        self.image = import_image(img, pos, size)
        self.rect = self.image.get_rect()        
