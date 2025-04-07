import pygame  # Import pygame module

# Initial setup
pygame.init()  # Initialize pygame
WIDTH, HEIGHT = 640, 480  # Screen size
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create game window
pygame.display.set_caption("Ping-Pong Game")  # Set game window title
clock = pygame.time.Clock()  # Create a clock for controlling game frame rate

# Music and sound effects
pygame.mixer.music.load('Background.mp3') # Background music.
pygame.mixer.music.play(-1) # Play music on loop.
pygame.mixer.music.set_volume(0.3) # Set music volume.
Bounce = pygame.mixer.Sound('Bounce.mp3') # Bounce sound effect.
Bounce.set_volume(0.3)

# Load image files
ball_img = pygame.image.load("ball.png")  # Ball image
pad_img = pygame.image.load("pad.png")  # Pad image

# Ball properties
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)  # Create a rectangle object for the ball
ball_speed_x = 4  # Set the ball's horizontal direction
ball_speed_y = -3  # Set the ball's vertical direction

# Pad properties
pad = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 1.5, 120, 20)  # Create a rectangle object for the pad
pad_img = pygame.transform.scale(pad_img, [120, 20])  # Resizes the pad image
pad_speed = 5  # Determines the pad's movement speed
pad_direction = 0  # Pad's movement direction (0 for stationary, 1 for right, -1 for left)

# Score
score = 0  # Score starting value
font = pygame.font.Font(None, 36)  # Create a font object for displaying the score

# Game loop
running = True  # Game loop variable True (means the game is running)
while running:
    screen.fill((150, 200, 255))  # Lighter background (RGB values)

    for event in pygame.event.get():  # Goes through all Pygame events
        if event.type == pygame.QUIT:  # If the user closes the window
            running = False  # Ends the loop

        # Control the pad movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                pad_direction = 1
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                pad_direction = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_a:
                pad_direction = 0

    # Ball movement
    ball.x += ball_speed_x  # Moves the ball horizontally
    ball.y += ball_speed_y  # Moves the ball vertically

    # Ball bouncing off walls
    if ball.left <= 0 or ball.right >= WIDTH:  # If the ball hits the left or right edge
        ball_speed_x = -ball_speed_x  # Flips the ball's horizontal direction
    if ball.top <= 0:  # If the ball hits the top edge
        ball_speed_y = -ball_speed_y  # Flips the ball's vertical direction

    # Ball and pad collision
    if ball.colliderect(pad) and ball_speed_y > 0:  # If the ball hits the pad and is moving down
        ball_speed_y = -ball_speed_y  # Flips the ball's vertical direction
        Bounce.play() # Play the bounce sound effect
        score += 1  # Increases the score

    # Game over condition
    if ball.bottom >= HEIGHT:  # If the ball falls below the screen
        running = False

    # Pad movement
    pad.x += pad_speed * pad_direction  # Moves the pad in the given direction
    if pad.left <= 0:  # If the pad hits the left edge
        pad.x = 0  # Keeps the pad within the screen
    elif pad.right >= WIDTH:  # If the pad hits the right edge
        pad.x = WIDTH - pad.width  # Keeps the pad within the screen

    # Drawing
    screen.blit(ball_img, (ball.x, ball.y))  # Draws the ball on the screen
    screen.blit(pad_img, (pad.x, pad.y))  # Draws the pad on the screen

    # Display the score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))  # Creates the score text
    screen.blit(score_text, (10, 10))  # Displays the score on the screen

    pygame.display.flip()  # Updates the screen
    clock.tick(60)  # Sets the frame rate to 60 frames per second

pygame.quit()  # Ends pygame