import pygame
import GUI

# Initialize character variables outside the function
x = 50
y = 50
width = 40
height = 60
velocity = 5

player_can_move = False

def create_character(window_surface, window_width, window_height):
    global x, y  # Declare x and y as global to modify them

    keys = pygame.key.get_pressed()

    if player_can_move:
        if keys[pygame.K_LEFT] and x > 0:
            x -= velocity
        if keys[pygame.K_RIGHT] and x + width < window_width:
            x += velocity
        if keys[pygame.K_UP] and y > 0:
            y -= velocity
        if keys[pygame.K_DOWN] and y + height < window_height:
            y += velocity

    # Draw the character
    pygame.draw.rect(window_surface, (255, 0, 0), (x, y, width, height))