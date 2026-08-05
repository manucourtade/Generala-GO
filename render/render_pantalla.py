import pygame
from datos.constantes import WIDTH, HEIGHT
from render.render_elementos import logo_juego, fondo_menu, crear_boton_rect, fondo_creditos
from estadisticas.archivo_json_csv import leer_archivo_csv, archivo
from datos.rutas import resource_path

COLOR_VERDE = (15, 112, 1)
COLOR_BLANCO = (255, 255, 255)

def pantalla_principal(pantalla):
    logo = logo_juego()
    fondo = fondo_menu()
    
    ancho_logo = logo.get_width()
    x_logo = (WIDTH - ancho_logo) // 2
    y_logo = 10

    etiquetas = ["Jugar", "Créditos", "Estadísticas", "Salir"]
    claves = ["jugar", "creditos", "estadisticas", "salir"]

    ANCHO_BOTON = 185
    ALTO_BOTON = 60
    ESPACIO = 40

    total_ancho_botones = (ANCHO_BOTON * 5) + (ESPACIO * 4)
    inicio_botones_x = (WIDTH - total_ancho_botones) // 2
    y_botones = y_logo + logo.get_height() - 20

    botones = {}   # ← AHORA ES UN DICCIONARIO

    pantalla.blit(fondo, (0, 0))
    pantalla.blit(logo, (x_logo, y_logo))

    for i, texto in enumerate(etiquetas):
        x = inicio_botones_x + i * (ANCHO_BOTON + ESPACIO * 2.8)

        rect = crear_boton_rect(
            pantalla,
            x, y_botones,
            ANCHO_BOTON,
            ALTO_BOTON,
            texto,
            COLOR_VERDE,
            COLOR_BLANCO
        )

        botones[claves[i]] = rect   # ← SE GUARDA COMO DICCIONARIO

    return botones

def volver_menu(pantalla):
    fuente_esc = pygame.font.Font(None, 35)
    texto_esc = fuente_esc.render("Presione ESC para volver al menu", True, (255, 255, 255))
    pantalla.blit(texto_esc, (20, 20))

    # Detectar la tecla ESC (sin consumir eventos)
    teclas = pygame.key.get_pressed() # Devuelve lista, estado de tecla presionada
    if teclas[pygame.K_ESCAPE]:
        return True

    return False


def pantalla_creditos(pantalla):
    fondo2 = fondo_creditos()
    pantalla.blit(fondo2, (0, 0))
    tam_datos = 45
    fuente = pygame.font.Font(None, 65)
    texto = fuente.render("CREDITOS", True, (0, 0, 0)) 
    pantalla.blit(texto, (500, 80))

    fuente_autores = pygame.font.Font(None, tam_datos)
    txt_autores = fuente_autores.render('Autores: Manuel Courtade, Maximo Savall', True, (0, 0, 0))
    pantalla.blit(txt_autores, (120, 190))

    fuente_fecha = pygame.font.Font(None, tam_datos)
    txt_fecha = fuente_fecha.render('Fecha: 31/10/2025', True, (0, 0, 0))
    pantalla.blit(txt_fecha, (120, 265))

    fuente_materia = pygame.font.Font(None, tam_datos)
    txt_materia = fuente_materia.render('Materia: Programacion I', True, (0, 0, 0))
    pantalla.blit(txt_materia, (120, 340))

    fuente_docentes = pygame.font.Font(None, tam_datos)
    txt_docentes = fuente_docentes.render('Docentes: Martin Alejandro Garcia - Veronica Carbonari', True, (0, 0, 0))
    pantalla.blit(txt_docentes, (120, 415))

    fuente_carrera = pygame.font.Font(None, tam_datos)
    txt_carrera = fuente_carrera.render('Carrera: Tecnicatura en programacion', True, (0, 0, 0))
    pantalla.blit(txt_carrera, (120, 490))

    fuente_contacto = pygame.font.Font(None, tam_datos)
    txt_contacto = fuente_contacto.render('Contacto: courtademanuel@outlook.es - savallmaximo@gmail.com', True, (0, 0, 0))
    pantalla.blit(txt_contacto, (120, 565))

    volver_menu(pantalla)

def pantalla_estadisticas(pantalla):
    fondo_stats = pygame.image.load(resource_path('assets/fondo_stats.png'))
    fondo_stats = pygame.transform.scale(fondo_stats, (WIDTH, HEIGHT))
    pantalla.blit(fondo_stats, (0, 0))

    # --- TÍTULOS ---
    fuente_titulo = pygame.font.Font(None, 70)
    txt_nombre = fuente_titulo.render('NOMBRE', True, (0, 0, 0))
    txt_puntaje = fuente_titulo.render('PUNTAJE', True, (0, 0, 0))
    pantalla.blit(txt_nombre, (230, 100))
    pantalla.blit(txt_puntaje, (750, 100))

    # --- LÍNEAS ---
    pygame.draw.line(pantalla, (0, 0, 0), (150, 170), (1130, 170), 4)  # Horizontal
    pygame.draw.line(pantalla, (0, 0, 0), (150, 85), (1130, 85), 4)  # Horizontal
    pygame.draw.line(pantalla, (0, 0, 0), (600, 85), (600, 690), 4)   # Vertical
    pygame.draw.line(pantalla, (0, 0, 0), (150, 85), (150, 690), 4)   # Vertical, IZQ
    pygame.draw.line(pantalla, (0, 0, 0), (1130, 85), (1130, 690), 4)   # Vertical, DER

    # --- LEER CSV ---
    puntajes = leer_archivo_csv(archivo)

    if not puntajes:
        return

    n = len(puntajes)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if puntajes[j][1] < puntajes[j + 1][1]:
                puntajes[j], puntajes[j + 1] = puntajes[j + 1], puntajes[j]

    # --- MOSTRAR TOP 10 ---
    fuente_fila = pygame.font.Font(None, 55)
    y_fila = 200

    limite = 10
    if len(puntajes) < 10:
        limite = len(puntajes)

    for i in range(limite):
        nombre = puntajes[i][0]
        puntos = puntajes[i][1]

        txt_nombre_fila = fuente_fila.render(nombre.title(), True, (0, 0, 255))
        txt_puntaje_fila = fuente_fila.render(str(puntos), True, (255 ,0 ,0 ))

        pantalla.blit(txt_nombre_fila, (230, y_fila))
        pantalla.blit(txt_puntaje_fila, (830, y_fila))

        y_fila += 50
        pygame.draw.line(pantalla, (0, 0, 0), (150, y_fila - 10), (1130, y_fila - 10), 4)


        if volver_menu(pantalla):
            return "menu"

