import pygame
import sys


pygame.init()


screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circle")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


ball_radius = 25
ball_x = 25
ball_y = 25

movement_speed = 20

while True:
    screen.fill(WHITE)

   
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    
    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - movement_speed > 0:
                    ball_y -= movement_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + movement_speed < screen_height: 
                    ball_y += movement_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - movement_speed > 0:
                    ball_x -= movement_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + movement_speed < screen_width: 
                    ball_x += movement_speed

