import pygame

class Salmon(pygame.sprite.Sprite):
    def __init__(self, image, x, y, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = image

        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect().move(x, y)

        self.mask = pygame.mask.from_surface(self.image)

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

        self.rect = pygame.Rect(x, y, width, height)

        self.mask = pygame.mask.Mask(size=(self.rect.width, self.rect.height), fill=False)

        pygame.draw.rect(screen, (0,0,255), self.rect)