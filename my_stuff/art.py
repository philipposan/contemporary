import pygame
import random

# Initialize Pygame
pygame.init()

# Screen size
width, height = 800, 600

# Colors
white = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Art")

# Main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw random colored rectangles with a dark edge
    for _ in range(10):
        x = random.randint(0, width - 50)
        y = random.randint(0, height - 50)
        color = random.choice(colors)

        # Randomly choose between flat and 3D appearance
        if random.choice([True, False]):
            # Draw the filled rectangle with a slightly smaller size
            pygame.draw.rect(screen, color, pygame.Rect(x + 2, y + 2, 46, 46))
        else:
            # Draw a 3D box using lines
            pygame.draw.lines(screen, (0, 0, 0), True, [(x, y), (x + 50, y), (x + 50, y + 50), (x, y + 50)], 2)

        # Draw the border
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, 50, 50), 2)

    # Update the screen
    pygame.display.flip()

    # Short pause to make the animation visible
    pygame.time.delay(500)

# Quit Pygame
pygame.quit()
