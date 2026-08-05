import csv
import json
import os
from json import JSONDecodeError

from datos.rutas import writable_path

archivo = writable_path('estadisticas/historial.csv')
archivo_json = writable_path('estadisticas/niveles.json')

SIMBOLOS = {
    '1': 'Pikachu',
    '2': 'Bulbasur',
    '3': 'Charmander',
    '4': 'Squirtle',
    '5': 'Snorlax',
    '6': 'Gengar',
    'escalera': '(20 pts) Secuencia 1-2-3-4-5 o 2-3-4-5-6',
    'full': '(30 pts) Tres dados iguales y otros dos iguales',
    'poker': '(40 pts) Cuatro dados iguales',
    'generala': '(50 pts) Cinco dados iguales. Si es servida, gana el juego automaticamente y suma 100 puntos',
}


def realizar_registro(nombre_archivo, nombre, puntos):
    existe = os.path.exists(nombre_archivo)

    with open(nombre_archivo, 'a', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        if not existe:
            escritor.writerow(['nombre', 'puntaje'])
        escritor.writerow([nombre.strip(), puntos])


def leer_archivo_csv(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []

    puntajes = []
    with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            puntos = fila.get('puntaje', '')
            nombre = fila.get('nombre', '')
            if puntos.isdigit():
                puntajes.append((nombre, int(puntos)))

    return puntajes


def ordenar_10_mejores(nombre_archivo):
    puntajes = sorted(leer_archivo_csv(nombre_archivo), key=lambda item: item[1], reverse=True)
    if not puntajes:
        return

    print()
    print('=' * 30)
    print('        TOP 10 JUGADORES')
    print('=' * 30)
    for nombre, puntos in puntajes[:10]:
        print(f'   {nombre:<10}|    {puntos:>7}')
    print('=' * 30)


def json_tematicas(nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as niveles:
        json.dump([SIMBOLOS], niveles, indent=4, ensure_ascii=False)


def asegurar_archivo_tematicas():
    if not os.path.exists(archivo_json) or os.path.getsize(archivo_json) == 0:
        json_tematicas(archivo_json)


def json_background(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        json_tematicas(nombre_archivo)

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as niveles:
            return json.load(niveles)
    except (JSONDecodeError, IndexError):
        json_tematicas(nombre_archivo)
        with open(nombre_archivo, 'r', encoding='utf-8') as niveles:
            return json.load(niveles)


def mostrar_archivo_json():
    pokemones_categoria = json_background(archivo_json)
    if not pokemones_categoria:
        return

    simbolos = pokemones_categoria[0]
    for valor, simbolo in simbolos.items():
        print(f'Valor: {valor} - Simbolo {simbolo}')
