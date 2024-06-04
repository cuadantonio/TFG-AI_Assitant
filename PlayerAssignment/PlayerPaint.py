from io import BytesIO

import pygame
import sys

import requests

# Inicializar pygame
print(1)
pygame.init()
print(2)

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Definir la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Alineación de Fútbol")

# Cargar imagen del campo de fútbol
campo_img = pygame.image.load("campo_futbol.jpg")
campo_img = pygame.transform.scale(campo_img, (ANCHO, ALTO))

# Función para dibujar jugadores

def cargar_imagen_desde_url(url):
    response = requests.get(url)
    imagen = pygame.image.load(BytesIO(response.content))
    return imagen
def dibujar_jugador(posicion, nombre, imagen_url):
    fuente = pygame.font.SysFont("Gill Sans", 20)
    texto = fuente.render(nombre, True, NEGRO,BLANCO)
    rectangulo = texto.get_rect()
    rectangulo.center = (posicion[0], posicion[1] - 20)  # Modificado para que el nombre esté encima del jugador
    pantalla.blit(texto, rectangulo)

    imagen = cargar_imagen_desde_url(imagen_url)
    imagen = pygame.transform.scale(imagen, (50, 50))
    rectangulo_imagen = imagen.get_rect()
    rectangulo_imagen.center = (posicion[0], posicion[1] + 20)
    pantalla.blit(imagen, rectangulo_imagen)

