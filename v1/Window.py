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
        field = self.field.field

        tlpIndex = [0, 0]
        trpIndex = [0, 1]
        blpIndex = [1, 0]
        # brpIndex = [1, 1]
        
        for row in field[:-1]:
            for i in range(len(row) - 1):
                topLeftPoint = field[tlpIndex[0]][tlpIndex[1]]
                topRightPoint = field[trpIndex[0]][trpIndex[1]]
                botLeftPoint = field[blpIndex[0]][blpIndex[1]]
                # botRightPoint = field[brpIndex[0]][brpIndex[1]]

                #print(f"{topLeftPoint} {topRightPoint} {botLeftPoint}")

                if topLeftPoint.v < self.isoVal < topRightPoint.v or topLeftPoint.v > self.isoVal > topRightPoint.v:
                    print(f"{topLeftPoint.y}")
                    #
                    # print(f"{topLeftPoint.x + 40/2} {topLeftPoint.y}")
                    pygame.draw.circle(self.win, (255,0,0), (topLeftPoint.x + 40/2, topLeftPoint.y), 2)
                
                if topLeftPoint.v < self.isoVal < botLeftPoint.v or topLeftPoint.v > self.isoVal > botLeftPoint.v:
                    pygame.draw.circle(self.win, (255,0,0), (topLeftPoint.x, topLeftPoint.y + 40/2), 2)

                tlpIndex[1] += 1
                trpIndex[1] += 1
                blpIndex[1] += 1
                # brpIndex[1] += 1
            print("-------------------")
            tlpIndex[0] += 1; tlpIndex[1] = 0
            trpIndex[0] += 1; trpIndex[1] = 0
            blpIndex[0] += 1; blpIndex[1] = 0
    

    # def marchingSquare(self):
    #     first = True
    #     for row in self.field.field:
    #         for point, nextPoint in zip(row, row[1:]):
    #             if not first:
    #                 continue
    #             print(point, nextPoint)
    #             first = False
    #             if(point.v < self.isoVal < nextPoint.v):
    #                 pygame.draw.circle(self.win, (255,0,0), (point.x + 40/self.isoVal, point.y), 2)
    #             elif(point.v > self.isoVal > nextPoint.v):
    #                 pygame.draw.circle(self.win, (255,0,0), (self.x, self.y), 2) 
    #     print("Fait !")    


    def loop(self):
        while self.run:
            pygame.time.Clock().tick(self.fps)
            self.commands()
            self.render()
            self.marchingSquare()
            pygame.display.update()
