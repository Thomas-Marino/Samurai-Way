import pygame
from config import load_img_alpha

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, left, top, width, height):
        super().__init__()
        self.rect = pygame.rect.Rect(left, top, width, height)
        self.top = self.rect.top
        self.bottom = self.rect.bottom
        self.lef = self.rect.left
        self.right = self.rect.right
        self.image = pygame.transform.scale(load_img_alpha("Pisos/0.png"), (215, 15))

def generacion_terreno(cargar_lv1, cargar_lv2, cargar_lv3):
    group_plataformas = pygame.sprite.Group()
    if cargar_lv1 or cargar_lv2 or cargar_lv3:
        plataforma_1 = Plataforma(200, 580, 200, 10)
        plataforma_2 = Plataforma(500, 490, 200, 10)
        group_plataformas.add(plataforma_1, plataforma_2)
    if cargar_lv2 or cargar_lv3:
        plataforma_3 = Plataforma(700, 400, 200, 10)
        plataforma_4 = Plataforma(400, 350, 200, 10)
        group_plataformas.add(plataforma_3, plataforma_4)
        if cargar_lv3:
            plataforma_5 = Plataforma(200, 390, 200, 10)
            plataforma_6 = Plataforma(0, 390, 200, 10)
            plataforma_7 = Plataforma(1100, 300, 200, 10)
            plataforma_8 = Plataforma(700, 200, 200, 10)
            group_plataformas.add(plataforma_5, plataforma_6, plataforma_7, plataforma_8)
    return group_plataformas



plataforma_1 = Plataforma(200, 580, 200, 10)
plataforma_2 = Plataforma(500, 490, 200, 10)
plataforma_3 = Plataforma(700, 400, 200, 10)
plataforma_4 = Plataforma(400, 350, 200, 10)
plataforma_5 = Plataforma(200, 390, 200, 10)
plataforma_6 = Plataforma(0, 390, 200, 10)
plataforma_7 = Plataforma(1100, 300, 200, 10)
plataforma_8 = Plataforma(700, 200, 200, 10)
trampa = pygame.rect.Rect(200, 390, 200, 10)