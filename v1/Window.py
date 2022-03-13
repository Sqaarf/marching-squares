import pygame

from v1.Field import Field


class Window:
    def __init__(self):
        self.width, self.height = (600, 400)
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Marching squares')

        self.fps = 30
        self.run = True

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
                point.render(self.win)

    def loop(self):
        while self.run:
            pygame.time.Clock().tick(self.fps)
            self.commands()
            self.render()
            pygame.display.update()
