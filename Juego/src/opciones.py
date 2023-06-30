import pygame
from config import load_img_alpha, WIDTH

class Opciones:
    def __init__(self, x:int, y:int, imagen):
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def mostrar_opcion(self, display):
        imagen_gris = pygame.transform.grayscale(self.image)
        display.blit(imagen_gris, (self.rect.x, self.rect.y))

    def seleccionar_opcion(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))


boton_jugar = Opciones(1100, 400, load_img_alpha("Botones/Boton_jugar.png"))
boton_seleccion_lvl = Opciones(1100, 500, load_img_alpha("Botones/Boton_seleccion.png"))
boton_sel_lvl_1 = Opciones(1100, 400, load_img_alpha("Botones/Boton_nivel1.png"))
boton_sel_lvl_2 = Opciones(1100, 500, load_img_alpha("Botones/Boton_nivel2.png"))
boton_sel_lvl_3 = Opciones(1100, 600, load_img_alpha("Botones/Boton_nivel3.png"))
boton_salir = Opciones(1100, 600, load_img_alpha("Botones/Boton_cerrar.png"))
boton_resumir = Opciones((WIDTH//2) ,200, load_img_alpha("Botones/Boton_resumir.png"))
boton_volver_al_menu = Opciones((WIDTH // 2), 400, load_img_alpha("Botones/Volver_menu.png"))
boton_volumen = Opciones((WIDTH//2), 300, load_img_alpha("Botones/Boton_volumen.png"))
boton_vol_0 = Opciones((WIDTH//2), 200, load_img_alpha("Botones/vol_0.png"))
boton_vol_50 = Opciones((WIDTH//2), 300, load_img_alpha("Botones/vol_50.png"))
boton_vol_100 = Opciones((WIDTH//2), 400, load_img_alpha("Botones/vol_100.png"))

def navegar_menu(keys:list, contador_opciones):
    seleccionar_opcion = False
    for evento in pygame.event.get():
            if keys[pygame.K_s]:
                contador_opciones += 1
            if keys[pygame.K_w]:
                contador_opciones -= 1
            if keys[pygame.K_e]:
                seleccionar_opcion = True
            if contador_opciones < 1:
                contador_opciones = 3
            elif contador_opciones > 3:
                contador_opciones = 1
    return seleccionar_opcion, contador_opciones