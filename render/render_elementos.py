import pygame
from datos.constantes import HEIGHT, WIDTH

LOGO = pygame.image.load('assets/logo.png')
LOGO = pygame.transform.scale(LOGO, (500, 500))

FONDO = pygame.image.load('assets/pokemonfondo.jpg')
FONDO = pygame.transform.scale(FONDO, (WIDTH, HEIGHT))

FONDO_CREDITOS = pygame.image.load('assets/fondocre.jpg')
FONDO_CREDITOS = pygame.transform.scale(FONDO_CREDITOS, (WIDTH, HEIGHT))

FONDO_PLAY = pygame.image.load('assets/fondojugar.jpg')
FONDO_PLAY = pygame.transform.scale(FONDO_PLAY, (WIDTH, HEIGHT))

# ENCAPSULAMIENTO

def logo_juego():
    return LOGO

def fondo_menu():
    return FONDO

def fondo_creditos():
    return FONDO_CREDITOS

def fondo_play():
    return FONDO_PLAY

# --- BOTÓN RECTÁNGULO ---
def crear_boton_rect(superficie, x, y, ancho, alto, texto, color_fondo, color_texto):
    fuente = pygame.font.Font(None, 40)
    rectangulo = pygame.Rect(x, y, ancho, alto)

    pygame.draw.rect(superficie, color_fondo, rectangulo, border_radius=10)
    pygame.draw.rect(superficie, (255, 255, 255), rectangulo, width=2, border_radius=10) # BORDES

    texto_img = fuente.render(texto, True, color_texto)
    texto_x = x + (ancho - texto_img.get_width()) // 2
    texto_y = y + (alto - texto_img.get_height()) // 2

    superficie.blit(texto_img, (texto_x, texto_y))

    return rectangulo


