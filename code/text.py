from pygame import freetype, sprite
from pathlib import Path


FONT_FOLDER = "font"


class SimpleText(sprite.RenderUpdates):
    def __init__(self, text, fontname, size, color, pos):
        fonttype = freetype.Font(Path(FONT_FOLDER, fontname), size)
        text_sprite = sprite.Sprite()
        text_sprite.image = fonttype.render(text, color)[0]
        text_sprite.rect = text_sprite.image.get_rect(center=pos)
        super().__init__(text_sprite)