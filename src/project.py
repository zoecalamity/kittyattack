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
    font = pygame.font.Font('freesansbold.ttf', 20)
    game_over_font = pygame.font.Font ('freesansbold.ttf', 64)
    return screen, font, game_over_font

def load_assets():
    player_image = pygame.image.load('data/spaceman.png')
    fish_image = pygame.image.load('data/fishbullet.png')
    cat_image_raw = pygame.image.load('data/aliencat.png')

    #Scale Images 
    player_image = pygame.transform.scale(player_image, (120, 120))
    fish_image = pygame.transform.scale(fish_image, (120, 120))
    cat_image = [pygame.transform.scale(cat_image_raw, (120, 120)) for _ in range(no_of_invaders)]

    return player_image, fish_image, cat_image


def init_invaders():
    invader_x = [random.randint(64, 737) for _ in range(no_of_invaders)]
    invader_y = [random.randint(30, 180) for _ in range(no_of_invaders)]
    invader_xchange = [0.3] * no_of_invaders
    invader_ychange = [50] * no_of_invaders
    return invader_x, invader_y, invader_xchange, invader_ychange

def is_collision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
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

def show_game_over(screen, font):
    text = font.render("GAME OVER!!!", True, (255, 255, 255))
    screen.blit(text, (190, 250))

def show_win(screen, font):
    text = font.render("YOU WIN!!!", True, (255, 255, 0))
    screen.blit(text, (240, 250)) 

def main():
    screen, font, game_over_font = init_game()
    player_image, fish_image, cat_image = load_assets()

    # player state 
    player_x = 370 
    player_y = screen_height - 130 
    player_xchange = 0 

    # Invader state 
    invader_x, invader_y, invader_xchange, invader_ychange = init_invaders()

    # Bullet state
    bullet_x = 0 
    bullet_y = 500 
    bullet_ychange = 3
    bullet_state = "rest"
    game_over = False 
    game_win = False 

    # Score 
    score_val = 0 
    score_x, score_y = 5, 5 

    running = True 
    while running: 
        screen.fill((0, 0, 0))

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_xchange = -1.7 
                if event.key == pygame.K_RIGHT:
                    player_xchange = 1.7 
                if event.key == pygame.K_SPACE:
                    if bullet_state == "rest":
                        bullet_x = player_x
                        bullet_y = player_y
                        bullet_state = "fire"
            
            if event.type == pygame.KEYUP:
                player_xchange = 0 
        
        # Update player position 
        player_x += player_xchange
        player_x = max(16, min(player_x, 750))

        # Update Invader Positions 
        for i in range(no_of_invaders):
            invader_x[i] += invader_xchange[i]

        # Update Bullet Position
        if bullet_y <= 0:
            bullet_y = 600 
            bullet_state = "rest"
        if bullet_state == "fire":
            draw_bullet(screen, fish_image, bullet_x, bullet_y)
            bullet_y -= bullet_ychange

        # Update invaders and check collisions 
        for i in range(no_of_invaders):
            #Game Over Condition 
            if invader_y[i] >= 450 and abs(player_x - invader_x[i]) < 80:
                for j in range(no_of_invaders):
                    invader_y[j] = 2000 
                    game_over = True 
                    break 

            # Bounce off Walls 
            if invader_x[i] >= 735 or invader_x[i] <= 0:
                invader_xchange[i] *= -1 
                invader_y[i] += invader_ychange[i]

            #Bullet Collision 
            if is_collision(bullet_x, invader_x[i], bullet_y, invader_y[i]):
                score_val += 1 
                if score_val >= 25:
                    game_win = True 
                    break 
                bullet_y = 600 
                bullet_state = "rest"
                invader_x[i] = random.randint(64, 736)
                invader_y[i] = random.randint(30, 200)
                invader_xchange[i] *= -1 
            
            draw_invader(screen, cat_image, invader_x[i], invader_y[i], i)

        draw_player(screen, player_image, player_x, player_y)
        show_score(screen, font, score_val, score_x, score_y)
        
        if game_over: 
            show_game_over(screen, game_over_font)
            pygame.display.update()
            pygame.time.wait(3000)
            running = False 

        if game_win: 
            show_win(screen, game_over_font)
            pygame.display.update()
            pygame.time.wait(3000)
            running = False 

        pygame.display.update()
       
    pygame.quit()


if __name__ == "__main__":
    main()

