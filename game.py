import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1500,750))
pygame.display.set_caption('PuzzlEd')
clock = pygame.time.Clock()

test_surface = pygame.Surface((200, 200))
test_surface.fill('Red')
# pygame.draw.polygon()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw all our elements
    # update everything

    screen.blit(test_surface,(200, 200))

    pygame.display.update()
    clock.tick(60)