# Generala GO!

Juego de Generala con interfaz grafica hecho en Python y Pygame.

## Requisitos

- Python 3.10, 3.11 o 3.12.
- No usar Python 3.13 o superior para este proyecto.
- Git, si queres descargarlo desde un repositorio.

## Descargar el proyecto

Si tenes Git instalado:

```bash
git clone https://github.com/manucourtade/Generala-GO.git
cd Generala-GO
```

Si descargaste un `.zip`, descomprimilo y entra a la carpeta del proyecto:

```bash
cd Generala-GO
```

## Ejecutar desde el codigo fuente

Crea y activa un entorno virtual:

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bat
py -3 -m venv .venv
.venv\Scripts\activate.bat
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Ejecuta el juego:

```bash
python main.py
```

## Ejecutar el juego en Linux

Ya hay un ejecutable generado en:

```bash
dist/main
```

Para abrirlo desde terminal:

```bash
./dist/main
```

Si no tiene permisos de ejecucion:

```bash
chmod +x dist/main
./dist/main
```

## Generar el ejecutable de Linux

Desde la raiz del proyecto, con el entorno virtual activado:

```bash
pyinstaller main.spec
```

El ejecutable queda en:

```bash
dist/main
```

## Generar el ejecutable de Windows

PyInstaller debe ejecutarse en Windows para crear un `.exe` de Windows.

En Windows, entra al proyecto y ejecuta:

```bat
dist\crear_exe_windows.bat
```

El ejecutable queda en:

```txt
dist\main.exe
```

## Archivos importantes

- `main.py`: archivo principal del juego.
- `requirements.txt`: dependencias necesarias.
- `main.spec`: configuracion de PyInstaller.
- `assets/`: imagenes y sonidos del juego.
- `dist/main`: ejecutable de Linux.
- `dist/crear_exe_windows.bat`: script para generar el `.exe` desde Windows.

## Notas

El juego guarda archivos de configuracion y estadisticas junto al ejecutable cuando se corre desde `dist`. Por eso pueden aparecer carpetas como:

```txt
dist/datos
dist/estadisticas
```
