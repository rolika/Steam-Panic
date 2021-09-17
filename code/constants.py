import enum


State = enum.Enum("State", "TITLE INSTRUCTIONS PLAY PAUSED OVER")


class GameAttributes(enum.Enum):
    GFX_FOLDER = "gfx"


class ScreenAttributes(enum.Enum):
    SIZE = (640, 480)
    FRAMERATE = 60
    BACKGROUND = (0, 0, 0)


class PlayerAttributes(enum.Enum):
    SIZE = (16, 32)
    GRAVITY_ACCELERATION = 0.05
    RUN_ACCELERATION = 0.1
    CLIMB_ACCELERATION = 0.1
    JUMP_ACCELERATION = 0.5
