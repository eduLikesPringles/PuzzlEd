import pygame
from sys import exit
import math
import random

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
        self.x =  x
        self.y = y
        self.size = size
        self.colors = ['Red', 'Green', 'Blue']
        self.color = self.colors[0]
        self.shapes = ['circle', 'square', 'triangle']
        self.shape = self.shapes[0]
        # the size is the Area in units of px**2

    def resize(self):
        pass

    def recolor(self):
        self.color = random.choice(self.colors)

    def reshape(self):
        self.shape = random.choice(self.shapes)

    def draw(self, win):
        if self.shape == 'circle':
            pygame.draw.circle(
                screen, self.color, (self.x, self.y), math.sqrt(self.size/math.pi))
        elif self.shape == 'square':
            pygame.draw.rect(
                screen, self.color, (self.x - math.sqrt(self.size) / 2, self.y - math.sqrt(self.size) / 2, math.sqrt(self.size), math.sqrt(self.size)))
        elif self.shape == 'triangle':
            pygame.draw.polygon(
                screen, self.color, [(self.x, self.y - math.sqrt(2 * math.sqrt(3) / 9 * self.size)), (self.x - 0.9 * (math.sqrt(self.size / math.sqrt(3))), (self.y + 0.9 * (math.sqrt(2 * math.sqrt(3) / 9 * self.size)))), (self.x + 0.9 * (math.sqrt(self.size / math.sqrt(3))), (self.y + 0.9 * (math.sqrt(2 * math.sqrt(3) / 9 * self.size))))])

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

Edu1 = Ed('circle', 100, 100, 10000)
Edu1.draw(screen)
Edu3 = Ed('triangle', 500, 100, 10000)
Edu3.draw(screen)
Edu2 = Ed('square', 900, 100, 10000)
Edu2.draw(screen)

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                Edu1.size += 1000
            elif mouse_presses[2]:
                Edu1.size -= 1000

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        Edu1.x -= 10
    if keys[pygame.K_d]:
        Edu1.x += 10
    if keys[pygame.K_w]:
        Edu1.y -= 10
    if keys[pygame.K_s]:
        Edu1.y += 10
    if keys[pygame.K_SPACE]:
        Edu1.recolor()
    if keys[pygame.K_LCTRL]:
        Edu1.reshape()

    buttons = pygame.mouse.get_pressed()
    if buttons[pygame.BUTTON_LEFT]:
        Edu1.size += 1000

    # draw all our elements

    # update everything

    # screen.blit(screen,(200, 200))
    screen.fill((0,0,0))
    Edu1.draw(screen)
    pygame.display.update()
    clock.tick(60)