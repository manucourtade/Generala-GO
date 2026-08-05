# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules


local_packages = [
    'audio',
    'creditos',
    'datos',
    'estadisticas',
    'eventos',
    'juego',
    'puntaje',
    'render',
    'render_logica',
]

hiddenimports = []
for package in local_packages:
    hiddenimports += collect_submodules(package)

datas = [
    ('assets', 'assets'),
    ('datos/set_up.json', 'datos'),
    ('estadisticas/niveles.json', 'estadisticas'),
]


a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
