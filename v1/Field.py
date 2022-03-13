import random

from v1.Point import Point


class Field:
    def __init__(self, width, height):
        self.width, self.height = (width, height)
        self.res = 40
        self.cols = width // self.res
        self.rows = height // self.res
        self.field = []

    def load(self):
        for y in range(self.cols):
            self.field.append([])
            for x in range(self.rows):
                self.field[y].append(Point(x*self.res+self.width//5, y*self.res+10, random.random()))