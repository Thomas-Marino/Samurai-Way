# Imports ----------------------------------------
import pygame, sys, pygame.font, opciones, plataformas, enemigos, jugador
from sonidos import *
from config import *
# Setup de la ventana/pygame ---------------------
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Samurai Way")
reloj = pygame.time.Clock()
# Imagenes ---------------------------------------
bg = load_img("Bg_1.png")
# .................................................
posibilidad_salto = False
# Botones y menu -----------------------------------------
portada = load_img("Menu.png")
pygame.mouse.set_visible(False)
contador_opciones = 1
play_cancion_menu = True
while jugar:
    # Inputs ------------------------------------------
    pygame.mixer.music.set_volume(seleccion_vol)
    if not menu_principal:
        display.blit(bg, (0,0)) # BG
    keys = pygame.key.get_pressed()
    if menu_principal or seleccion_de_niveles or pausa:
        if play_cancion_menu: 
            pygame.mixer.music.load(cancion_menu)
            pygame.mixer.music.play()
            play_cancion_menu = False
        if menu_principal:
            display.blit(portada, (0,0))
    # Controles del menu ------------------------------
        seleccionar_opcion, contador_opciones = opciones.navegar_menu(keys, contador_opciones)
    # Mostrar opciones seleccionadas -------------------------------
        match contador_opciones:
            case 1:
                if menu_principal:
                    opciones.boton_jugar.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        menu_principal = False
                    generar_terreno = True
                    generar_enemigos = True
                    generar_jugador = True
                    play_cancion_nivel = True
                    contador_tiempo = 45
                    if (not cargar_lv1 and 
                        not cargar_lv2 and 
                        not cargar_lv3):
                        cargar_lv1 = True
                elif seleccion_de_niveles:
                    opciones.boton_sel_lvl_1.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        cargar_lv1 = True
                        cargar_lv2 = False
                        cargar_lv3 = False
                        menu_principal = True
                        seleccion_de_niveles = False
                elif mostrar_menu_volumen:
                    opciones.boton_vol_0.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        mostrar_menu_volumen = False
                        seleccion_vol = 0
                elif not mostrar_menu_volumen and not menu_principal and not seleccion_de_niveles:
                    opciones.boton_resumir.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        pausa = False
            case 2:
                if not mostrar_menu_volumen and not menu_principal and not seleccion_de_niveles: # Menu de pausa
                    opciones.boton_volumen.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        mostrar_menu_volumen = True
                elif mostrar_menu_volumen: # Menu de volumen
                    opciones.boton_vol_50.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        mostrar_menu_volumen = False
                        seleccion_vol = 0.25
                elif menu_principal: # Menu principal
                    opciones.boton_seleccion_lvl.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        seleccion_de_niveles = True
                        menu_principal = False
                elif seleccion_de_niveles: # Menu de seleccion de niveles
                    opciones.boton_sel_lvl_2.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        cargar_lv1 = False
                        cargar_lv2 = True
                        cargar_lv3 = False
                        menu_principal = True
                        seleccion_de_niveles = False
            case 3:
                if not mostrar_menu_volumen and not menu_principal and not seleccion_de_niveles:
                    opciones.boton_volver_al_menu.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        pausa = False
                        menu_principal = True
                        play_cancion_menu = True
                elif mostrar_menu_volumen:
                    opciones.boton_vol_100.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        mostrar_menu_volumen = False
                        seleccion_vol = 0.5
                elif menu_principal:
                    opciones.boton_salir.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        pygame.quit()
                        sys.exit()
                elif seleccion_de_niveles:
                    opciones.boton_sel_lvl_3.seleccionar_opcion(display)
                    if seleccionar_opcion:
                        cargar_lv1 = False
                        cargar_lv2 = False
                        cargar_lv3 = True
                        menu_principal = True
                        seleccion_de_niveles = False
    # Mostrar opciones sin seleccionar ---------------------------
        if contador_opciones != 1:
            if not mostrar_menu_volumen and not menu_principal and not seleccion_de_niveles:
                opciones.boton_resumir.mostrar_opcion(display)
            elif mostrar_menu_volumen:
                opciones.boton_vol_0.mostrar_opcion(display)
            elif menu_principal:
                opciones.boton_jugar.mostrar_opcion(display)
            elif seleccion_de_niveles:
                opciones.boton_sel_lvl_1.mostrar_opcion(display)
        if contador_opciones != 2:
            if not mostrar_menu_volumen and not menu_principal and not seleccion_de_niveles:
                opciones.boton_volumen.mostrar_opcion(display)
            elif mostrar_menu_volumen:
                opciones.boton_vol_50.mostrar_opcion(display)
            elif menu_principal:
                opciones.boton_seleccion_lvl.mostrar_opcion(display)
            elif seleccion_de_niveles:
                opciones.boton_sel_lvl_2.mostrar_opcion(display)
        if contador_opciones != 3:
            if not mostrar_menu_volumen and not menu_principal and not seleccion_de_niveles:
                opciones.boton_volver_al_menu.mostrar_opcion(display)
            elif mostrar_menu_volumen:
                opciones.boton_vol_100.mostrar_opcion(display)
            elif menu_principal:
                opciones.boton_salir.mostrar_opcion(display)
            elif seleccion_de_niveles:
                opciones.boton_sel_lvl_3.mostrar_opcion(display)
    # Reset de opcion ---------------------------------
        if seleccionar_opcion:
            seleccionar_opcion = False
            contador_opciones = 1
    # Juego -------------------------------------------
    if not pausa and not menu_principal and not seleccion_de_niveles:
        if generar_jugador:
            player = jugador.Jugador(50, 600)
            muerte_jugador = False
            generar_jugador = False
        if play_cancion_nivel: 
            pygame.mixer.music.load(cancion_nivel)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            play_cancion_nivel = False
    # Movimiento --------------------------------------
        if not attack and not muerte_jugador:
            if (player.rect.bottom < terreno.top and 
                not saltando):
                cayendo = True
            else:
                cayendo = False
                posibilidad_salto = True
            if keys[pygame.K_SPACE] and posibilidad_salto:
                saltando = True
            if player.rect.right < WIDTH:
                if keys[pygame.K_d]:
                    player.rect.x += speed_x
                    izquierda = False
                    corriendo = True
            else:
                player.rect.right = WIDTH
            if player.rect.left > 0:
                if keys[pygame.K_a]:
                    player.rect.x -= speed_x
                    izquierda = True
                    corriendo = True
            if keys[pygame.K_f] and not cd_dash:
                dashing = True
    # PAUSA -------------------------------------------
        if keys[pygame.K_ESCAPE]:
            pausa = True
    # GENERACION DE PLATAFORMAS -----------------------
        if generar_terreno:
            group_plataformas = plataformas.generacion_terreno(cargar_lv1, cargar_lv2, cargar_lv3)
            generar_terreno = False
        if cargar_lv3:
            trampa = pygame.rect.Rect(200, 390, 200, 10)
    # GENERACION DE ENEMIGOS --------------------------
        if generar_enemigos:
            sprites_muertos = []
            group_enemigos, contador_enemigos = enemigos.generacion_de_enemigos(cargar_lv1, cargar_lv2, cargar_lv3)
            generar_enemigos = False
    # COLISIONES -------------------------------------- 
        for sprite in group_plataformas:
            if sprite.rect.colliderect(player.rect.left, player.rect.bottom, player.rect.width, 1):
                cayendo = False
                posibilidad_salto = True
        if cargar_lv3:
            if trampa.colliderect(player.rect.left, player.rect.bottom, player.rect.width, 1):
                muerte_jugador = True
    # EVENTOS -----------------------------------------
        for evento in pygame.event.get():
            if evento.type == pygame.KEYUP:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN and not cd_ataque and not muerte_jugador:
                attack = True
                cd_ataque = True
    # COOLDOWNS --------------------------------------------------
        if cd_ataque:
            contador_cd_ataque += 1
            if contador_cd_ataque == 30:
                contador_cd_ataque = 0
                cd_ataque = False
        if cd_dash:
            contador_cd_dash += 1
            if contador_cd_dash == 200:
                contador_cd_dash = 0
                cd_dash = False
    # ================ MOVIMIENTOS DEL JUGADOR ===================
    # DASH -------------------------------------------------------
        if dashing:
            if cayendo:
                cayendo = False
            posibilidad_salto = False
            if not izquierda:
                player.rect.x += speed_x * 5
            else:
                player.rect.x -= speed_x * 5
            contador_dasheo += 1
            if contador_dasheo == 1:
                attack = True
            if contador_dasheo > 10:
                contador_dasheo = 0
                if not kill:
                    cd_dash = True
                if kill:
                    kill = False
                dashing = False
    # CAIDA -------------------------------------------------------
        if cayendo:
            if not izquierda:
                player.mostrar_animacion_caida(frame_salto, display)
            else:
                player.mostrar_animacion_caida(frame_salto, display, 1)
            frame_salto, contador_frames_salto = animacion_cd(frame_salto, contador_frames_salto, 5, 1)
            speed_y += 0.4 
            if speed_y >= 9.8:
                speed_y = 9.8
            attack = False
            posibilidad_salto = False
            player.rect.y += speed_y
        else:
            speed_y = 1.8
    # SALTO ------------------------------------------------------
        if saltando and posibilidad_salto:
            attack = False # El jugador no puede atacar en el aire
            contador_frames_salto += 1
            player.rect.y -= speed_salto
            posibilidad_salto = False
            if contador_frames_salto == 20:
                saltando = False
                cayendo = True
                contador_frames_salto = 0
    # ATAQUE --------------------------------------------------------
        if attack:
            if not izquierda:
                player.mostrar_animacion_ataque(frame_ataque, display)
            else:
                player.mostrar_animacion_ataque(frame_ataque, display, 1)
            frame_ataque, contador_3 = animacion_cd(frame_ataque, contador_3, 5, 3)
            if frame_ataque == 3:
                if contador_3 == 4:
                    sonido_miss.set_volume(seleccion_vol - 0.1)
                    sonido_miss.play()
                    frame_ataque = 0
                    attack = False
            for sprite in group_enemigos:
                if player.rect_2.colliderect(sprite.rect):
                    kill = True
                    sonido_hit.set_volume(seleccion_vol)
                    sonido_hit.play()
                    sprite_position = sprite.rect.topleft
                    sprite.kill()
                    contador_enemigos -= 1
                    sprites_muertos.append(sprite_position)
    # QUIETO ---------------------------------------------------------
        else:
            if not muerte_jugador:
                if not cayendo:
                    if not corriendo :
                        if not izquierda:
                            player.mostrar_animacion_quieto(frame, display)
                        else:
                            player.mostrar_animacion_quieto(frame, display, 1)
                        frame, contador = animacion_cd(frame, contador, 8, 7)
                    else:
                        if not izquierda:
                            player.mostrar_animacion_coriendo(frame, display)
                        else:
                            player.mostrar_animacion_coriendo(frame, display, 1)
                        frame, contador_2 = animacion_cd(frame, contador_2, 4, 7)
        for pos in sprites_muertos:
            display.blit(load_img_alpha("Enemigos/Muerte/0.png"), pos)
    # Muerte del Jugador ----------------------------------------------
        if muerte_jugador:
            if not animacion_muerte_completada:
                if not izquierda:
                    player.mostrar_animacion_muerte(frame_muerte, display)
                else:
                    player.mostrar_animacion_muerte(frame_muerte, display,1)
                frame_muerte, contador_muerte = animacion_cd(frame_muerte, contador_muerte, 10, 5)
                if frame_muerte == 0:
                    sonido_muerte.play()
                if frame_muerte == 5:
                    animacion_muerte_completada = True
                    frame_muerte = 0
                    contador_muerte = 0
            else:
                display.blit(load_img_alpha("Enemigos/Muerte/0.png"), player.rect)
    # Blits ------------------------------------------------------------
        group_plataformas.draw(display)
        group_enemigos.draw(display)
        group_enemigos.update()
        if cargar_lv3:
            display.blit(pygame.transform.scale(load_img_alpha("Pisos/trampa.png") ,(215, 15)), (plataformas.plataforma_5.lef, plataformas.plataforma_5.top - 10))
        for sprite in group_enemigos:
            if sprite.rect.colliderect(player.rect):
                muerte_jugador = True
    # Texto en pantalla y eventos con tiempo ---------------------------
        if contador_tiempo < 0:
            muerte_jugador = True
            contador_tiempo = 0
        font = pygame.font.Font("./src/fonts/DJGROSS.ttf", 25)
        if contador_enemigos != 0:
            texto = font.render(f"Enemigos restantes: {contador_enemigos}", True, BLANCO)
            pasar_tiempo += 1
            if pasar_tiempo == 60:
                contador_tiempo -= 1
                pasar_tiempo = 0
            tiempo_restante = font.render(f"Tiempo: {contador_tiempo}", True, BLANCO)
            display.blit(texto, (50, 50))
            display.blit(tiempo_restante,(1100, 50))
        if contador_enemigos == 0 and cargar_lv3:
            texto = font.render("Nivel superado! Pulse backspace para volver al menú", True, BLANCO)
            display.blit(texto, (250, 50))
            if keys[pygame.K_BACKSPACE]:
                menu_principal = True
                play_cancion_menu = True
        elif contador_enemigos == 0 and not cargar_lv3:
            texto = font.render("Nivel superado! Pulse backspace para pasar al siguiente nivel", True, BLANCO)
            display.blit(texto, (100, 50))
            if keys[pygame.K_BACKSPACE]:
                if cargar_lv2 == True:
                    cargar_lv3 = True
                    cargar_lv2 = False
                if cargar_lv1 == True:
                    cargar_lv2 = True
                    cargar_lv1 = False
                generar_enemigos = True
                generar_terreno = True
                generar_jugador = True
        if muerte_jugador:
            texto = font.render("Has muerto! Pulsa R para reiniciar.", True, BLANCO)
            display.blit(texto, (500, 50))
            if keys[pygame.K_r]:
                generar_enemigos = True
                generar_jugador = True
                animacion_muerte_completada = False
                contador_tiempo = 60
    # MOSTRAR HITBOXES ---------------------------------------
        if keys[pygame.K_TAB]:
            mostrar_hitbox = True
            if mostrar_hitbox == True:
                player.mostrar_hitbox(display, VERDE)
                for enemigo in group_enemigos:
                    enemigo.mostrar_hitbox(display, ROJO)
    # Linea de actualizacion ---------------------------------
    reloj.tick(FPS)
    pygame.display.flip() 