import json
import os
from json import JSONDecodeError

from datos.rutas import writable_path

json_archive = writable_path('datos/set_up.json')

config__ = {
    'default': {
        'ventana': {'w': 1280, 'h': 720, 'titulo': 'Generala GO!'},
        'audio': {'vol': 0.01},
        'colores': {
            'fondo': [196, 101, 86],
            'primario': [],
            'secundario': [255, 215, 0],
            'texto_claro': [255, 255, 255],
            'texto_oscuro': [0, 0, 0]
        }
    }
}


def guardar_datos(archivo, config):
    with open(archivo, 'w', encoding='utf-8') as datos:
        json.dump(config, datos, indent=4, ensure_ascii=False)


def cargar_datos():
    if not os.path.exists(json_archive) or os.path.getsize(json_archive) == 0:
        guardar_datos(json_archive, config__)
        return config__

    try:
        with open(json_archive, 'r', encoding='utf-8') as datos:
            datos_cargados = json.load(datos)
    except JSONDecodeError:
        guardar_datos(json_archive, config__)
        return config__

    if 'default' not in datos_cargados:
        guardar_datos(json_archive, config__)
        return config__

    return datos_cargados
