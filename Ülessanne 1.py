import pygame
pygame.init()
screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumemees - Robin Roosmaa")
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
pygame.draw.circle(screen, white, (150, 75), 30)  # Head
pygame.draw.circle(screen, white, (150, 140), 40) # Midsection
pygame.draw.circle(screen, white, (150, 225), 50) # Base

# Draw facial features
pygame.draw.circle(screen, black, (140, 70), 5)  # Left eye
pygame.draw.circle(screen, black, (160, 70,), 5)  # Right eye
pygame.draw.polygon(screen, red, ((145, 80), (155, 80), (150, 95)))

# Game loop (to keep the window open)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()