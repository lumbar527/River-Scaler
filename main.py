import river_scaler
import yaml
import pygame

images = []
load_image = pygame.image.load("salmon.png")
images.append(load_image)
load_image = pygame.image.load("title.png")
images.append(load_image)
sounds = None

game = river_scaler.RiverScaler(images, sounds)
game.title_screen()
# game.run()