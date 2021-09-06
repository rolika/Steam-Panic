from pygame import image, Rect, Surface
from pathlib import Path


GFX_FOLDER = "gfx"


def import_image(img:str, pos:list=[0,0], size:tuple=None) -> Surface:
    """Load a single image from a graphic file, at the position and in size provided.
    If size is not povided, load the entire image."""
    img = image.load(Path(GFX_FOLDER, img))
    if size:
        img = img.subsurface(Rect(pos, size)).copy()  # copy: don't want to remember the parent surface
    return img.convert_alpha()
