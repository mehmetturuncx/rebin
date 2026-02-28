from pathlib import Path
import json

TRASH_DIR = Path.home() / ".trash"
METADATA_FILE = TRASH_DIR / "metadata.json"

def ensure_trash():
    if not TRASH_DIR.exists():
        TRASH_DIR.mkdir(exist_ok=True,parents=True)
    
    if not METADATA_FILE.exists():
        with open(METADATA_FILE, "w", encoding="utf-8") as f:
            json.dump({},f, indent=4)

def load_metadata():
    ensure_trash()

    try:
        with open(METADATA_FILE,"r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}
    except FileNotFoundError:
        return {}

def save_metadata(data):
    with open(METADATA_FILE,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)

def generate_unique_name(path):
    destination = Path(path)
    new_destination = destination
    counter = 1    
    while new_destination.exists():
        new_destination = destination.parent / f"{destination.stem}_{counter}{destination.suffix}"
        counter += 1
    return new_destination
