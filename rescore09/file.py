from pathlib import Path
import shutil

def createdir(path):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p

def list_files(path, pattern="*"):
    return list(Path(path).glob(pattern))

def copy_file(src, dest):
    return shutil.copy(Path(src), Path(dest))

def move_file(src, dest):
    return shutil.move(Path(src), Path(dest))

def delete_file(path):
    p = Path(path)
    if p.exists():
        p.unlink()

def read_file(path):
    return Path(path).read_text()

def write_file(path, data):
    Path(path).write_text(data)
