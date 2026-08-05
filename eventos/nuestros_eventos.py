import pygame

from audio.musica import EFECTO_CLICK, cargar_efecto, reproducir_efecto

_efecto_click = None


def reproducir_click():
    global _efecto_click
    if _efecto_click is None:
        _efecto_click = cargar_efecto(EFECTO_CLICK)
    reproducir_efecto(_efecto_click)


def gestionar_eventos(evento, pantalla_actual, botones):
    if pantalla_actual == 'menu' and evento.type == pygame.MOUSEBUTTONDOWN and botones:
        acciones = {
            'jugar': 'jugar',
            'creditos': 'creditos',
            'estadisticas': 'estadisticas',
            'salir': 'salir',
        }

        for clave, pantalla_destino in acciones.items():
            if botones[clave].collidepoint(evento.pos):
                reproducir_click()
                return pantalla_destino

    if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
        return 'menu'

    return pantalla_actual
