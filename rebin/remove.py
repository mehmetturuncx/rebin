from pathlib import Path
import utils

TRASH_DIR = Path.home() / ".rebin" / "trash"

def remove_file(filename):
    metadata = utils.load_metadata()

    if filename not in metadata:
        print("Dosya çöp kutusunda bulunamadı")
        return

    file_path = TRASH_DIR / filename

    if file_path.exists():
        file_path.unlink()

    del metadata[filename]
    utils.save_metadata(metadata)

    print(f"{filename} kalıcı olarak silindi.")