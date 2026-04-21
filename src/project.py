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

def init_invaders():
    invader_x = [random.randint(64, 737) for _ in range(no_of_invaders)]
    invader_y = [random.randint(30, 180) for _ in range(no_of_invaders)]
    invader_xchange = [1.2] * no_of_invaders
    invader_ychange = [50] * no_of_invaders
    return invader_x, invader_y, invader_xchange, invader_ychange

def is_collision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1, y2, 2)))
    return distance <= 50 

def draw_player(screen, image, x, y):
    screen.blit(image, (x - 16, y + 10))

def draw_invader(screen, images, x, y, i):
    screen.blit(images[i], (x,y))

def draw_bullet(screen, image, x, y):
    screen.blit(image, (x,y))

def show_score(screen, font, score_val, x, y):
    score = font.render("Points:" + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))


pygame.quit()