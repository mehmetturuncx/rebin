from pathlib import Path
import shutil
import utils

def restore(file_name):
    utils.ensure_trash()
    metadata = utils.load_metadata()

    trash_file_path = utils.TRASH_DIR / file_name
    if not trash_file_path.exists():
        print("Trash dosyası bulunamadı!")
        return

    if file_name not in metadata:
        print("Dosya bulunamadı!")
        return

    original_path = Path(metadata[file_name]["original_path"])
    restore_path = utils.generate_unique_name(original_path)

    restore_path.parent.mkdir(exist_ok=True,parents=True)
    shutil.move(str(trash_file_path),restore_path)    

    del metadata[file_name]
    utils.save_metadata(metadata)

    print(f"{file_name} geri yüklendi -> {restore_path}")


if __name__ == "__main__":
    file_input = input("Trash deki dosya adı: ")
    restore(file_input)