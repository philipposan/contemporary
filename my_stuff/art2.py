import pygame
import random

# Initialize Pygame
pygame.init()

# Screen size
width, height = 800, 600

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Interactive Abstract Art")

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to draw an abstract shape
def draw_abstract_shape(surface, color, vertices):
    if len(vertices) > 2:  # Ensure there are more than 2 points to draw a polygon
        pygame.draw.polygon(surface, color, vertices)

# Main program loop
running = True
drawing = False
current_shape = []
shapes = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            drawing = True
            current_shape = [event.pos]
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            shapes.append((random_color(), current_shape))
            current_shape = []
        elif event.type == pygame.MOUSEMOTION and drawing:
            current_shape.append(event.pos)

    # Draw a gradient background
    gradient_color = random_color()
    pygame.draw.rect(screen, gradient_color, (0, 0, width, height))

    # Draw existing abstract shapes
    for color, vertices in shapes:
        draw_abstract_shape(screen, color, vertices)

    # Draw the current abstract shape being drawn
    if current_shape:
        draw_abstract_shape(screen, random_color(), current_shape)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
