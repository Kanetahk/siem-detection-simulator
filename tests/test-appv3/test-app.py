# note: The .json file for this test has been deleted to avoid the risk of it overwriting the loader's .json loader, also, 

import json; from pathlib import Path

GENERATORS_DIR = Path(__file__).parent / "tests" / "test-app-json"

def load_generators():
    generators = {}
    for gerators_file in sorted(GENERATORS_DIR.glob("*/generators.json")):
        with open(gerators_file, encoding="utf-8") as g:
            generators[data["name"]] = data
        return generators

GENERATORS = load_generators()