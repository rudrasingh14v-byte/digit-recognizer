import pygame 

pygame.init()

WIDTH,HEIGHT = 280, 280

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Draw a digit!")

BLACK = (0,0,0)
WHITE = (255,255,255)

screen.fill(BLACK)

is_running = True
is_drawing = False

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        elif event.type == pygame.MOUSEBUTTONUP:
            is_drawing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            is_drawing = True
        
        elif event.type == pygame.MOUSEMOTION:
            if is_drawing:
                x_cursor, y_cursor = event.pos
                pygame.draw.circle(screen,WHITE,(x_cursor,y_cursor),6)
                pygame.display.flip()
pygame.quit()
        