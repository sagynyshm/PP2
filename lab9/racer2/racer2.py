import pygame, sys
from pygame.locals import *
import random, time

# Initializing Pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # Initial speed of enemy and coins
SCORE = 0
ENEMY_SPEED_INCREASE_COINS = 10  # Number of coins collected to increase enemy speed

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load the background image, ensure the path is correct
background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if (self.rect.left > 0) and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if (self.rect.right < SCREEN_WIDTH) and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("coin1.png")
        # Randomly select coin size for different weights
        sizes = [(20, 20), (30, 30), (40, 40)]
        size = random.choice(sizes)
        self.image = pygame.transform.scale(original_image, size)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Initialize Sprites
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
for _ in range(5):  # Add a set number of coins initially
    coin = Coin()
    coins.add(coin)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(*coins)  # Add coins to all_sprites for easy rendering

# Main Game Loop
coin_count = 0  # Initialize coin count
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Drawing the background and score
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    coin_text = font_small.render("Coins: " + str(coin_count), True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 150, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Check for collision between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
        
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Coin collection
    coin_hit_list = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coin_hit_list:
        coin_count += 1
        # Increase speed of enemy if coin count meets certain threshold
        if coin_count % ENEMY_SPEED_INCREASE_COINS == 0:
            SPEED += 1  # Increase speed by 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.update()
    FramePerSec.tick(FPS)
