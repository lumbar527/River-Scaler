import river_scaler
import yaml
import pygame

images = []
load_image = pygame.image.load("test.png")
images.append(load_image)
sounds = None

game = river_scaler.RiverScaler(images, sounds)
game.run()