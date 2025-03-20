import pygame # Impordime pygame raamatukogu
pygame.init() # Alustame pygame funktsioonid.
screen=pygame.display.set_mode([640,480]) # Määrame pygame akna laiuseks 640 x 480 pixlit.
pygame.display.set_caption("Ülessanne 2 - Robin Roosmaa") # Määrame pygame pealkirjaks "Ülessanne 2 - Robin Roosmaa".
white = (255, 255, 255) # Määrame vajaliku värvi väärtuse.
pood = pygame.image.load("bg_shop.png")
screen.blit(pood,[0,0])
muua = pygame.image.load("seller.png")
muua = pygame.transform.scale(muua, [260, 305])
screen.blit(muua, [103,159])
mull = pygame.image.load("chat.png")
mull = pygame.transform.scale(mull, [258, 200])
screen.blit(mull, [245, 68])
font = pygame.font.Font(pygame.font.match_font('Times New Roman'), 22)
text = font.render("Tere, olen Robin Roosmaa", True, white)
screen.blit(text, [255,140])
jooksmas = True
while jooksmas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jooksmas = False
    pygame.display.flip()
pygame.quit()