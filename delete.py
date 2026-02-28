import json
from pathlib import Path
from datetime import datetime
import shutil
import utils


def delete_file(file_path):
    source = Path(file_path)
    
    if not source.exists():
        print("Dosya bulunamadı")
        return

    utils.ensure_trash()

    original_path = str(source.resolve())
    file_size = source.stat().st_size
    file_type = source.suffix if source.suffix else "unknown"

    trash_name = utils.generate_unique_name(utils.TRASH_DIR / source.name)
    shutil.move(str(source), trash_name)
    
    
    metadata = utils.load_metadata()
    metadata[trash_name.name] = {
        "original_path": original_path,
        "deleted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "size": int(file_size),
        "type": file_type
    }

    utils.save_metadata(metadata)

    print(f"{trash_name.name} trash'e taşındı!")

if __name__ == "__main__":
    path_input = input("Silinecek dosya: ")
    delete_file(path_input)