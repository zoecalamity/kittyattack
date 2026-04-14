import pygame
import random 
import math 
from pygame import mixer 


#screen size
screen_width = 800 
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height))
no_of_invaders = 8 

def init_game(): 
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Kitty Attack!")

def load_assets():
    player_image = pygame.image.load('data/spaceman.png')
    fish_image = pygame.image.load('data/fishbullet.png')
    cat_image = [pygame.image.load('data/aliencat.png') for _ in range(no_of_invaders)]
    return player_image, fish_image, cat_image