# Función para dibujar una alineación 3-4-3
def dibujar_alineacion_343(jugadores, imagenes_urls):
    # Definir posiciones base de los jugadores para la alineación 3-4-3
    posiciones_base = {
        "Portero": (ANCHO // 2, ALTO // 7),
        "Defensa": [(ANCHO // 4, ALTO // 3), (ANCHO // 2, ALTO // 3), (3 * ANCHO // 4, ALTO // 3)],
        "Centrocampista": [(ANCHO // 4, 1.75 * ALTO // 3), (1.6 * ANCHO // 4, 1.75 * ALTO // 3),
                           (2.4 * ANCHO // 4, 1.75 * ALTO // 3), (3 * ANCHO // 4, 1.75 * ALTO // 3)],
        "Delantero": [(ANCHO // 4, 5 * ALTO // 6), (ANCHO // 2, 5 * ALTO // 6), (3 * ANCHO // 4, 5 * ALTO // 6)]
    }

    pantalla.fill(NEGRO)
    pantalla.blit(campo_img, (0, 0))

    # Dibujar jugadores en las posiciones correspondientes
    for i, fila in enumerate(jugadores):
        for j, jugador in enumerate(fila):
            nombre = jugador
            imagen_url = imagenes_urls[i][j]
            if i == 0:
                posicion_base = posiciones_base["Portero"]
            elif i == 1:
                posicion_base = posiciones_base["Defensa"][j]
            elif i == 2:
                posicion_base = posiciones_base["Centrocampista"][j]
            else:
                posicion_base = posiciones_base["Delantero"][j]
                # Si hay más delanteros que posiciones base, los distribuye equitativamente
                """posiciones_delanteros = posiciones_base["Delantero"]
                num_delanteros = len(fila)
                espacio_entre_jugadores = ANCHO // (num_delanteros + 1)
                posicion_base = (espacio_entre_jugadores * (j + 1), posiciones_delanteros[0][1])"""
            dibujar_jugador(posicion_base, nombre,imagen_url)

    # Manejo de eventos


    pygame.display.flip()

def dibujar_alineacion_442(jugadores, imagenes_urls):
    # Definir posiciones base de los jugadores para la alineación 3-4-3
    posiciones_base = {
        "Portero": (ANCHO // 2, ALTO // 7),
        "Defensa": [(ANCHO // 4, ALTO // 3), (1.6 * ANCHO // 4, ALTO // 3),
                    (2.4 * ANCHO // 4, ALTO // 3),(3 * ANCHO // 4, ALTO // 3)],
        "Centrocampista": [(ANCHO // 4, 1.75 * ALTO // 3), (1.6 * ANCHO // 4, 1.75 * ALTO // 3),
                           (2.4 * ANCHO // 4, 1.75 * ALTO // 3), (3 * ANCHO // 4, 1.75 * ALTO // 3)],
        "Delantero": [(ANCHO // 4, 5 * ALTO // 6), (ANCHO // 2, 5 * ALTO // 6)]
    }

    pantalla.fill(NEGRO)
    pantalla.blit(campo_img, (0, 0))

    # Dibujar jugadores en las posiciones correspondientes
    for i, fila in enumerate(jugadores):
        for j, jugador in enumerate(fila):
            nombre = jugador
            imagen_url = imagenes_urls[i][j]
            if i == 0:
                posicion_base = posiciones_base["Portero"]
            elif i == 1:
                posicion_base = posiciones_base["Defensa"][j]
            elif i == 2:
                posicion_base = posiciones_base["Centrocampista"][j]
            else:
                # Si hay más delanteros que posiciones base, los distribuye equitativamente
                posiciones_delanteros = posiciones_base["Delantero"]
                num_delanteros = len(fila)
                espacio_entre_jugadores = ANCHO // (num_delanteros + 1)
                posicion_base = (espacio_entre_jugadores * (j + 1), posiciones_delanteros[0][1])
            dibujar_jugador(posicion_base, nombre,imagen_url)

    # Manejo de eventos


    pygame.display.flip()

def dibujar_alineacion_541(jugadores, imagenes_urls):
    # Definir posiciones base de los jugadores para la alineación 3-4-3
    posiciones_base = {
        "Portero": (ANCHO // 2, ALTO // 7),
        "Defensa": [(ANCHO // 4, ALTO // 3), (1.5 * ANCHO // 4, ALTO // 3), (2 * ANCHO // 4, ALTO // 3),
                    (2.5 * ANCHO // 4, ALTO // 3),(3 * ANCHO // 4, ALTO // 3)],
        "Centrocampista": [(ANCHO // 4, 1.75 * ALTO // 3), (1.6 * ANCHO // 4, 1.75 * ALTO // 3),
                           (2.4 * ANCHO // 4, 1.75 * ALTO // 3), (3 * ANCHO // 4, 1.75 * ALTO // 3)],
        "Delantero": [(ANCHO // 2, 5 * ALTO // 6)]
    }

    pantalla.fill(NEGRO)
    pantalla.blit(campo_img, (0, 0))

    # Dibujar jugadores en las posiciones correspondientes
    for i, fila in enumerate(jugadores):
        for j, jugador in enumerate(fila):
            nombre = jugador
            imagen_url = imagenes_urls[i][j]
            if i == 0:
                posicion_base = posiciones_base["Portero"]
            elif i == 1:
                posicion_base = posiciones_base["Defensa"][j]
            elif i == 2:
                posicion_base = posiciones_base["Centrocampista"][j]
            else:
                # Si hay más delanteros que posiciones base, los distribuye equitativamente
                posiciones_delanteros = posiciones_base["Delantero"]
                num_delanteros = len(fila)
                espacio_entre_jugadores = ANCHO // (num_delanteros + 1)
                posicion_base = (espacio_entre_jugadores * (j + 1), posiciones_delanteros[0][1])
            dibujar_jugador(posicion_base, nombre,imagen_url)

    # Manejo de eventos


    pygame.display.flip()

def dibujar_alineacion_451(jugadores, imagenes_urls):
    # Definir posiciones base de los jugadores para la alineación 3-4-3
    posiciones_base = {
        "Portero": (ANCHO // 2, ALTO // 7),
        "Defensa": [(ANCHO // 4, ALTO // 3), (1.6 * ANCHO // 4, ALTO // 3),
                    (2.4 * ANCHO // 4, ALTO // 3),(3 * ANCHO // 4, ALTO // 3)],
        "Centrocampista": [(ANCHO // 4, 1.75 * ALTO // 3), (1.5 * ANCHO // 4, 1.75 * ALTO // 3), (2 * ANCHO // 4, 1.75 * ALTO // 3),
                           (2.5 * ANCHO // 4, 1.75 * ALTO // 3), (3 * ANCHO // 4, 1.75 * ALTO // 3)],
        "Delantero": [(ANCHO // 2, 5 * ALTO // 6)]
    }

    pantalla.fill(NEGRO)
    pantalla.blit(campo_img, (0, 0))

    # Dibujar jugadores en las posiciones correspondientes
    for i, fila in enumerate(jugadores):
        for j, jugador in enumerate(fila):
            nombre = jugador
            imagen_url = imagenes_urls[i][j]
            if i == 0:
                posicion_base = posiciones_base["Portero"]
            elif i == 1:
                posicion_base = posiciones_base["Defensa"][j]
            elif i == 2:
                posicion_base = posiciones_base["Centrocampista"][j]
            else:
                # Si hay más delanteros que posiciones base, los distribuye equitativamente
                posiciones_delanteros = posiciones_base["Delantero"]
                num_delanteros = len(fila)
                espacio_entre_jugadores = ANCHO // (num_delanteros + 1)
                posicion_base = (espacio_entre_jugadores * (j + 1), posiciones_delanteros[0][1])
            dibujar_jugador(posicion_base, nombre,imagen_url)

    # Manejo de eventos


    pygame.display.flip()
#Probar desde aqui
def dibujar_alineacion_352(jugadores, imagenes_urls):
    # Definir posiciones base de los jugadores para la alineación 3-4-3
    posiciones_base = {
        "Portero": (ANCHO // 2, ALTO // 7),
        "Defensa": [(ANCHO // 4, ALTO // 3), (ANCHO // 2, ALTO // 3), (3 * ANCHO // 4, ALTO // 3)],
        "Centrocampista": [(ANCHO // 4, 1.75 * ALTO // 3), (1.5 * ANCHO // 4, 1.75 * ALTO // 3), (2 * ANCHO // 4, 1.75 * ALTO // 3),
                           (2.5 * ANCHO // 4, 1.75 * ALTO // 3), (3 * ANCHO // 4, 1.75 * ALTO // 3)],
        "Delantero": [(ANCHO // 4, 5 * ALTO // 6), (ANCHO // 2, 5 * ALTO // 6)]
    }

    pantalla.fill(NEGRO)
    pantalla.blit(campo_img, (0, 0))

    # Dibujar jugadores en las posiciones correspondientes
    for i, fila in enumerate(jugadores):
        for j, jugador in enumerate(fila):
            nombre = jugador
            imagen_url = imagenes_urls[i][j]
            if i == 0:
                posicion_base = posiciones_base["Portero"]
            elif i == 1:
                posicion_base = posiciones_base["Defensa"][j]
            elif i == 2:
                posicion_base = posiciones_base["Centrocampista"][j]
            else:
                # Si hay más delanteros que posiciones base, los distribuye equitativamente
                posiciones_delanteros = posiciones_base["Delantero"]
                num_delanteros = len(fila)
                espacio_entre_jugadores = ANCHO // (num_delanteros + 1)
                posicion_base = (espacio_entre_jugadores * (j + 1), posiciones_delanteros[0][1])
            dibujar_jugador(posicion_base, nombre,imagen_url)

    # Manejo de eventos


    pygame.display.flip()

def dibujar_alineacion_433(jugadores, imagenes_urls):
    # Definir posiciones base de los jugadores para la alineación 3-4-3
    posiciones_base = {
        "Portero": (ANCHO // 2, ALTO // 7),
        "Defensa": [(ANCHO // 4, ALTO // 3), (1.6 * ANCHO // 4, ALTO // 3),
                    (2.4 * ANCHO // 4, ALTO // 3),(3 * ANCHO // 4, ALTO // 3)],
        "Centrocampista": [(ANCHO // 4, 1.75 * ALTO // 3), (2 * ANCHO // 4, 1.75 * ALTO // 3),
                           (3 * ANCHO // 4, 1.75 * ALTO // 3)],
        "Delantero": [(ANCHO // 4, 5 * ALTO // 6), (ANCHO // 2, 5 * ALTO // 6), (3 * ANCHO // 4, 5 * ALTO // 6)]
    }

    pantalla.fill(NEGRO)
    pantalla.blit(campo_img, (0, 0))

    # Dibujar jugadores en las posiciones correspondientes
    for i, fila in enumerate(jugadores):
        for j, jugador in enumerate(fila):
            nombre = jugador
            imagen_url = imagenes_urls[i][j]
            if i == 0:
                posicion_base = posiciones_base["Portero"]
            elif i == 1:
                posicion_base = posiciones_base["Defensa"][j]
            elif i == 2:
                posicion_base = posiciones_base["Centrocampista"][j]
            else:
                # Si hay más delanteros que posiciones base, los distribuye equitativamente
                posiciones_delanteros = posiciones_base["Delantero"]
                num_delanteros = len(fila)
                espacio_entre_jugadores = ANCHO // (num_delanteros + 1)
                posicion_base = (espacio_entre_jugadores * (j + 1), posiciones_delanteros[0][1])
            dibujar_jugador(posicion_base, nombre,imagen_url)

    # Manejo de eventos


    pygame.display.flip()

def dibujar_alineacion_532(jugadores, imagenes_urls):
    # Definir posiciones base de los jugadores para la alineación 3-4-3
    posiciones_base = {
        "Portero": (ANCHO // 2, ALTO // 7),
        "Defensa": [(ANCHO // 4, ALTO // 3), (1.5 * ANCHO // 4, ALTO // 3), (2 * ANCHO // 4, ALTO // 3),
                    (2.5 * ANCHO // 4, ALTO // 3),(3 * ANCHO // 4, ALTO // 3)],
        "Centrocampista": [(ANCHO // 4, 1.75 * ALTO // 3), (2 * ANCHO // 4, 1.75 * ALTO // 3),
                           (3 * ANCHO // 4, 1.75 * ALTO // 3)],
        "Delantero": [(ANCHO // 4, 5 * ALTO // 6), (ANCHO // 2, 5 * ALTO // 6)]
    }

    pantalla.fill(NEGRO)
    pantalla.blit(campo_img, (0, 0))

    # Dibujar jugadores en las posiciones correspondientes
    for i, fila in enumerate(jugadores):
        for j, jugador in enumerate(fila):
            nombre = jugador
            imagen_url = imagenes_urls[i][j]
            if i == 0:
                posicion_base = posiciones_base["Portero"]
            elif i == 1:
                posicion_base = posiciones_base["Defensa"][j]
            elif i == 2:
                posicion_base = posiciones_base["Centrocampista"][j]
            else:
                # Si hay más delanteros que posiciones base, los distribuye equitativamente
                posiciones_delanteros = posiciones_base["Delantero"]
                num_delanteros = len(fila)
                espacio_entre_jugadores = ANCHO // (num_delanteros + 1)
                posicion_base = (espacio_entre_jugadores * (j + 1), posiciones_delanteros[0][1])
            dibujar_jugador(posicion_base, nombre,imagen_url)

    # Manejo de eventos


    pygame.display.flip()
# Ejemplo de uso
alineacion_343 = [["Kepa"],["Militao","Nacho","Rudiger"],["Modric","Kroos","Camavinga","Brahim"],["Vini","Joselu","Rodrygo"]]
imagenes_urls = [["https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"]]
alineacion_442 = [["Kepa"],["Militao","Nacho","Rudiger","Alaba"],["Modric","Kroos","Camavinga","Brahim"],["Vini","Rodrygo"]]
imagenes_urls442 = [["https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"]]
alineacion_541 = [["Kepa"],["Militao","Nacho","Rudiger","Alaba","Mendy"],["Modric","Kroos","Camavinga","Brahim"],["Joselu"]]
imagenes_urls541 = [["https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png"]]
alineacion_451 = [["Kepa"],["Militao","Nacho","Rudiger","Alaba"],["Modric","Kroos","Camavinga","Brahim","Valverde"],["Joselu"]]
imagenes_urls451 = [["https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png"]]
alineacion_352 = [["Kepa"],["Militao","Nacho","Rudiger"],["Modric","Kroos","Camavinga","Brahim","Valverde"],["Vini","Rodrygo"]]
imagenes_urls352 = [["https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/194750.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/194750.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"]]
alineacion_433 = [["Kepa"],["Militao","Nacho","Rudiger","Alaba"],["Modric","Kroos","Camavinga"],["Vini","Joselu","Rodrygo"]]
imagenes_urls433 = [["https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"]]
alineacion_532 = [["Kepa"],["Militao","Nacho","Rudiger","Alaba","Mendy"],["Modric","Kroos","Camavinga"],["Vini","Rodrygo"]]
imagenes_urls532 = [["https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"],["https://media.api-sports.io/football/players/20627.png","https://media.api-sports.io/football/players/20627.png"]]


##dibujar_alineacion_343(alineacion_343,imagenes_urls)
##dibujar_alineacion_442(alineacion_442,imagenes_urls442)
#dibujar_alineacion_541(alineacion_541,imagenes_urls541)
#dibujar_alineacion_451(alineacion_451,imagenes_urls451)
#dibujar_alineacion_352(alineacion_352,imagenes_urls352)
#dibujar_alineacion_433(alineacion_433,imagenes_urls433)
dibujar_alineacion_532(alineacion_532,imagenes_urls532)




