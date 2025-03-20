import pygame # Impordime pygame raamatukogu
pygame.init() # Alustame pygame funktsioonid.
screen=pygame.display.set_mode([640,480]) # Määrame pygame akna laiuseks 640 x 480 pixlit.
pygame.display.set_caption("Ülessanne 2 - Robin Roosmaa") # Määrame pygame pealkirjaks "Ülessanne 2 - Robin Roosmaa".
white = (255, 255, 255) # Määrame vajaliku värvi väärtuse.
pood = pygame.image.load("bg_shop.png") # Tausta laadimine png failist.
screen.blit(pood,[0,0]) # Tausta printimine ekraanile
muua = pygame.image.load("seller.png") # Müüa laadimine png failist.
muua = pygame.transform.scale(muua, [260, 305]) # Müüa suuruse muutmine sobivaks.
screen.blit(muua, [103,159]) # Müüa printimine ekraanile.
mull = pygame.image.load("chat.png") # Jutumulli laadimine png failist.
mull = pygame.transform.scale(mull, [258, 200]) # Jutumulli skaala muutmine.
screen.blit(mull, [245, 68]) # jutumulli printimine ekraanile.
font = pygame.font.Font(pygame.font.match_font('Times New Roman'), 22) # Teksti fondi ja suuruse määramine.
text = font.render("Tere, olen Robin Roosmaa", True, white) # Teksti väärtuste määramine.
screen.blit(text, [255,140]) # Teksti printimine ekraanile.
#Lihtne loop ekraani käimas hoidmiseks, et see sulgeks alles siis kui rististi vajutatakse.
jooksmas = True
while jooksmas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jooksmas = False
    pygame.display.flip()
pygame.quit()