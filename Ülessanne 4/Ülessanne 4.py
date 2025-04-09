import pygame # Impordime pygame raamatukogu
import random # Impordime random raamatukogu
pygame.init() # Alustame pygame funktsioonid.

screen = pygame.display.set_mode([640,480]) # Määrame pygame akna mõõtmed.
pygame.display.set_caption("Rally") # Määrame pygame akna pealkirja.

white = (255, 255, 255) # Määrame vajaliku värvi väärtuse.

taust = pygame.image.load("bg_rally.jpg") # Tausta laadimine png failist.
screen.blit(taust, [0, 0]) # Tausta printimine ekraanile.
f1_blue = pygame.image.load("f1_blue.png") # Sinise auto laadimine png failist.
f1_red = pygame.image.load("f1_red.png") # Punase auto laadimine png failist.

font = pygame.font.Font(pygame.font.match_font('Times New Roman'), 30) # Teksti fondi ja suuruse määramine.
punktid = 0 # Algse punktisumma määramine.
score = font.render(str(punktid), True, white) # Algse punktiskoori määramine
screen.blit(score, [50,100]) # Skoori printimine ekraanile.

f1_red_x, f1_red_y = 300, 360 # Punase auto x ja y kordinaat.
f1_blue1_x, f1_blue1_y = 150, -100 # Esimese sinise auto x ja y kordinaat.
f1_blue2_x, f1_blue2_y = 395, -100 # Teise sinise auto x ja y kordinaat.
f1_blue1_kiirus = 5 # Esimese auto algne kiirus
f1_blue2_kiirus = 10 # Teise auto algne kiirus.
clock = pygame.time.Clock() # Mängu tick kiiruse määramiseks kella loomine

#While tsükkel ekraani püsivaks muutmiseks ja mängu sulgemiseks.
jooksmas = True
while jooksmas:
    clock.tick(60) # Tick kiiruse määramine.
    #Mängu sulgemine risti vajutusel.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jooksmas = False
    # Siniste autode ekraani põhja jõudmisel liiguvad need tagasi üles, muudavad suvaliselt oma positsiooni ja liikumis kiirust ning lisavad punkti skoori.
    if f1_blue1_y > 480:
        f1_blue1_y = -100
        punktid += 1
        f1_blue1_x = random.randint(150, 205)
        f1_blue1_kiirus = random.randint(5, 10)
    if f1_blue2_y > 480:
        f1_blue2_y = -100
        punktid += 1
        f1_blue2_x = random.randint(395, 450)
        f1_blue2_kiirus = random.randint(5, 10)
    # Uuendame mängu komponente iga ticki korral.
    screen.blit(f1_red, (f1_red_x, f1_red_y))
    screen.blit(f1_blue, (f1_blue1_x, f1_blue1_y))
    screen.blit(f1_blue, (f1_blue2_x, f1_blue2_y))
    f1_blue1_y += f1_blue1_kiirus
    f1_blue2_y += f1_blue2_kiirus
    pygame.display.flip()
    screen.blit(taust, [0, 0])
    # Uuendame skoori nii muutujas kui ekraanil.
    score = font.render(str(punktid), True, white)
    screen.blit(score, [50, 100])
pygame.quit()