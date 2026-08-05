from pathlib import Path
import sys


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parents[1]
    return str(base_path / relative_path)


def writable_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = Path(sys.executable).resolve().parent
    else:
        base_path = Path(__file__).resolve().parents[1]

    path = base_path / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    return str(path)
