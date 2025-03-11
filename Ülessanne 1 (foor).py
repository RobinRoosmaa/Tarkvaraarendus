import pygame # Impordime pygame raamatukogu
pygame.init() # Alustame pygame funktsioonid.
screen=pygame.display.set_mode([300,300]) # Määrame pygame akna laiuseks 300 x 300 pixlit.
pygame.display.set_caption("Foor - Robin Roosmaa") # Määrame pygame pealkirjaks "Foor - Robin Roosmaa".
grey = (125,125,125) # Määrame vajatud värvide väärtused.
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
# Foor
pygame.draw.polygon(screen, grey, ((100, 10), (200, 10), (200, 280), (100, 280)), 2) # Foori äär
pygame.draw.circle(screen, red, (150, 60), 40) # Punane tuli
pygame.draw.circle(screen, yellow, (150, 145), 40) # Kollane tuli
pygame.draw.circle(screen, green, (150, 230), 40) # Roheline tuli
#While tsükkel akna lahti hoidmiseks.
jooksmas = True
while jooksmas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jooksmas = False

    pygame.display.flip()

pygame.quit()