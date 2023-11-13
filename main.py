import river_scaler
import yaml
import pygame

images = []
load_image = pygame.image.load("salmon.png")
images.append(load_image)
load_image = pygame.image.load("title.png")
images.append(load_image)
load_image = pygame.image.load("bear.png")
images.append(load_image)
load_image = pygame.image.load("bear1.png")
images.append(load_image)
load_image = pygame.image.load("rock.png")
images.append(load_image)
load_image = pygame.image.load("wave.png")
images.append(load_image)
load_image = pygame.image.load("game_over.png")
images.append(load_image)
load_image = pygame.image.load("wave2.png")
images.append(load_image)
sounds = None

playing = True

game = river_scaler.RiverScaler(images, sounds)
game.title_screen()