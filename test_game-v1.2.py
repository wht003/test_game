import pygame
import os
import random


pygame.init()
pygame.display.set_caption("Test Game")

game_icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(game_icon)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

BLACK = (0, 0, 0)
BLUE = (30, 100, 255)
WHITE = (255, 255, 255)

points=0

screen=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(BLUE)

FPS=60
clock= pygame.time.Clock()


headsize = 80
head = pygame.transform.scale(pygame.image.load('images/head.png'), (headsize, headsize)).convert()
head_rect = head.get_rect()
head_rect.x = random.randint(0, WINDOW_WIDTH-headsize)
head_rect.y = random.randint(0, WINDOW_HEIGHT-headsize)


blockspeed = 10
blocksize = 20
block = pygame.transform.scale(pygame.image.load('images/rectangle.png'), (blocksize, blocksize)).convert()
block_rect = block.get_rect()
block_rect.x= (WINDOW_WIDTH/2)
block_rect.y= (WINDOW_HEIGHT/2)


def move():
    global blockxpos
    global blockypos

    if pygame.key.get_pressed()[pygame.K_LEFT] and (block_rect.x-blockspeed)>=0:
        block_rect.x -= blockspeed
    if pygame.key.get_pressed()[pygame.K_RIGHT] and (block_rect.x + blocksize + blockspeed) <=WINDOW_WIDTH:
        block_rect.x += blockspeed
    if pygame.key.get_pressed()[pygame.K_UP] and (block_rect.y- blockspeed) >=0:
        block_rect.y -= blockspeed
    if pygame.key.get_pressed()[pygame.K_DOWN] and (block_rect.y + blocksize + blockspeed) <=WINDOW_HEIGHT:
        block_rect.y += blockspeed

    screen.blit(block, (block_rect.x, block_rect.y))

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os.exit()

def collision():
    global points
    global WINDOW_HEIGHT, WINDOW_WIDTH

    if head_rect.colliderect(block_rect) == True:
        head_rect.x = random.randint(0, WINDOW_WIDTH-headsize)
        head_rect.y = random.randint(0, WINDOW_HEIGHT-headsize)
        
        points += 1

def display_score():
    global txt

    font = pygame.font.SysFont("Bell", 25)
    txt = font.render(f'{points} points', True, WHITE)
    screen.blit(txt, (0, 0))


while True:
    screen.fill(BLUE)

    screen.blit(head, (head_rect.x, head_rect.y))
    
    quit()
    
    move()

    collision()

    display_score()

    clock.tick(FPS)
    pygame.display.update()
