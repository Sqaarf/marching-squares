import pygame

class Player:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.color = (255, 0, 0)
    
    def render(self, win):
         pygame.draw.circle(win, self.color, (self.x, self.y), 3)

    def __str__(self) -> str:
        return f"{self.name}:({self.x}, {self.y})"