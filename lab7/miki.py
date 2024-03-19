import pygame
import sys
import datetime


pygame.init()


screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clock")

clock_image = pygame.image.load("C:/Users/Asus/Downloads/clock.jpg")  
right_hand_image = pygame.image.load("C:/Users/Asus/Downloads/MicrosoftTeams-image.png")  
left_hand_image = pygame.image.load("C:/Users/Asus/Downloads/MicrosoftTeams-image (1).png")  


hand_center = (screen_width // 2, screen_height // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    current_time = datetime.datetime.now()

   
    minute_angle = 360 * (current_time.minute / 60)
    second_angle = 360 * (current_time.second / 60)

    # Rotate hand images
    rotated_right_hand = pygame.transform.rotate(right_hand_image, -minute_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand_image, -second_angle)

    
    screen.fill((255, 255, 255))

   
    screen.blit(clock_image, (0, 0))  
    screen.blit(rotated_right_hand, rotated_right_hand.get_rect(center=hand_center))
    screen.blit(rotated_left_hand, rotated_left_hand.get_rect(center=hand_center))


    pygame.display.flip()



pygame.quit()
sys.exit()
