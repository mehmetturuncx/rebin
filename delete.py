import json
from pathlib import Path
from datetime import datetime
import shutil

def delete_file(file_path):
    source = Path(file_path)
    trash = Path.home() / ".trash"
    trash.mkdir(exist_ok=True)
    metadata_file = trash / "metadata.json"

    if not source.exists():
        print("Dosya bulunamadı")
        return


    if metadata_file.exists():
        with open(metadata_file, "r") as f:
            metadata = json.load(f)
    else:
        metadata = {}


    destination = trash / source.name
    if destination.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        destination = trash / f"{source.stem}_{timestamp}{source.suffix}"


    metadata[destination.name] = {
        "original_path": str(source.resolve()),
        "deleted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(metadata_file, "w") as f:
        json.dump(metadata, f, indent=4)

    shutil.move(str(source), destination)
    print(f"{source.name} trash'e taşındı")

if __name__ == "__main__":
    path_input = input("Silinecek dosya: ")
    delete_file(path_input)