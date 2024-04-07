import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


class Block:
    def __init__(self, block_rect, color_list, unbreakable=False, bonus=False):
        self.rect = block_rect
        self.color = color_list
        self.unbreakable = unbreakable
        self.bonus = bonus
        self.num_hits = 3 if bonus else 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color[0], self.rect)

    def hit(self):
        if not self.unbreakable:
            self.num_hits -= 1
            if self.num_hits == 0:
                if self.bonus:
                    return self.handle_bonus()
                else:
                    return True
        return False

    def handle_bonus(self):
        global ballRadius
        ballRadius += 5  # Increase ball size
        return True


#block settings
block_list = []

for i in range(10):
    for j in range(4):
        block_rect = pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50)
        unbreakable = (i % 3 == 0)
        bonus = (i % 6 == 0 and j % 2 == 0)
        if unbreakable:
            color_list = (230, 230, 250)
        elif bonus:
            color_list = (220, 20, 60)
        else:
            color_list = [(random.randrange(0, 255), random.randrange(0, 255),  random.randrange(0, 255))] 
        block_list.append(Block(block_rect, color_list, unbreakable, bonus))

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

incrSpeed = pygame.USEREVENT + 1
shrinkPaddle = pygame.USEREVENT + 2
pygame.time.set_timer(incrSpeed, 2000)
pygame.time.set_timer(shrinkPaddle, 2000)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == incrSpeed:
            ballSpeed += 0.5
        if event.type == shrinkPaddle:
            paddleW -= 5  # decreasing paddle width
            paddle.width = paddleW

    screen.fill(bg)
    
    for block in block_list:
        block.draw(screen)
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    # Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision blocks
    hitIndex = ball.collidelist([block.rect for block in block_list])

    if hitIndex != -1:
        block = block_list[hitIndex]
        if block.unbreakable:
            dx, dy = detect_collision(dx, dy, ball, block.rect)
        else:
            dx, dy = detect_collision(dx, dy, ball, block.rect)
            if block.hit():
                block_list.pop(hitIndex)
                game_score += 1
                collision_sound.play()

    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
        
    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)