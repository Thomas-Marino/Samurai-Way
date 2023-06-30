import  pygame

FPS = 60

AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
YELLOW = (255, 255, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

WIDTH = 1280
HEIGHT = 720
CENTER = WIDTH // 2, HEIGHT // 2

display = pygame.display.set_mode((WIDTH, HEIGHT))

# =========== Declaracion de variables ===========
# =========== Variables del jugador ==============
speed_x = 3
speed_y = 1.8
speed_salto = 6
muerte_jugador = False
animacion_muerte_completada = False
izquierda = False
corriendo = False
saltando = False
cayendo = True
attack = False
cd_ataque = False
contador_cd_ataque = 1
dashing = False
cd_dash = 0
contador_dasheo = 0
contador_cd_dash = 0
# Variables para el entorno -----------------------
jugar = True
seleccion_vol = 0.5
pasar_tiempo = 0
contador_tiempo = 60
contador = 1
contador_2 = 1
contador_3 = 0
contador_frames_salto = 0
frame = 0
frame_ataque = 0
frame_salto = 0
terreno = pygame.draw.rect(display, BLANCO, (0, 680, 1280 ,10))
# Enemigos ----------------------------------------
kill = False
frame_muerte = 0
contador_muerte = 0
# Menu --------------------------------------------
pausa = False
seleccionar_opcion = False
mostrar_menu_volumen = False
seleccion_de_niveles = False
menu_principal = True
cargar_lv1 = False
cargar_lv2 = False
cargar_lv3 = False

def load_img(nombre):
    img = pygame.image.load('./src/images/' + nombre).convert()
    return img
def load_img_alpha(nombre):
    img = pygame.image.load('./src/images/' + nombre).convert_alpha()
    return img

def agrupar_imagenes(path):
    try:
        lista = []
        index_test = []
        for i in range(100):
            index_test.append(load_img_alpha(path + f"{i}.png"))
            lista.append(load_img_alpha(path + f"{i}.png"))
    except FileNotFoundError:
        return lista

def animacion_cd(frame, contador, tiempo_entre_frames, max_frame):
    contador += 1
    if contador == tiempo_entre_frames:
        frame += 1
        contador = 0
    if frame > max_frame:
        frame = 0
        # contador = 0
    # print(frame, contador)
    return frame, contador



