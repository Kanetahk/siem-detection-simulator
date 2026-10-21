import importlib
import json
from pathlib import Path

GENERATORS_DIR = Path(__file__).parent

def load_generators():
    generators = {}
    for info_file in sorted(GENERATORS_DIR.glob("*/info.json")):
        folder = info_file.parent.name
        try:
            with open(info_file, encoding="utf-8") as f:
                data = json.load(f)
            name = data["name"]
        except (json.JSONDecodeError, KeyError) as erro:
            print(f"Skipping {folder}: {type(erro).__name__}")
            continue
        try:
            module = importlib.import_module(f".{folder}.{folder}", package=__package__)
            data["generate"] = module.generate
        except (ModuleNotFoundError, AttributeError):
            data["generate"] = None
        generators[name] = data
    return generators