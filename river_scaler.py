import pygame
import pygame_widgets
from pygame_widgets.button import Button
import random
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
        waterfall_x = 1280
        waterfall_width = 400
        waterfall_height = 200
        speed = 2
        bear = objects.Bear(self.images[2],screen, waterfall_x-waterfall_width/2, waterfall_height-175, True)
        waterfall_increase = 0
        waterfall_increased = 0

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
                    oxygen += 0.3

            if oxygen < 0:
                running = False
            if health < 0:
                running = False

            # Bars
            pygame.draw.rect(screen, (200,200,200), (48, 48, 204, 44))
            pygame.draw.rect(screen, (255,0,0), (50, 50, health * 2, 40))
            pygame.draw.rect(screen, (200,200,200), (48, 98, 204, 44))
            pygame.draw.rect(screen, (0,0,255), (50, 100, oxygen * 2, 40))

            # River
            pygame.draw.rect(screen, (0,77,129), (0,545,1280,175))

            if waterfall_x < 0 - waterfall_width:
                waterfall_increase = random.randint(10,50)
                waterfall_increased += waterfall_increase
                if waterfall_height < 400:
                    waterfall_height += waterfall_increase
                waterfall_width = waterfall_width * random.randint(11, 14) / 10
                waterfall_x = 1280
                speed += (random.randint(0,1) / 10)

            waterfall = objects.Waterfall(screen, waterfall_x, 545-waterfall_height, waterfall_width, waterfall_height)
            waterfall_x -= speed

            salmon = objects.Salmon(self.images[0], x, y, screen)

            bear = objects.Bear(bear.image,screen, waterfall_x+waterfall_width/2, bear.rect.height-waterfall_increased-60, bear.go)

            pygame.display.flip()

            dt = clock.tick(60) / 1000

            screen.fill((255, 255, 255))

            me_waterfall = pygame.sprite.collide_mask(waterfall, salmon)
            if not me_waterfall == None:
                if x + 200 < waterfall_x + waterfall_width / 2:
                    x -= 1+speed
                    oxygen += 0.4
                    if oxygen > 100:
                        oxygen = 100
                else:
                    x += 1+speed
                    oxygen += 0.9
                    if oxygen > 100:
                        oxygen = 100
        if not event.type == pygame.QUIT:
            self.game_over()
    def end():
        # Intentionally empty function.
        ...