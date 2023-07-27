import pygame
import random
import sys
import math

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

class Dot:
    def __init__(self,colorless = False):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)
        self.radius = random.randint(3, 6)
        if colorless:
            self.color = WHITE
        else:
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x < 0 or self.x > SCREEN_WIDTH:
            self.speed_x *= -1
        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def find_closest_dots(mouse_pos, dots, radius):
    closest_dots = []
    for dot in dots:
        distance = math.sqrt((dot.x - mouse_pos[0]) ** 2 + (dot.y - mouse_pos[1]) ** 2)
        if distance <= radius:
            closest_dots.append(dot)
    return closest_dots

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Random Moving Dots")
    clock = pygame.time.Clock()

    dots = [Dot() for _ in range(100)]
            
    control_line = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                control_line = not control_line
                mouse_pos = pygame.mouse.get_pos()
                closest_dots = find_closest_dots(mouse_pos, dots, 100)
                for dot in closest_dots:
                    pygame.draw.line(screen, WHITE, mouse_pos, (int(dot.x), int(dot.y)))

        screen.fill((0, 0, 0))
        mouse_pos = pygame.mouse.get_pos()

        for dot in dots:
            dot.move()
            dot.draw(screen)
            if control_line:
                closest_dots = find_closest_dots(mouse_pos, dots, 250)
                for dot in closest_dots:
                    distance = math.sqrt((dot.x - mouse_pos[0]) ** 2 + (dot.y - mouse_pos[1]) ** 2)
                    max_distance = 200.0  # Maximum distance for full line thickness
                    line_thickness = max(1, int(6 * (1 - distance / max_distance)))
                    pygame.draw.line(screen, dot.color, mouse_pos, (int(dot.x), int(dot.y)), line_thickness)

        pygame.display.flip()
        clock.tick(50)

main()
