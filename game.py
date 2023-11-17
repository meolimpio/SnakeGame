import pygame, random
from pygame.locals import *


def on_grid():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision(cel1, cel2):
    return (cel1[0] == cel2[0] and (cel1[1] == cel2[1]))

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0, 0, 255))

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
apple_position = on_grid()

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT :
                my_direction = LEFT

    if collision(snake[0], apple_position):
        apple_position = on_grid()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_position)
    
    for position in snake:
        screen.blit(snake_skin, position)
    
    pygame.display.update()