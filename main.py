import time

from battle import start_battle
from characters import Character, Monster
import pygame

# screen variables
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


is_defeated = False

#rect 1 variables
white = (255, 255, 255)
rect_x = 100
rect_y = 100
rect_width = 200
rect_height = 150

#rect 2 variables
other_white = (100, 50, 200)
rect2_x = 400
rect2_y = 300



# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

hero = Character("hero", 1000, 100, False)
wizard = Monster("wizard", 100, 500, 500, False)

if __name__ == '__main__':
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # draw the rectangles as long as the character is not defeated
        if not hero.is_defeated:
            rect1 = pygame.draw.rect(screen, white, (rect_x, rect_y, rect_width, rect_height))
        if not wizard.is_defeated:
            rect2 = pygame.draw.rect(screen, other_white, (rect2_x, rect2_y, rect_width, rect_height))

        # pygame setup, unsure what it does. added the sleep to slow the action. can be removed once a better way of
        # turn based action is completed
        pygame.display.flip()
        time.sleep(0.5)
        clock.tick(60)

        # starts the action between the hero and the wizard
        start_battle(hero, wizard)

    pygame.quit()


