import pygame
import sys

from GeometryComponents.Window import Window

if __name__ == "__main__":
    pygame.init()

    if len(sys.argv) == 2:
        if sys.argv[1] == "--verbose":
            verbose = True
        else:
            verbose = False
    else:
        verbose = False
    window = Window(verbose)
    window.loop()

    pygame.quit()
