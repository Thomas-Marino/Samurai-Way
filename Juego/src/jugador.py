import pygame
from config import agrupar_imagenes, load_img_alpha

class Jugador():
    def __init__(self, x, y):
        self.image = load_img_alpha("Jugador/Quieto/2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    # Animacion al correr --------------------------------
    def mostrar_animacion_coriendo(self, frame, display, izquierda = 0):
        jugador_corriendo = agrupar_imagenes("Jugador/Correr/")
        if izquierda == 0:
            self.image = jugador_corriendo[frame]
        else:
            self.image = pygame.transform.flip(jugador_corriendo[frame], True, False)
        self.rect_2 = self.image.get_rect()
        self.rect_2.center = self.rect.center
        display.blit(self.image, self.rect_2)
    # Animacion al estar quieto --------------------------
    def mostrar_animacion_quieto(self, frame, display, izquierda = 0):
        jugador_quieto = agrupar_imagenes("Jugador/Quieto/")    
        if izquierda == 0:
            self.image = jugador_quieto[frame]
        else:
            self.image = pygame.transform.flip(jugador_quieto[frame], True, False)
        self.rect_2 = self.image.get_rect()
        self.rect_2.center = self.rect.center
        display.blit(self.image, self.rect_2)
    # Animacion de atacar --------------------------------
    def mostrar_animacion_ataque(self, frame, display, izquierda = 0):
        jugador_atacando = agrupar_imagenes("Jugador/Ataque/")
        if izquierda == 0:
            self.image = jugador_atacando[frame]
        else:
            self.image = pygame.transform.flip(jugador_atacando[frame], True, False)
        self.rect_2 = self.image.get_rect()
        self.rect_2.center = self.rect.center
        display.blit(self.image, self.rect_2)
    # Animacion de muerte --------------------------------
    def mostrar_animacion_muerte(self, frame, display, izquierda = 0):
        jugador_muerto = agrupar_imagenes("Jugador/Muerte/")
        if izquierda == 0:
            self.image = jugador_muerto[frame]
        else:
            self.image = pygame.transform.flip(jugador_muerto[frame], True, False)
        self.rect_2 = self.image.get_rect()
        self.rect_2.center = self.rect.center
        display.blit(self.image, self.rect_2)
    def mostrar_animacion_caida(self, frame, display, izquierda = 0):
        jugador_cayendo = agrupar_imagenes("Jugador/Caida/")
        if izquierda == 0:
            self.image = jugador_cayendo[frame]
        else:
            self.image = pygame.transform.flip(jugador_cayendo[frame], True, False)
        self.rect_2 = self.image.get_rect()
        self.rect_2.center = self.rect.center
        display.blit(self.image, self.rect_2)
    # hitbox ---------------------------------------------
    def hitbox(self):
        self.rect_hitbox = self.image.get_rect()
        self.rect_hitbox.center = self.rect.center
    def mostrar_hitbox(self, display, color):
        self.rect_2 = self.image.get_rect()
        self.rect_2.center = self.rect.center
        pygame.draw.rect(display, color, self.rect_2, 2)
