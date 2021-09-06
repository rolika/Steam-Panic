from pygame import Color, freetype, sprite
from pathlib import Path


FONT_FOLDER = "font"


class SimpleText(sprite.Sprite):
    def __init__(self, text:str, fontname:str, size:tuple, color:Color):
        super().__init__()
        fonttype = freetype.Font(Path(FONT_FOLDER, fontname), size)
        self.image = fonttype.render(text, color)[0]
        self.rect = self.image.get_rect()