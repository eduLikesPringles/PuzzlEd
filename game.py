import pygame
from sys import exit
import math

pygame.init()
screen = pygame.display.set_mode((1500,750))
pygame.display.set_caption('PuzzlEd')
clock = pygame.time.Clock()

WHITE = (255, 255, 255)

class Ed:
    COLOR = WHITE
    VEL = 4

    # we always start drawing a circle
    def __init__(self, shape, x, y, size):
        self.shape = shape
        self.x =  x
        self.y = y
        self.size = size
        # the size is the Area in units of px**2

    def reshape(self):
        pass

    def draw(self, win):
        if self.shape == 'circle':
            pygame.draw.circle(
                screen, self.COLOR, (self.x, self.y), math.sqrt(self.size/math.pi))
        elif self.shape == 'square':
            pygame.draw.rect(
                screen, self.COLOR, (self.x - math.sqrt(self.size) / 2, self.y - math.sqrt(self.size) / 2, math.sqrt(self.size), math.sqrt(self.size)))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

test_surface = pygame.Surface((200, 200))
# test_surface.fill('Red')
pygame.draw.polygon(test_surface, 'Red', [(100, 100), (100, 200), (200, 200)])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw all our elements

    Edu1 = Ed('circle', 100, 100, 1000)
    Edu1.draw(screen)
    Edu2 = Ed('square', 100, 100, 1000)
    Edu2.draw(screen)

    # update everything

    screen.blit(test_surface,(200, 200))

    pygame.display.update()
    clock.tick(60)