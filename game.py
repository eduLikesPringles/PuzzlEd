import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1500,750))
pygame.display.set_caption('PuzzlEd')
clock = pygame.time.Clock()

WHITE = (255, 255, 255)

class Ed:
    COLOR = WHITE
    VEL = 4

    # we always start drawing a circle
    def __init__(self, x, y, radius):
        self.x =  x
        self.y = y
        self.radius = radius

    def draw(self, win):
        pygame.draw.circle(
            screen, self.COLOR, (self.x, self.y), self.radius)

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

    Edu = Ed(100, 100, 10)
    Edu.draw(screen)

    # update everything

    screen.blit(test_surface,(200, 200))

    pygame.display.update()
    clock.tick(60)