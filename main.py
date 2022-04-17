import pygame
import sys

from GeometryComponents.Window import Window
from GameComponents.Player import Player

if __name__ == "__main__":
    pygame.init()
    
    window = Window(Player("Sqaarf"))
    window.loop()

    pygame.quit()
