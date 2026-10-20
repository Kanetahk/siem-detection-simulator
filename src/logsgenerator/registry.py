import json
from pathlib import Path

GENERATORS_DIR = Path(__file__).parent

def load_generators():
    generators = {}
    for info_file in sorted(GENERATORS_DIR.glob("*/info.json")):
        try:
            with open(info_file, encoding="utf-8") as f:
                data = json.load(f)
            generators[data["name"]] = data
        except (json.JSONDecodeError, KeyError) as erro:
            print(f"Skipping {info_file.parent.name}: {type(erro).__name__}")
    return generators