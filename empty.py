from pathlib import Path
import shutil
import utils

def empty_trash():
    utils.ensure_trash()
    metadata = utils.load_metadata()

    if not metadata:
        print("Çöp kutusu zaten boş")
        return

    for file_name in list(metadata.keys()):
        trash_file = utils.TRASH_DIR / file_name
        try:
            if trash_file.is_file():
                trash_file.unlink() 
            elif trash_file.is_dir():
                shutil.rmtree(trash_file) 
            print(f"{file_name} silindi")
        except Exception as e:
            print(f"{file_name} silinemedi: {e}")

        del metadata[file_name]

    utils.save_metadata(metadata)
    print("Çöp kutusu tamamen boşaltıldı")