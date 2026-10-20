from src.logsgenerator.registry import load_generators
from src.gui.window import run

if __name__ == '__main__':
    run(load_generators())