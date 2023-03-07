import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)


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
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 
3)


# Define the explosion class
class Explosion:
    def __init__(self, x, y):
        self.particles = []
        for i in range(100):
            color = random.choice([RED, GREEN, BLUE, YELLOW, PURPLE, 
CYAN])
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
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the window
    size = (800, 600)
    screen = pygame.display.set_mode(size)

    # Set the caption of the window
    pygame.display.set_caption("Celebratory Fireworks")

    # Set up the clock
    clock = pygame.time.Clock()

    # Set up the list of explosions
    explosions = []
    dvd_image = pygame.image.load("dvd-removebg-preview.png")
    dvd_image.convert()
    dvdrect = dvd_image.get_rect()
    # Set up the dvd's initial position and movement
    dvd_x = 800 // 2
    dvd_y = 600 // 2
    dvd_speed = 5
    dvd_directiony = "up"
    dvd_directionx = "right"

    # Set up the game loop
    done = False
    while not done:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # Move the dvd
        if dvd_directiony == "up":
            dvd_y -= dvd_speed
            if dvd_y <= 0:
                dvd_directiony = "down"
        elif dvd_directiony == "down":
            dvd_y += dvd_speed
            if dvd_y >= 500:
                dvd_directiony = "up"
        if dvd_directionx == "left":
            dvd_x -= dvd_speed
            if dvd_x <= 0:
                dvd_directionx = "right"
        elif dvd_directionx == "right":
            dvd_x += dvd_speed
            if dvd_x >= 500:
                dvd_directionx = "left"

        screen.fill(BLACK)    
        screen.blit(dvd_image, (dvd_x, dvd_y))
        clock.tick(60)
        pygame.display.update()
        
        

        if(dvd_x == 0 & dvd_y == 0) | (dvd_x == 500 & dvd_y == 0) | (dvd_x == 0 & dvd_y == 500) | (dvd_x == 500 & dvd_y == 500):
            screen.fill(BLACK)
            for i in range(0,100):    
                
                # Create a new explosion
                if random.random() < 0.02:
                    explosions.append(Explosion(random.randint(0, 800), 
        random.randint(0, 600)))

                # Update the explosions
                for explosion in explosions:
                    explosion.update()

                # Draw the background
                screen.fill(BLACK)

                # Draw the explosions
                for explosion in explosions:
                    explosion.draw(screen)

                # Update the screen
                pygame.display.flip()

                # Tick the clock
                clock.tick(60)

    # Quit Pygame
    pygame.quit()


# Call the main function
if __name__ == "__main__":
    main()
