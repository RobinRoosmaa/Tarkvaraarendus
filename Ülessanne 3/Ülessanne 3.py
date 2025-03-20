import pygame # Impordime pygame raamatukogu
pygame.init() # Alustame pygame funktsioonid
ekraan = pygame.display.set_mode([640, 480]) # Määrame pygame akna mõõtmed.
pygame.display.set_caption("Ruudustik - Robin Roosmaa") # Määrame pygame akna pealkirja.
ekraan.fill([153, 255, 153]) # Täidame ekraani tausta helerohelise värviga.

def ruudustik(kuva, ekraani_suurus, ruudu_moodud, ruudustiku_varv): # Loome funktsiooni, mis küsib pygaqme display-d, millele ruudustikku joonistada, selle ruudustiku üksiku ruudu mõõtmeid ja ruudsutiku värvi.
    x = 0 # Joonistatava ruudu x positsioon.
    y = 0 # Joonistatava ruudu y positsioon.
    ruudu_laius = ruudu_moodud[0] # Ruudustiku ruudu laius.
    ruudu_korgus = ruudu_moodud[1] # Ruudustiku ruudu kõrgus.
    while ekraani_suurus[1] > y: # Tsükkel jookseb kuni joonistamis positsioon on allpool display kõrgust.
        pygame.draw.rect(kuva, ruudustiku_varv, [x, y, ruudu_laius, ruudu_korgus], 1) # Joonistab ruudu saadud andmetega.
        if ekraani_suurus[0] > x: # Kordame ainult järgnevat kuni joonistamis positsioon jõuab display parema ääreni.
            x += ruudu_laius # Liigutame joonistamis positsiooni edasi ruudu laiuse võrra.
        else: # Ääreni jõudmisel teeme järgnevat.
            y += ruudu_korgus # Liigume järgmisele reale ruudu kõrguse põhjal.
            x = 0 # Liigume rea algusesse, ehk display vasakule äärele.

# Ruudustiku muutujad
varv = (255, 0, 0)
ruudu_mootmed = [20, 20]

ruudustik(ekraan, [640, 480], ruudu_mootmed, varv)

#While tsükkel akna lahti hoidmiseks.
jooksmas = True
while jooksmas:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jooksmas = False
    pygame.display.flip()
pygame.quit()