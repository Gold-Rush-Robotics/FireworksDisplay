import pygame
import random
import math
import sys
import time
from pygame import mixer

# Define some colors
CLTGREEN = (0, 80, 53)
NINERGOLD = (164, 150, 101)
WHITE = (255, 255, 255)
JASPER = (241, 230, 178)
PINEGREEN = (137, 144, 100)
CLAYRED = (128, 47, 45)
SKYBLUE = (0, 115, 119)
OREBLACK = (16, 24, 32)
BLACK = (0, 0, 0)


def end_game():
    pygame.quit()
    sys.exit()


start_time = round(time.time())
stop_after = start_time + 5  # 5 seconds

# GRR logo
GRR_png = pygame.image.load("fireworkDisplay.png")
img_size = GRR_png.get_rect().size

# Define the particle class
class Particle:
    def __init__(self, x, y, color, angle):
        self.x = x
        self.y = y
        self.color = color
        self.angle = angle
        self.speed = random.randint(1, 5)

    def update(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))
        self.speed -= 0.1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)


# Define the explosion class
class Explosion:
    def __init__(self, x, y):
        self.particles = []
        for i in range(100):
            color = random.choice([WHITE, JASPER, PINEGREEN, CLAYRED, SKYBLUE, OREBLACK])
            angle = random.randint(0, 360)
            self.particles.append(Particle(x, y, color, angle))

    def update(self):
        for particle in self.particles:
            particle.update()

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)


# Define the main function
def main():

    pygame.init()

    info_object = pygame.display.Info()
    width = info_object.current_w
    height = info_object.current_h

    global alpha
    alpha = 255

    x_speed = 18
    y_speed = 14
    x = random.randint(1, 1)
    y = random.randint(1, 1)



    # Initialize Pygame
    mixer.init()
    mixer.music.load("fireworkDisplay.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play()

    # Set the dimensions of the window
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # alpha of logo
    GRR_png.set_alpha(alpha)

    # Set the caption of the window
    pygame.display.set_caption("Celebratory Fireworks")

    # Set up the clock
    clock = pygame.time.Clock()

    # Set up the list of explosions
    explosions = []

    # Set up the game loop
    done = False
    while not done:
        # Handle events

        current_time = round(time.time())
        if current_time >= stop_after:
            end_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Create a new explosion
        if random.random() < 0.25:   # frequency of fireworks
            explosions.append(Explosion(random.randint(0, width), random.randint(0, height)))

        # Update the explosions
        for explosion in explosions:
            explosion.update()

        # Draw the background
        screen.fill(BLACK)

        # Draw the explosions
        for explosion in explosions:
            explosion.draw(screen)

        # Update the screen

        if (x + img_size[0] >= width) or (x <= 0):
            x_speed = -x_speed
        if (y + img_size[1] >= height) or (y <= 0):
            y_speed = -y_speed
        x += x_speed
        y += y_speed

        GRR_png.set_alpha(alpha)
        screen.blit(GRR_png, (x, y))
        # decrease opacity
        alpha -= 1

        pygame.display.flip()

        # Tick the clock
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


# Call the main function
if __name__ == "__main__":
    main()
