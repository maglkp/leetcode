import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CIRCLE_RADIUS = 20
NUM_CIRCLES = 5
BOUNDARY_PADDING = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Circle class
class Circle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed_x = random.choice([-5, 15])
        self.speed_y = random.choice([-5, 15])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off the walls
        if self.x <= BOUNDARY_PADDING or self.x >= WIDTH - BOUNDARY_PADDING:
            self.speed_x = -self.speed_x
        if self.y <= BOUNDARY_PADDING or self.y >= HEIGHT - BOUNDARY_PADDING:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), CIRCLE_RADIUS)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Circles")

# Create circles
circles = [Circle(random.randint(CIRCLE_RADIUS + BOUNDARY_PADDING, WIDTH - CIRCLE_RADIUS - BOUNDARY_PADDING),
                  random.randint(CIRCLE_RADIUS + BOUNDARY_PADDING, HEIGHT - CIRCLE_RADIUS - BOUNDARY_PADDING),
                  RED) for _ in range(NUM_CIRCLES)]

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move and draw circles
    for circle in circles:
        circle.move()
        circle.draw()

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)

    # Clear the screen
    screen.fill(BLACK)
