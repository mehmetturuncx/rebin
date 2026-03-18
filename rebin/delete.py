import json
from pathlib import Path
from datetime import datetime
import shutil
import rebin.utils as utils


def delete_file(file_path):
    source = Path(file_path)
    
    if not source.exists():
        print("File not found")
        return

    utils.ensure_trash()

    original_path = str(source.resolve())
    file_size = source.stat().st_size
    file_type = source.suffix if source.suffix else "unknown"

    contents = None
    if source.is_dir():
        file_size = sum(f.stat().st_size for f in source.rglob('*') if f.is_file())
        file_type = "folder"
        contents = []
        for f in sorted(source.rglob('*')):
            if f.is_file():
                rel = f.relative_to(source)
                contents.append({
                    "name": str(rel),
                    "size": f.stat().st_size,
                    "type": f.suffix if f.suffix else "unknown"
                })

    trash_name = utils.generate_unique_name(utils.TRASH_DIR / source.name)
    shutil.move(str(source), trash_name)
    
    
    metadata = utils.load_metadata()
    metadata[trash_name.name] = {
        "original_path": original_path,
        "deleted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "size": int(file_size),
        "type": file_type
    }

    if contents is not None:
        metadata[trash_name.name]["contents"] = contents

    utils.save_metadata(metadata)

    print(f"{trash_name.name} moved to trash!")

if __name__ == "__main__":
    path_input = input("File to delete: ")
    delete_file(path_input)