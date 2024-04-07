import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    painting = False
    
    while True:
        pressed = pygame.key.get_pressed()        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click starts painting
                    painting = True
                elif event.button == 3:  # right click clears canvas
                    points.clear()
                
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # left click stops painting
                    painting = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_q:  # Change mode to draw rectangles
                    mode = 'rectangle'
                if event.key == pygame.K_c:  # Change mode to draw circles
                    mode = 'circle'
                if event.key == pygame.K_PLUS and pressed[pygame.K_DOWN]:
                    radius = min(200, radius + 1)
                elif event.key == pygame.K_MINUS and pressed[pygame.K_DOWN]:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION and painting:
                position = event.pos
                points.append(position)
        
        screen.fill((0, 0, 0))
        if mode == 'rectangle':
            drawRectangle(screen, points)
        elif mode == 'circle':
            drawCircle(screen, points)
        else:
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, points):
    if len(points) > 1:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(points[0], (points[-1][0] - points[0][0], points[-1][1] - points[0][1])), 3)

def drawCircle(screen, points):
    if len(points) > 1:
        radius = max(1, abs(points[-1][0] - points[0][0]))
        pygame.draw.circle(screen, (255, 255, 255), points[0], radius, 3)

main()