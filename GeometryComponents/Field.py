import random

from GeometryComponents.Point import Point


class Field:
    def __init__(self, width, height):
        self.width, self.height = (width, height)
        self.res = 40
        self.cols = width // self.res
        self.rows = height // self.res
        self.field = []
        self.isoVal = random.uniform(2.1, 3.9)

    def load(self):
        with open("./Data/data.txt") as file:
            for y in range(self.cols):
                self.field.append([])
                for x in range(self.rows):
                    v = float(file.readline())
                    self.field[y].append(Point(x*self.res+10, y*self.res+10, v, int(v < self.isoVal)))
        print(f"Size of field : {len(self.field)}")
        print(f"Number of points : {len(self.field)**2}")
        print(f"Iso-value : {self.isoVal}")