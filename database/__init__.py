from os import path

def get_dir() -> str:
    basedir = path.dirname(__file__)

    return basedir