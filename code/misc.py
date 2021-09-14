from pygame import image, Rect, Surface
from pathlib import Path


GFX_FOLDER = "gfx"


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
