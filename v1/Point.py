from random import random

import pygame


class Point:
    def __init__(self, x, y, v, bVal):
        self.x = x
        self.y = y
        self.v = v
        self.bVal = bVal
        self.hue = int((self.v % int(self.v)) * 255)
        self.color = (self.hue, self.hue, self.hue)
        self.font = pygame.font.SysFont("times new roman", 10)
        self.verbose = False

        #self.color = (255, 255, 255)

    def render(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), 2)

        if self.verbose:
            scalar_label = self.font.render(str(self.bVal), True, (255,255,255))
            # scalar_label = self.font.render("%.3f" % self.v, True, (255,255,255))
            win.blit(scalar_label, (self.x + scalar_label.get_width() // 2 - 6, self.y))

    def __str__(self):
        return f"({self.x},{self.y},{'%.3f' % self.v})"
