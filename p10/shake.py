import pygame
import random
import time
import sys

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 100)
black= (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue= (30, 56, 186)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('snake game by stupid cow')

clock = pygame.time.Clock()

def gameLoop():
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


gameLoop()

