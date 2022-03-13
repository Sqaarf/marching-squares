import pygame

from v1.Window import Window

if __name__ == "__main__":
    pygame.init()

    window = Window()
    window.loop()

    pygame.quit()
