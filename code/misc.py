from pygame import image, Rect, Surface
from pathlib import Path


GFX_FOLDER = "gfx"

GRAVITY_ACCELERATION = 0.05
SCREEN_SIZE = (640, 480)


def import_image(img:str, pos:list=[0,0], size:tuple=None) -> Surface:
    img = image.load(Path(GFX_FOLDER, img))
    if size:
        img = img.subsurface(Rect(pos, size)).copy()  # copy: don't want to remember the parent surface
    return img.convert_alpha()


def import_frames(img:str, num_of_frames:int, size:tuple) -> list:
    frames = []
    x = 0
    for _ in range(num_of_frames):
        frames.append(import_image(img, (x,0), size))
        x += size[0]
    return frames


def apply_gravity(update):
    def gravitate(element, platforms):
        if not (element.controlled or element.on_platform):
            element.dx = 0
            element.dy += GRAVITY_ACCELERATION
        return update(element, platforms)
    return gravitate


def constrain_to_screen(update):
    def constrain(element, platforms):
        left_limit = element.size[0] // 2 + 1
        right_limit = SCREEN_SIZE[0] - left_limit
        top_limit = element.size[1] // 2 + 1
        bottom_limit = SCREEN_SIZE[1] - top_limit
        if element.rect.centerx < left_limit:
            element.rect.centerx = left_limit
            element.dx = 0
        if element.rect.centerx > right_limit:
            element.rect.centerx = right_limit
            element.dx = 0
        if element.rect.centery < top_limit:
            element.rect.centery = top_limit
            element.dy = 0
        if element.rect.centery > bottom_limit:
            element.rect.centery = bottom_limit
            element.dy = 0
        return update(element, platforms)
    return constrain

def stands_on_platform(character, platform):
    return character.rect.bottom >= platform.rect.top and platform.rect.left <= character.rect.left and platform.rect.right >= character.rect.right
