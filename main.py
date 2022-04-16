import pygame
import sys

from GeometryComponents.Window import Window

if __name__ == "__main__":
    pygame.init()

    if len(sys.argv) == 2:
        verbose = bool(sys.argv[1])
    else:
        verbose = False
    window = Window(verbose)
    window.loop()

    pygame.quit()
