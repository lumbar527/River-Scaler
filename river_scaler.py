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
            screen.blit(self.images[1], (0,0))
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
        health = 100
        oxygen = 100
        x = 540
        y = 500
        up = False
        down = False
        left = False
        right = False
        up_timer = 10

        while running:
            pygame.display.set_caption('River Scaler')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == None:
                    ...
                pygame_events = pygame.key.get_pressed()
                if pygame_events[pygame.K_UP]:
                    # y -= 30
                    up = True
                    up_timer = 10
                    down = False
                    # left = False
                    # right = False
                elif pygame_events[pygame.K_DOWN]:
                    # y += 10
                    down = True
                    up = False
                    # left = False
                    # right = False
                elif pygame_events[pygame.K_LEFT]:
                    left = True
                    # down = False
                    # up = False
                    right = False
                elif pygame_events[pygame.K_RIGHT]:
                    right = True
                    # down = False
                    left = False
                    # up = False

            if up:
                if up_timer > 0:
                    y -= 15
                up_timer -= 1
            if down:
                y += 2
            if left:
                x -= 1
            if right:
                x += 1

            if y < 500:
                y += 5

            pygame.draw.rect(screen, (200,200,200), (48, 48, 204, 44))
            pygame.draw.rect(screen, (255,0,0), (50, 50, health * 2, 40))

            pygame.draw.rect(screen, (200,200,200), (48, 98, 204, 44))
            pygame.draw.rect(screen, (0,0,255), (50, 100, oxygen * 2, 40))

            pygame.draw.rect(screen, (0,77,129), (0,545,1280,175))

            screen.blit(self.images[0], (x, y))

            pygame.display.flip()

            dt = clock.tick(60) / 1000

            screen.fill((255, 255, 255))

        pygame.quit()