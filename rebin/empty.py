from pathlib import Path
import shutil
import rebin.utils as utils

def empty_trash():
    utils.ensure_trash()
    metadata = utils.load_metadata()

    if not metadata:
        print("Trash is already empty")
        return

    for file_name in list(metadata.keys()):
        trash_file = utils.TRASH_DIR / file_name
        try:
            if trash_file.is_file():
                trash_file.unlink() 
            elif trash_file.is_dir():
                shutil.rmtree(trash_file) 
            print(f"{file_name} deleted")
        except Exception as e:
            print(f"Failed to delete {file_name}: {e}")

        del metadata[file_name]

    utils.save_metadata(metadata)
    print("Trash emptied completely")