import pygame
import random

class Salmon(pygame.sprite.Sprite):
    def __init__(self, image, x, y, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = image

        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect().move(x, y)

        self.mask = pygame.mask.from_surface(self.image)

        # self.image = pygame.transform.scale(self.image, (400, 800)) # Testing to see if this works. [x]

        screen.blit(self.image, (x, y))

class Wave(pygame.sprite.Sprite):
    def __init__(self, image, screen, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = image

        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect().move(x, y)

        self.mask = pygame.mask.from_surface(self.image)

        screen.blit(self.image, (x, y))

class Waterfall(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        height += 545

        self.rect = pygame.Rect(x, y, width, height)

        self.mask = pygame.mask.Mask(size=(self.rect.width, self.rect.height), fill=True)

        pygame.draw.rect(screen, (0,77,129), self.rect)

class Bear(pygame.sprite.Sprite):
    def __init__(self, image, screen, x, y, go):
        pygame.sprite.Sprite.__init__(self)

        if x > 1200:
            go = True

        self.image = image

        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect().move(x, y)

        self.mask = pygame.mask.from_surface(self.image)

        if x < 0 - self.rect.width and go == True:
            grow = random.randint(10, 11) / 10
            self.image = pygame.transform.scale(self.image, (self.rect.width*grow, self.rect.height*grow))
            go = False

        screen.blit(self.image, (x, y))

        self.go = go