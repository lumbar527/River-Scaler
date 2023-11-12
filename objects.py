import pygame

class Salmon(pygame.sprite.Sprite):
    def __init__(self, image, x, y, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = image

        self.rect = self.image.get_rect().move(x, y)

        self.mask = pygame.mask.from_surface(self.image)

        screen.blit(self.image, (x, y))
