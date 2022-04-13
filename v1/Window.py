import pygame

from Field import Field
import numpy as np


class Window:
    def __init__(self):
        self.width, self.height = (800, 800)
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Marching squares')

        self.fps = 30
        self.run = True

        self.field = Field(self.width, self.height)
        self.field.load()

        self.isoVal = 2.4

    def commands(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.run = False

    def render(self):
        self.win.fill((0, 0, 0))
        for row in self.field.field:
            for point in row:
                point.render(self.win)
    
    def marchingSquare(self):
        first = True
        for row in self.field.field:
            for point, nextPoint in zip(row, row[1:]):
                if not first:
                    continue
                print(point, nextPoint)
                first = False
                if(point.v < self.isoVal < nextPoint.v):
                    pygame.draw.circle(self.win, (255,0,0), (point.x + 40/self.isoVal, point.y), 2)
                elif(point.v > self.isoVal > nextPoint.v):
                    pygame.draw.circle(self.win, (255,0,0), (self.x, self.y), 2) 
        print("Fait !")    
                    

    def loop(self):
        while self.run:
            pygame.time.Clock().tick(self.fps)
            self.commands()
            self.render()
            self.marchingSquare()
            pygame.display.update()
