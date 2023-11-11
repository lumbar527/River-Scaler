import pygame
import random
import time

class RiverScaler():
    def __init__(self, images, sounds):
        self.images = images
        self.sounds = sounds
    def title_screen(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        while running:
            pygame.display.set_caption('River Scaler')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.blit(self.images[2], (0,0))
            pygame.display.flip()
            dt = clock.tick(60) / 1000
            screen.fill((0, 0, 0))
        pygame.quit()
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        dt = 0

        while running:
            pygame.display.set_caption('River Scaler')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == None:
                    ...
                pygame_events = pygame.key.get_pressed()
                if pygame_events[pygame.K_UP]:
                    ...
                elif pygame_events[pygame.K_DOWN]:
                    ...
                elif pygame_events[pygame.K_LEFT]:
                    ...
                elif pygame_events[pygame.K_RIGHT]:
                    ...

            pygame.display.flip()

            dt = clock.tick(60) / 1000

            screen.fill((0, 0, 0))

        pygame.quit()