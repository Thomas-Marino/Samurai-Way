import pygame, random
from config import load_img_alpha
import plataformas

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images_caminar_derecha = []  # Lista de imágenes para caminar hacia la derecha
        self.images_caminar_izquierda = []  # Lista de imágenes para caminar hacia la izquierda
        self.frame = 0  # Índice del marco actual
        self.tiempo_entre_animacion = 0  # Temporizador de animación
        self.cargar_imagenes()  # Cargar las imágenes de la animación
        self.image = self.images_caminar_derecha[self.frame]  # Establecer la imagen inicial
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = "def"
        self.move_counter = 0
        self.dir = random.randint(0,1)

    def cargar_imagenes(self):
        # Cargar las imágenes de la animación de caminar hacia la derecha
        for i in range(4):
            img = load_img_alpha(f"Enemigos/Movimiento/{i}.png")
            self.images_caminar_derecha.append(img)
        # Cargar las imágenes de la animación de caminar hacia la izquierda
        for i in range(4):
            img = pygame.transform.flip(load_img_alpha(f"Enemigos/Movimiento/{i}.png"), True, False)
            self.images_caminar_izquierda.append(img)

    def update(self):
        if self.move_direction == "def":
            if self.dir == 1:
                self.move_direction = -1
            else:
                self.move_direction = 1
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter > 90:
            self.move_direction *= -1
            self.move_counter *= -1

        # Actualizar la animación
        self.tiempo_entre_animacion += 1
        if self.tiempo_entre_animacion > 15:  # Velocidad de la animación
            self.frame = (self.frame + 1) % len(self.images_caminar_derecha)
            if self.move_direction == 1:  # Caminar hacia la derecha
                self.image = self.images_caminar_derecha[self.frame]
            else:  # Caminar hacia la izquierda
                self.image = self.images_caminar_izquierda[self.frame]
            self.tiempo_entre_animacion = 0

    def hitbox(self):
        self.rect_hitbox = self.image.get_rect()
        self.rect_hitbox.center = self.rect.center

    def mostrar_hitbox(self, display, color):
        self.rect_2 = self.image.get_rect()
        self.rect_2.center = self.rect.center
        pygame.draw.rect(display, color, self.rect_2, 2)

def generacion_de_enemigos(cargar_lv1, cargar_lv2, cargar_lv3):
    if cargar_lv1 or cargar_lv2 or cargar_lv3:
        group_enemigos = pygame.sprite.Group()
        enemigo_1 = Enemigo(300, (plataformas.plataforma_1.top - 45))
        enemigo_2 = Enemigo(600, (plataformas.plataforma_2.top - 45))
        # muerte_e1, muerte_e2 = False, False
        contador_enemigos = 2
        group_enemigos.add(enemigo_1, enemigo_2)
        if cargar_lv2 or cargar_lv3:
            enemigo_3 = Enemigo(800, (plataformas.plataforma_3.top - 45))
            enemigo_4 = Enemigo(500, (plataformas.plataforma_4.top - 45))
            # muerte_e3, muerte_e4 = False, False
            contador_enemigos = 4
            group_enemigos.add(enemigo_3, enemigo_4)
        if cargar_lv3:
            enemigo_5 = Enemigo(100, (plataformas.plataforma_6.top - 45))
            enemigo_5.move_direction = 1
            enemigo_8 = Enemigo(100, (plataformas.plataforma_6.top - 45))
            enemigo_8.move_direction = -1
            enemigo_6 = Enemigo(800, (plataformas.plataforma_8.top - 45))
            enemigo_6.move_direction = -1
            enemigo_7 = Enemigo(800, (plataformas.plataforma_8.top - 45))
            enemigo_7.move_direction = 1
            # muerte_e5, muerte_e6, muerte_e7, muerte_e8 = False, False, False, False 
            group_enemigos.add(enemigo_5, enemigo_6, enemigo_7, enemigo_8)
            contador_enemigos = 8
    return group_enemigos, contador_enemigos
