import pygame
import pygame_widgets
from pygame_widgets.button import Button
import random
import objects

class RiverScaler():
    def __init__(self, images, sounds):
        self.images = images
        self.sounds = sounds
    def game_over(self, score):
        pygame.init()
        pygame.font.init()
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
            screen.blit(self.images[5], (0,0))
            pygame_widgets.update(pygame.event.get())
            font = pygame.font.SysFont('Gill Sans', 60)
            print_score = font.render(f"Score: {str(round(score))}", False, (255, 0, 0))
            screen.blit(print_score, (500,50))
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
        pygame.font.init()
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
        bear = objects.Bear(self.images[2],screen, waterfall_x-round(waterfall_width/2), waterfall_height-175, True)
        waterfall_increase = 0
        waterfall_increased = 0
        damage = False
        bear_pos = random.randint(round(-waterfall_width/2), round(waterfall_width/2)-bear.rect.width)
        waterfalls_passed = 0
        points = 0
        rock0 = random.randint(-round(waterfall_width),0)
        rock1 = random.randint(-round(waterfall_width),0)
        rock2 = random.randint(-round(waterfall_width),0)
        rock3 = random.randint(-round(waterfall_width),0)
        test_mode = False
        damage_mod = 1
        health_plus = 0
        oxygen_plus = 0
        upgrade_points = 0
        thousand_upgrades = 10
        ten_thousand_upgrades = 10

        while running:
            pygame.display.set_caption('River Scaler')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
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
                elif pygame_events[pygame.K_SPACE]:
                    if test_mode == True:
                        speed += 1
                elif pygame_events[pygame.K_LSHIFT]:
                    if test_mode == True:
                        speed -= 1

            if health < 100 + health_plus:
                health += 0.02

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
                if oxygen < 100 + oxygen_plus:
                    oxygen += 0.3

            if y > 670:
                y = 670

            if test_mode == False:
                if oxygen < 0:
                    running = False
                if health < 0:
                    running = False

                if x < -200:
                    health = 0
                    running = False

            if upgrade_points > 1000 and thousand_upgrades > 0:
                oxygen_plus += 10
                oxygen = 100 + oxygen_plus
                health_plus += 10
                health = 100 + health_plus
                upgrade_points -= 1000
                thousand_upgrades -= 1

            if upgrade_points > 10000 and ten_thousand_upgrades > 0:
                oxygen_plus += 75
                oxygen = 100 + oxygen_plus
                health_plus += 50
                health = 100 + health_plus
                upgrade_points -= 10000
                ten_thousand_upgrades -= 1
                thousand_upgrades += 1

            damage_mod += 0.00003

            # River
            pygame.draw.rect(screen, (0,77,129), (0,545,1280,175))

            if waterfall_x < 0 - waterfall_width:
                waterfalls_passed += 1
                points += waterfall_width
                upgrade_points += waterfall_width
                rock0 = random.randint(-round(waterfall_width),0)
                rock1 = random.randint(-round(waterfall_width),0)
                rock2 = random.randint(-round(waterfall_width),0)
                rock3 = random.randint(-round(waterfall_width),0)
                waterfall_increase = random.randint(10,50)
                waterfall_increased += waterfall_increase
                if waterfall_height < 400:
                    waterfall_height += waterfall_increase
                waterfall_width = waterfall_width * random.randint(11, 14) / 10
                waterfall_x = 1280
                speed += (random.randint(0,1) / 10)
                bear_pos = random.randint(round(-waterfall_width/2), round(waterfall_width/2)-bear.rect.width)

            waterfall = objects.Waterfall(screen, waterfall_x, 545-waterfall_height, waterfall_width, waterfall_height)
            waterfall_x -= speed

            rock = objects.Rock(self.images[4], screen, waterfall_x-rock0, waterfall_height-waterfall_increase*waterfalls_passed)
            rock_1 = objects.Rock(self.images[4], screen, waterfall_x-rock1, waterfall_height-waterfall_increase*waterfalls_passed)
            rock_2 = objects.Rock(self.images[4], screen, waterfall_x-rock2, waterfall_height-waterfall_increase*waterfalls_passed)
            rock_3 = objects.Rock(self.images[4], screen, waterfall_x-rock3, waterfall_height-waterfall_increase*waterfalls_passed)

            if random.randint(0,100) < 5:
                bear = objects.Bear(self.images[3],screen, waterfall_x+round(waterfall_width/2)+bear_pos, bear.rect.height-waterfall_increased-60, bear.go)   
                damage = True
            else:
                bear = objects.Bear(self.images[2],screen, waterfall_x+round(waterfall_width/2)+bear_pos, bear.rect.height-waterfall_increased-60, bear.go)
                damage = False

            # Bars
            pygame.draw.rect(screen, (200,200,200), (48, 48, 204+health_plus*2, 44))
            pygame.draw.rect(screen, (255,0,0), (50, 50, health * 2, 40))
            pygame.draw.rect(screen, (200,200,200), (48, 98, 204+oxygen_plus*2, 44))
            pygame.draw.rect(screen, (0,0,255), (50, 100, oxygen * 2, 40))

            salmon = objects.Salmon(self.images[0], x, y, screen)

            font = pygame.font.SysFont('Gill Sans', 60)
            score = font.render(str(round(points)), False, (0, 0, 0))
            screen.blit(score, (300+oxygen_plus*2,50))

            # damage_log = font.render(str(damage_mod), False, (0, 0, 0))
            # screen.blit(damage_log, (500,50))

            pygame.display.flip()

            dt = clock.tick(60) / 1000

            screen.fill((255, 255, 255))

            # Collisions
            me_waterfall = pygame.sprite.collide_mask(waterfall, salmon)
            me_bear = pygame.sprite.collide_mask(bear, salmon)
            me_rock = pygame.sprite.collide_mask(rock, salmon)
            me_rock1 = pygame.sprite.collide_mask(rock_1, salmon)
            me_rock2 = pygame.sprite.collide_mask(rock_2, salmon)
            me_rock3 = pygame.sprite.collide_mask(rock_3, salmon)

            if not me_waterfall == None:
                if x + 200 < waterfall_x + waterfall_width / 2:
                    x -= 1+speed
                    oxygen += 0.4
                    if oxygen > 100+oxygen_plus:
                        oxygen = 100+oxygen_plus
                else:
                    x += 1+speed
                    oxygen += 0.9
                    if oxygen > 100+oxygen_plus:
                        oxygen = 100+oxygen_plus

            if not me_bear == None and damage == True:
                health -= random.randint(10,50) / 10 * damage_mod
            if not me_rock == None:
                health -= 0.03 * damage_mod
            if not me_rock1 == None:
                health -= 0.03 * damage_mod
            if not me_rock2 == None:
                health -= 0.03 * damage_mod
            if not me_rock3 == None:
                health -= 0.03 * damage_mod

        if not event.type == pygame.QUIT:
            self.game_over(round(points))
    def end():
        # Intentionally empty function.
        ...