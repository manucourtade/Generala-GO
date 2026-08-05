import pygame

from datos.constantes import HEIGHT, WIDTH
from datos.rutas import resource_path

_imagenes = {}


def cargar_imagen(nombre_archivo, tamanio):
    clave = (nombre_archivo, tamanio)
    if clave not in _imagenes:
        imagen = pygame.image.load(resource_path(f'assets/{nombre_archivo}')).convert_alpha()
        _imagenes[clave] = pygame.transform.scale(imagen, tamanio)
    return _imagenes[clave]


def logo_juego():
    return cargar_imagen('logo.png', (500, 500))


def fondo_menu():
    return cargar_imagen('pokemonfondo.jpg', (WIDTH, HEIGHT))


def fondo_creditos():
    return cargar_imagen('fondocre.jpg', (WIDTH, HEIGHT))


def fondo_play():
    return cargar_imagen('fondojugar.jpg', (WIDTH, HEIGHT))


def crear_boton_rect(superficie, x, y, ancho, alto, texto, color_fondo, color_texto):
    fuente = pygame.font.Font(None, 40)
    rectangulo = pygame.Rect(x, y, ancho, alto)

    pygame.draw.rect(superficie, color_fondo, rectangulo, border_radius=10)
    pygame.draw.rect(superficie, (255, 255, 255), rectangulo, width=2, border_radius=10)

    texto_img = fuente.render(texto, True, color_texto)
    texto_x = x + (ancho - texto_img.get_width()) // 2
    texto_y = y + (alto - texto_img.get_height()) // 2

    superficie.blit(texto_img, (texto_x, texto_y))
    return rectangulo
