import pygame
import random
pygame.init()

# Constants
W, H = 1200, 800
FPS = 60

# Colors
BG_COLOR = (0, 0, 0)

# Game States
GAME_RUNNING, GAME_PAUSED, GAME_MENU = "Running", "Paused", "Menu"
game_state = GAME_MENU  # Start the game in the menu state

# Initialize screen and clock
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Initialize paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Initialize ball
ballRadius = 20
ballSpeed = 6
ball = pygame.Rect(random.randrange(0, W), H // 2, ballRadius, ballRadius)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)

# Sound
collision_sound = pygame.mixer.Sound('catch.mp3')  # Make sure you have a sound file named 'catch.mp3'

# Block class
class Block:
    def __init__(self, block_rect, color, unbreakable=False, bonus=False):
        self.rect = block_rect
        self.color = color
        self.unbreakable = unbreakable
        self.bonus = bonus
        self.num_hits = 3 if bonus else 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def hit(self):
        global game_score
        if not self.unbreakable:
            self.num_hits -= 1
            if self.num_hits <= 0:
                game_score += 10
                return True
        return False

# Initialize blocks
block_list = []
colors = [(230, 230, 250), (220, 20, 60)]
for i in range(10):
    for j in range(4):
        block_rect = pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50)
        color = colors[random.randint(0, 1)]
        block_list.append(Block(block_rect, color))

def draw_menu():
    # Draw the menu
    menu_font = pygame.font.SysFont('comicsansms', 50)
    continue_text = menu_font.render('Press SPACE to start', True, (255, 255, 255))
    quit_text = menu_font.render('Press Q to quit', True, (255, 255, 255))
    screen.blit(continue_text, (W//2 - continue_text.get_width()//2, H//2 - 100))
    screen.blit(quit_text, (W//2 - quit_text.get_width()//2, H//2))

def toggle_pause():
    global game_state
    if game_state == GAME_PAUSED:
        game_state = GAME_RUNNING
    else:
        game_state = GAME_PAUSED

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and game_state == GAME_RUNNING:
                toggle_pause()
            if event.key == pygame.K_SPACE and game_state == GAME_MENU:
                game_state = GAME_RUNNING
            if event.key == pygame.K_q:
                pygame.quit()
                exit()

    screen.fill(BG_COLOR)

    if game_state == GAME_RUNNING:
        # Game logic and drawing go here
        pygame.draw.rect(screen, (255, 255, 255), paddle)
        pygame.draw.ellipse(screen, (255, 0, 0), ball)

        ball.x += dx * ballSpeed
        ball.y += dy * ballSpeed

        # Ball collision with walls
        if ball.left <= 0 or ball.right >= W:
            dx = -dx
        if ball.top <= 0 or ball.colliderect(paddle):
            dy = -dy

        # Ball collision with blocks
        for block in block_list[:]:
            if ball.colliderect(block.rect):
                block.hit() and block_list.remove(block)
                dy = -dy
                collision_sound.play()
                break

        # Game over
        if ball.bottom >= H:
            game_state = GAME_MENU

        # Draw blocks
        for block in block_list:
            block.draw(screen)

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddleSpeed
        if keys[pygame.K_RIGHT] and paddle.right < W:
            paddle.x += paddleSpeed

        # Score display
        score_surface = game_score_fonts.render('Score: ' + str(game_score), False, (255, 255, 255))
        screen.blit(score_surface, (50, 10))

    elif game_state == GAME_PAUSED or game_state == GAME_MENU:
        draw_menu()

    pygame.display.flip()
    clock.tick(FPS)


