import pygame
import sys


pygame.init()


WINDOW_SIZE = (500, 500)
BACKGROUND_COLOR = (58, 58, 58)
IMAGE_SIZE = (300, 300)
CAPTION = "My first game screen"


screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(CAPTION)


image = pygame.image.load("cherry.jfif")  
image = pygame.transform.scale(image, IMAGE_SIZE)


image_rect = image.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    screen.fill(BACKGROUND_COLOR)

    
    screen.blit(image, image_rect)

    
    pygame.display.flip()
