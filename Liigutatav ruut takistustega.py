import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ruudu mäng")

# Colors
green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)

# Square properties
square_size = 20
square_x = screen_width // 2 - square_size // 2
square_y = screen_height // 2 - square_size // 2
square_speed = 0.1
square_color = green

# Rectangle properties
rectangle_width = 30
rectangle_height = 15
rectangle_list = []

# Create 10 random rectangles
for _ in range(10):
    rectangle_x = random.randint(0, screen_width - rectangle_width)
    rectangle_y = random.randint(0, screen_height - rectangle_height)
    rectangle_list.append([rectangle_x, rectangle_y])

# Game loop
running = True
game_end_timer = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    if game_end_timer == 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            square_y -= square_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            square_y += square_speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            square_x -= square_speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            square_x += square_speed

    # Keep square within screen bounds
    square_x = max(0, min(square_x, screen_width - square_size))
    square_y = max(0, min(square_y, screen_height - square_size))

    # Check for collisions
    for rectangle in rectangle_list:
        rect_x, rect_y = rectangle
        if (
            square_x < rect_x + rectangle_width
            and square_x + square_size > rect_x
            and square_y < rect_y + rectangle_height
            and square_y + square_size > rect_y
        ):
            # Collision detected, turn square red
            square_color = red
            game_end_timer = pygame.time.get_ticks()

    # Draw everything
    screen.fill((255, 255, 255))  # White background
    pygame.draw.rect(
        screen, square_color, (square_x, square_y, square_size, square_size)
    )
    for rectangle in rectangle_list:
        rect_x, rect_y = rectangle
        pygame.draw.rect(
            screen, black, (rect_x, rect_y, rectangle_width, rectangle_height)
        )

    # Game end timer
    if game_end_timer > 0:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over!", True, black)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
        if pygame.time.get_ticks() - game_end_timer > 3:
            running = False
    pygame.display.flip()

# Quit Pygame
pygame.quit()