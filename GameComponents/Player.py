import pygame

class Player:
    def __init__(self, name):
        self.name = name
        self.x = 3
        self.y = 3
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(self.x, self.y, 3, 3)
    
    def render(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), 3)
        self.rect = pygame.Rect(self.x, self.y, 3, 3)
    
    def isColliding(self, walls):
        # for wall in walls:
        #     if pygame.Rect.colliderect(self.rect, wall):
        #         return True
        # return False

        return pygame.Rect.collidelistall(self.rect, walls)

    def __str__(self) -> str:
        return f"{self.name}:({self.x}, {self.y})"