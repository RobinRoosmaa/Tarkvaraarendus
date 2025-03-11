import pygame # Impordime pygame raamatukogu
pygame.init() # Alustame pygame funktsioonid.
screen=pygame.display.set_mode([300,300]) # Määrame pygame akna laiuseks 300 x 300 pixlit.
pygame.display.set_caption("Lumemees - Robin Roosmaa") # Määrame pygame pealkirjaks "Lumemees - Robin Roosmaa".
white = (255, 255, 255) # Määrame vajatud värvide väärtused.
black = (0, 0, 0)
red = (255, 0, 0)
pygame.draw.circle(screen, white, (150, 75), 30)  # Lumememme ülemine pall
pygame.draw.circle(screen, white, (150, 140), 40) # Lumememme keskmine pall
pygame.draw.circle(screen, white, (150, 225), 50) # Lumememme alumine pall
pygame.draw.circle(screen, black, (140, 70), 5)  # Vasak silm
pygame.draw.circle(screen, black, (160, 70,), 5)  # Parem silm
pygame.draw.polygon(screen, red, ((145, 80), (155, 80), (150, 95))) # Nina
#While tsükkel akna lahti hoidmiseks.
jooksmas = True
while jooksmas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jooksmas = False

    pygame.display.flip()

pygame.quit()