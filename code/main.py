import pygame
from pygame.locals import *
from pygame import freetype, time  # import freetype here to initialize it
from enum import Enum
from game import Game


SCREEN_SIZE = (640, 480)
FRAMERATE = 60
BLACK = (0, 0, 0)


State = Enum("State", "TITLE INSTRUCTIONS PLAY PAUSED OVER")


class Main():
    def __init__(self, screen_size:tuple, framerate:int, state:State, background:pygame.Color) -> None:
        screen = pygame.display.set_mode(screen_size)
        clock = time.Clock()
        pygame.init()
        self._run(screen, state, framerate, clock, background)

    def _run(self, screen:pygame.Surface, state:State, framerate:int, clock:time.Clock, background:pygame.Color) -> None:

        game = Game(screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = State.OVER
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        if state == State.TITLE:
                            state = State.PLAY
                        elif state == State.OVER:
                            state = State.TITLE
                        elif state == State.PAUSED:
                            state = State.PLAY
                    if event.key == K_ESCAPE:
                        if state == State.TITLE:
                            state = State.OVER
                        elif state == State.INSTRUCTIONS:
                            state = State.TITLE
                        elif state == State.PLAY:
                            state = State.PAUSED
                        elif state == State.PAUSED:
                            state = State.PLAY
                        elif state == State.OVER:
                            state = State.TITLE


            screen.fill(background)

            if state == State.TITLE:
                game.show_title()
            elif state == State.INSTRUCTIONS:
                pass
            elif state == State.PLAY:
                game.play()
            elif state == State.PAUSED:
                pass
            elif state == State.OVER:
                pygame.quit()
                return

            pygame.display.update()
            clock.tick(framerate)


if __name__ == "__main__":
    Main(SCREEN_SIZE, FRAMERATE, State.TITLE, BLACK)
