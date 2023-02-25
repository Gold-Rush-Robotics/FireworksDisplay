import pygame
import math
import random

pygame.init()

# Set display surface and background color
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_color = (0, 0, 0)


# Define firework particle class
class Particle:
    def __init__(self, x, y, size, color, speed):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.angle = 0
        self.radius = 1

    def update(self):
        self.x += self.radius * self.speed * math.cos(self.angle)
        self.y += self.radius * self.speed * math.sin(self.angle)
        self.radius += 0.05
        self.color = (self.color[0], self.color[1], self.color[2])

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 
self.size)


# Define function to create a firework explosion
def explode(x, y, color):
    particles = []
    particle_count = 100
    for i in range(particle_count):
        size = random.randint(2, 5)
        speed = random.randint(1, 10)
        particle = Particle(x, y, size, color, speed)
        particle.angle = random.uniform(0, 2 * math.pi)
        particles.append(particle)
    return particles


# Create initial fireworks
fireworks = []
while len(fireworks) < 5:
    x = random.randint(100, WIDTH - 100)
    y = random.randint(100, HEIGHT - 100)
    size = random.randint(10, 20)
    color = [int(random.randint(0, 255)), int(random.randint(0, 255)), 
int(random.randint(0, 255))]
    speed = random.uniform(0.1, 1)
    firework = Particle(x, y, size, color, speed)
    fireworks.append(firework)

# Define main game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)

    # Draw fireworks
    for firework in fireworks:
        firework.draw()
        firework.update()
        if firework.color[2] <= 0:
            fireworks.remove(firework)
            particles = explode(firework.x, firework.y, firework.color)
            for particle in particles:
                fireworks.append(particle)

    pygame.display.flip()

pygame.quit()

