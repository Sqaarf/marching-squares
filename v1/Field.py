import random

from Point import Point


class Field:
    def __init__(self, width, height):
        self.width, self.height = (width, height)
        self.res = 40
        self.cols = width // self.res
        self.rows = height // self.res
        self.field = []

    def load(self):
        with open("./data.txt") as file:
            for y in range(self.cols):
                self.field.append([])
                for x in range(self.rows):
                    self.field[y].append(Point(x*self.res+10, y*self.res+10, float(file.readline())))
        print(f"Size of field : {len(self.field)}")
        print(f"Number of points : {len(self.field)**2}")