import pygame.mixer
import pygame

pygame.mixer.init(48000)

cancion_menu = "./src/sounds/Naruto Main Theme.mp3"

cancion_nivel ="./src/sounds/Bad Situation (320 kbps).mp3"

sonido_hit = pygame.mixer.Sound("./src/sounds/hit.wav")

sonido_miss = pygame.mixer.Sound("./src/sounds/miss.wav")

sonido_muerte = pygame.mixer.Sound("./src/sounds/sonido_muerte.OGG")