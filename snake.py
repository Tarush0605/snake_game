import pygame
import random
pygame.init()


# Screen
screen_size = (screen_width, screen_height) = (800,600);
screen = pygame.display.set_mode(screen_size);
pygame.display.set_caption('Snake Game');


# colors
white = (255,255,255);
black = (0,0,0);
red = (255,0,0);
green = (0,255,0);
blue = (0,0,255);


# Snake
block = 20;
x,y = (200,100);
snake = [(x,y)];
speed = (0,0);


# Miscellaneous
game_over = False;
tick_speed = 50;
score = 0;
font = pygame.font.Font('freesansbold.ttf', 20);


def check_edges(x,y):
    if x >= screen_width:
        x=0;
    elif x < 0:
        x = screen_width;

    if y >= screen_height:
        y = 0;
    elif y < 0:
        y = screen_height;
    
    return x,y;


def make_food():
    foodx = round(random.randrange(2*block, screen_width - 2*block) / block) * block;
    foody = round(random.randrange(2*block, screen_height - 2*block) / block) * block;
    while (foodx, foody) in snake:
        foodx = round(random.randrange(2*block, screen_width - 2*block) / block) * block;
        foody = round(random.randrange(2*block, screen_height - 2*block) / block) * block;
    return foodx,foody;


def draw_snake():
    for x1,y1 in snake:
        pygame.draw.rect(screen, blue, (x1, y1, block, block));


# Food
food = make_food();


while not game_over:
    for event in pygame.event.get():
        # print(event);

        if event.type == pygame.QUIT:
            game_over = True;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed = (0,-block);
            elif event.key == pygame.K_DOWN:
                speed = (0,block);
            elif event.key == pygame.K_RIGHT:
                speed = (block,0);
            elif event.key == pygame.K_LEFT:
                speed = (-block,0);
    
    x += speed[0];
    y += speed[1];
    x,y = check_edges(x,y);

    if (x,y) == food:
        score += 1;
        # while food in snake:
        food = make_food();
    else:
        snake.pop();

    for pos in snake:
        if (x,y) == pos:
            game_over = True;
            break;

    head = x,y;
    snake.insert(0, head);
    # snake.pop();

    text = font.render('Score: ' + str(score), True, white);
    text_rect = text.get_rect();
    text_rect.center = (50, 20);

    screen.fill(black);
    screen.blit(text, text_rect);
    draw_snake();
    pygame.draw.rect(screen, red, (food[0], food[1], block, block));
    pygame.display.update();

    pygame.time.delay(tick_speed);

pygame.quit();
