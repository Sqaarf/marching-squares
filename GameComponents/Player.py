import pygame

class Player:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
    
    def render(self):
        pygame.draw.circle()

    def __str__(self) -> str:
        return f"{self.name}:({self.x}, {self.y})"