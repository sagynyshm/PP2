import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    painting = False
    eraser_mode = False
    current_color = (255, 0, 0)  # Default color: red
    shapes = []  # List to store drawn shapes
    
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
                    shapes.clear()
                
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # left click stops painting
                    painting = False
                    if mode == 'rectangle':
                        drawRectangle(screen, points, current_color, eraser_mode, shapes)
                        points.clear()  # Clear points after drawing rectangle
                    elif mode == 'circle':
                        drawCircle(screen, points, current_color, eraser_mode, shapes)
                        points.clear()  # Clear points after drawing circle
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_q:  # Change mode to draw rectangles
                    mode = 'rectangle'
                if event.key == pygame.K_c:  # Change mode to draw circles
                    mode = 'circle'
                if event.key == pygame.K_e:  # Toggle eraser mode
                    eraser_mode = not eraser_mode
                if event.key == pygame.K_w:
                    current_color = (255, 255, 255)
                if event.key == pygame.K_r:  # Select red color
                    current_color = (255, 0, 0)
                if event.key == pygame.K_g:  # Select green color
                    current_color = (0, 255, 0)
                if event.key == pygame.K_b:  # Select blue color
                    current_color = (0, 0, 255)
                if event.key == pygame.K_PLUS and pressed[pygame.K_DOWN]:
                    radius = min(200, radius + 1)
                elif event.key == pygame.K_MINUS and pressed[pygame.K_DOWN]:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION and painting:
                position = event.pos
                points.append(position)
        
        screen.fill((0, 0, 0))
        for shape in shapes:  # Draw existing shapes
            if shape[0] == 'rectangle':
                drawRectangle(screen, shape[1], shape[2], shape[3], [])
            elif shape[0] == 'circle':
                drawCircle(screen, shape[1], shape[2], shape[3], [])
        
        if mode == 'rectangle':
            drawRectangle(screen, points, current_color, eraser_mode, [])
        elif mode == 'circle':
            drawCircle(screen, points, current_color, eraser_mode, [])
        else:
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, current_color, eraser_mode)
                i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color, eraser_mode):
    if eraser_mode:
        color = (0, 0, 0)  # Use black color to erase
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, points, color, eraser_mode, shapes):
    if len(points) > 1:
        if eraser_mode:
            color = (0, 0, 0)  # Use black color to erase
        pygame.draw.rect(screen, color, pygame.Rect(points[0], (points[-1][0] - points[0][0], points[-1][1] - points[0][1])), 3)
        if not eraser_mode:
            shapes.append(('rectangle', points.copy(), color, False))

def drawCircle(screen, points, color, eraser_mode, shapes):
    if len(points) > 1:
        if eraser_mode:
            color = (0, 0, 0)  # Use black color to erase
        radius = max(1, abs(points[-1][0] - points[0][0]))
        pygame.draw.circle(screen, color, points[0], radius, 3)
        if not eraser_mode:
            shapes.append(('circle', points.copy(), color, False))

main()