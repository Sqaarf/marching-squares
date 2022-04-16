import pygame

from Field import Field
from Point import Point


class Window:
    def __init__(self, verbose):
        self.width, self.height = (800, 800)
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Marching squares')

        self.fps = 30
        self.run = True

        self.verbose = verbose

        self.field = Field(self.width, self.height)
        self.field.load()

    def commands(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.run = False

    def render(self):
        self.win.fill((0, 0, 0))
        
        for row in self.field.field:
            for point in row:
                point.render(self.win, self.verbose)
        

    def marchingSquare(self):
        field = self.field.field

        tlpIndex = [0, 0]
        trpIndex = [0, 1]
        blpIndex = [1, 0]
        brpIndex = [1, 1]

        for i in range(len(field[:-1])):
            for j in range(len(field[:-1][i]) - 1):
                topLeftPoint = field[tlpIndex[0]][tlpIndex[1]]
                topRightPoint = field[trpIndex[0]][trpIndex[1]]
                botRightPoint = field[brpIndex[0]][brpIndex[1]]
                botLeftPoint = field[blpIndex[0]][blpIndex[1]]

                a = (topLeftPoint.x + 40 / 2, topLeftPoint.y)
                b = (topRightPoint.x, topRightPoint.y + 40 / 2)
                c = (botLeftPoint.x + 40 / 2, botLeftPoint.y)
                d = (topLeftPoint.x, topLeftPoint.y + 40 / 2)

                state = self.getState(topLeftPoint, topRightPoint, botRightPoint, botLeftPoint)
                self.drawIsoLines(state, a, b, c, d)

                tlpIndex[1] += 1
                trpIndex[1] += 1
                blpIndex[1] += 1
                brpIndex[1] += 1
            tlpIndex[0] += 1
            tlpIndex[1] = 0
            trpIndex[0] += 1
            trpIndex[1] = 1
            brpIndex[0] += 1
            brpIndex[1] = 1
            blpIndex[0] += 1
            blpIndex[1] = 0

    def getState(self, tlp: Point, trp: Point, brp: Point, blp: Point, ):
        return tlp.bVal * 8 + trp.bVal * 4 + brp.bVal * 2 + blp.bVal * 1

    def drawIsoLines(self, state: int, a: tuple, b: tuple, c: tuple, d: tuple):

        if state == 1:
            pygame.draw.line(self.win, (255, 255, 255), c, d, 2)
        elif state == 2:
            pygame.draw.line(self.win, (255, 255, 255), b, c, 2)
        elif state == 3:
            pygame.draw.line(self.win, (255, 255, 255), b, d, 2)
        elif state == 4:
            pygame.draw.line(self.win, (255, 255, 255), a, b, 2)
        elif state == 5:
            pygame.draw.line(self.win, (255, 255, 255), a, d, 2)
            pygame.draw.line(self.win, (255, 255, 255), b, c, 2)
        elif state == 6:
            pygame.draw.line(self.win, (255, 255, 255), a, c, 2)
        elif state == 7:
            pygame.draw.line(self.win, (255, 255, 255), a, d, 2)
        elif state == 8:
            pygame.draw.line(self.win, (255, 255, 255), a, d, 2)
        elif state == 9:
            pygame.draw.line(self.win, (255, 255, 255), a, c, 2)
        elif state == 10:
            pygame.draw.line(self.win, (255, 255, 255), a, b, 2)
            pygame.draw.line(self.win, (255, 255, 255), c, d, 2)
        elif state == 11:
            pygame.draw.line(self.win, (255, 255, 255), a, b, 2)
        elif state == 12:
            pygame.draw.line(self.win, (255, 255, 255), b, d, 2)
        elif state == 13:
            pygame.draw.line(self.win, (255, 255, 255), b, c, 2)
        elif state == 14:
            pygame.draw.line(self.win, (255, 255, 255), c, d, 2)

    def loop(self):
        while self.run:
            pygame.time.Clock().tick(self.fps)
            self.commands()
            self.render()
            self.marchingSquare()
            pygame.display.update()
