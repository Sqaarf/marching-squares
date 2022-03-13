from random import random

import pygame


class Point:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
        self.hue = int(self.v * 255)
        self.color = (self.hue, self.hue, self.hue)
        self.font = pygame.font.SysFont("times new roman", 10)

        #self.color = (255, 255, 255)

    def render(self, win):
        scalar_label = self.font.render("%.3f" % self.v, True, (255,255,255))

        pygame.draw.circle(win, self.color, (self.x, self.y), 2)
        win.blit(scalar_label, (self.x + scalar_label.get_width() // 2, self.y))

    def __str__(self):
        return f"({self.x},{self.y})"
