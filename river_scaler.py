import pygame
import pygame_widgets
from pygame_widgets.button import Button
import objects

class RiverScaler():
    def __init__(self, images, sounds):
        self.images = images
        self.sounds = sounds
    def game_over(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running2 = True
        def click_play2():
            nonlocal running2
            running2 = False
        restart = Button(
        screen, 490, 385, 300, 150, text='Restart',
        fontSize=50, margin=20,
        inactiveColour=(255, 0, 0),
        pressedColour=(0, 0, 255), radius=20,
        onClick=click_play2
        )
        quit = Button(
        screen, 540, 570, 200, 100, text='Quit',
        fontSize=50, margin=20,
        inactiveColour=(255, 0, 0),
        pressedColour=(0, 0, 255), radius=20,
        onClick=self.end
        )

        while running2:
            restart.show()
            quit.show()
            pygame.display.set_caption('River Scaler')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running2 = False
            screen.blit(self.images[6], (0,0))
            pygame_widgets.update(pygame.event.get())
            pygame.display.flip()
            dt = clock.tick(60) / 1000
            screen.fill((0, 0, 0))
        restart.hide()
        quit.hide()
        self.title_screen()
    def title_screen(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        def click_play():
            nonlocal running
            running = False
        start = Button(
        screen, 800, 500, 300, 150, text='Play',
        fontSize=50, margin=20,
        inactiveColour=(0, 90, 152),
        pressedColour=(0, 0, 255), radius=20,
        onClick=click_play
        )
        while running:
            start.show()
            pygame.display.set_caption('River Scaler')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.blit(self.images[1], (0,0))
            pygame_widgets.update(pygame.event.get())
            pygame.display.flip()
            dt = clock.tick(60) / 1000
            screen.fill((0, 0, 0))
        start.hide()
        self.run()
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
                    up = True
                    up_timer = 10
                    down = False
                elif pygame_events[pygame.K_DOWN]:
                    down = True
                    up = False
                elif pygame_events[pygame.K_LEFT]:
                    left = True
                    right = False
                elif pygame_events[pygame.K_RIGHT]:
                    right = True
                    left = False

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
                oxygen -= 0.5
            else:
                if oxygen < 100:
                    oxygen += 0.1

            if oxygen < 0:
                running = False
            if health < 0:
                running = False

            pygame.draw.rect(screen, (200,200,200), (48, 48, 204, 44))
            pygame.draw.rect(screen, (255,0,0), (50, 50, health * 2, 40))

            pygame.draw.rect(screen, (200,200,200), (48, 98, 204, 44))
            pygame.draw.rect(screen, (0,0,255), (50, 100, oxygen * 2, 40))

            pygame.draw.rect(screen, (0,77,129), (0,545,1280,175))

            salmon = objects.Salmon(self.images[0], x, y, screen)

            pygame.display.flip()

            dt = clock.tick(60) / 1000

            screen.fill((255, 255, 255))

        if health < 0 or oxygen < 0:
            self.game_over()
    def end():
        # Intentionally empty.
        ...