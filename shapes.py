import pygame
from pygame import Rect, surface, color
from pygame.draw import rect

###not really using this module yet. we will see. would be nice to have the images created here and brought to main
# but not sure how yet



def create_rectange():
    white = (255, 255, 255)
    rect_x = 100
    rect_y = 100
    rect_width = 200
    rect_height = 150
    pygame.draw.rect(screen, white, rect_x, rect_y, rect_width, rect_height)




