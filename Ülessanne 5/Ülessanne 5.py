import pygame # Impordib pygame mooduli
import random   # Impordib random mooduli juhuslikkuse jaoks

# Algseadistused
pygame.init() #käivitab pygame
WIDTH, HEIGHT = 640, 480 #ekraani suurus
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Loob mängu akna
pygame.display.set_caption("Ping-Pong Mäng") # Seab mänguakna pealkirja
clock = pygame.time.Clock() # Loob kella mängu kaadrisageduse juhtimiseks.

# Lae piltide failid
ball_img = pygame.image.load("ball.png") #Palli pilt
pad_img = pygame.image.load("pad.png") #Aluse pilt

# Palli omadused
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20) #Loob ristküliku objekti palli jaoks
ball_speed_x = 4 * random.choice((1, -1)) #Seab palli horisontaalse kiiruse juhuslikus suunas
ball_speed_y = 4 * random.choice((1, -1)) #Seab palli vertikaalse kiiruse juhuslikus suunas

# Aluse omadused
pad = pygame.Rect(WIDTH // 2-60, HEIGHT // 1.5, 120, 20) #Loob ristküliku objekti aluse jaoks
pad_img = pygame.transform.scale(pad_img, [120, 20]) # Muudab aluse pildi suurust
pad_speed = 3 # Määrab aluse liikumise kiiruse
direction = 1 # Aluse liikumise suund

# Punktid
score = 0 # Skoori algväärtus
defeat = 0 # Kaotuse algväärtus
font = pygame.font.Font(None, 36) # Loob kirjatüübiga objekti skoori kuvamiseks

# Mängu tsükkel
running = True # Mängu tsükli muutuja True (tähendab, et mäng käib
while running:
    screen.fill((149, 203, 255))  # Heledam taust (RGB väärtused)

    for event in pygame.event.get(): # Käib läbi kõik Pygame sündmused
        if event.type == pygame.QUIT: # Kui kasutaja sulgeb akna
            running = False # Lõpetab tsükli

    # Palli liikumine
    ball.x += ball_speed_x # Liigutab palli horisontaalselt
    ball.y += ball_speed_y # Liigutab palli vertikaalselt

    # Palli põrkumine seintelt
    if ball.left <= 0 or ball.right >= WIDTH: # Kui pall puudutab vasakut või paremat serva
        ball_speed_x = -ball_speed_x # Muudab ppalli horistontaalset suunda
    if ball.top <= 0: # Kui pall puudutab ülemist serva
        ball_speed_y = -ball_speed_y # Muudab palli vertikaalset suunda

    # Palli ja aluse kokkupõrge
    if ball.colliderect(pad) and ball_speed_y > 0: #Kui pall põrkab vastu alust ja liigub alla
        ball_speed_y = -ball_speed_y #Muudab palli vertikaalset suunda
        score += 1 # Suurendab skoori

    # Kui pall puudutab alumist äärt
    if ball.bottom >= HEIGHT: #Kui pall langeb ekraani alla
        defeat += 1 # Suurendab kaotuste arvu
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2 #Taastab palli algpositsiooni
        ball_speed_x *= random.choice((1, -1)) #Muudab palli horistonaalsuunalist liikumist juhuslikult
        ball_speed_y *= random.choice((1, -1)) # Muudab palli vertikaalsuunalist liikumist juhuslikult

        # Aluse liikumine
    pad.x += pad_speed * direction # Liigutab alust etteantud suunas
    if pad.left <= 0: # Kui alus puudutab vasakut serva
        pad.x = 0 # Hoiab alust ekraani piires
        direction = 1 # Muudab suunda paremale
    elif pad.right >= WIDTH: # Kui alus puudutab paremat serva
        pad.x = WIDTH - pad.width # Hoiab alust ekraani piires
        direction = -1 # Muudab suunda vasakule

    # Joonistamine
    screen.blit(ball_img, (ball.x, ball.y)) # Joonistab palli ekraanile
    screen.blit(pad_img, (pad.x, pad.y)) # Joonistab aluse ekraanile

    # Kuvame skoori
    score_text = font.render(f"Skoor: {score}  Kaotused: {defeat}", True, (0, 0, 0)) #Loob skoori teksti
    screen.blit(score_text, (10, 10)) # Kuvab skoori ekraanil

    pygame.display.flip() # Uuendab ekraani
    clock.tick(60) # Seab kaadrisageduse 60 kaadrit sekundis

pygame.quit() # lõpetab pygame

#updated 08:56