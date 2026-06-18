import pygame 

pygame.init()

WIDTH, HEIGHT = 280, 280
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Digit Recognizer")

is_running = True 

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    screen.fill((0,0,0))
    pygame.display.flip()

pygame.quit()