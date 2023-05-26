import pygame,random,sys
from pygame.locals import *

WINDOW = (630,480)
TILE_SIZE = 15
XTILES = WINDOW[0]//TILE_SIZE
YTILES = WINDOW[1]//TILE_SIZE
MOVESPEED = 8
DARK_GREEN = (0, 128,  0)
DARK_GRAY = (75, 75, 75)

pygame.init()
SURF = pygame.display.set_mode(WINDOW)
CLOCK = pygame.time.Clock()

snake = pygame.rect.Rect(0,0,TILE_SIZE,TILE_SIZE)
food = pygame.rect.Rect(0,0,TILE_SIZE,TILE_SIZE)

def draw_grid():
    [pygame.draw.line(SURF,DARK_GRAY,(0,i),(WINDOW[0],i)) for i in range(0,WINDOW[1],TILE_SIZE)]
    [pygame.draw.line(SURF,DARK_GRAY,(i,0),(i,WINDOW[1])) for i in range(0,WINDOW[0],TILE_SIZE)]

def rand_tile():
    return random.randint(1,XTILES-1),random.randint(1,YTILES-1)

def draw_snake(segments):
    for i in segments:
        pygame.draw.rect(SURF,'green',i)
    pygame.draw.rect(SURF, 'green', snake)
    pygame.draw.rect(SURF, DARK_GREEN, snake,5)

def self_eat(segments):
    for i in segments[:-1]:
        if i.center == snake.center:
            return 1
    return 0

restart = True
segments = []
dir = 'None'
len = 1

while True:
    SURF.fill('black')
    if restart:
        m, n = rand_tile()
        snake.topleft = (m * TILE_SIZE, n * TILE_SIZE)
        x, y = rand_tile()
        food.topleft = (x * TILE_SIZE, y * TILE_SIZE)
        restart = False
        segments = [snake.copy()]
        len = 1
    pygame.draw.rect(SURF,'red',food)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key in (K_UP,K_w):
                dir = 'up'
            if event.key in (K_LEFT,K_a):
                dir = 'left'
            if event.key in (K_DOWN, K_s):
                dir = 'down'
            if event.key in (K_RIGHT, K_d):
                dir = 'right'
    if dir == 'up':
        snake.top -= TILE_SIZE
    elif dir == 'left':
        snake.left -= TILE_SIZE
    elif dir == 'down':
        snake.top += TILE_SIZE
    elif dir == 'right':
        snake.left += TILE_SIZE
    if snake.center == food.center:
        len += 1
        segments.append(snake.copy())
        x, y = rand_tile()
        food.topleft = (x * TILE_SIZE, y * TILE_SIZE)
    if self_eat(segments):
        restart = True
        dir = None
    if snake.top < 0 or snake.left < 0 or snake.right > WINDOW[0] or snake.bottom > WINDOW[1]:
        restart = True
        dir = None
    draw_snake(segments)
    segments.append(snake.copy())
    del segments[0]
    draw_grid()
    pygame.display.update()
    CLOCK.tick(10)

