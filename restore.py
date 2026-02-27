from pathlib import Path
import shutil
import json

def restore(file_name):
    trash = Path.home() / ".trash"    
    metadata_file = trash / "metadata.json"
    source = trash / file_name

    if not source.exists():
        print("Dosya trash'de bulunamadı!")
        return
    if not metadata_file.exists():
        print("Metadata bulanamadı!")
        return

    with open(metadata_file,"r") as f:
        metadata = json.load(f)

    if file_name not in metadata:
        print("Bu dosya metadataya kayıtlı değildir.") 
    destination = Path(metadata[file_name]["original_path"])
    destination.parent.mkdir(parents=True, exist_ok=True)

    if destination.exists():
        counter = 1
        new_destination = destination

        while new_destination.exists():
            new_destination = destination.parent / f"{destination.stem}_{counter}{destination.suffix}"
            counter += 1

        destination = new_destination
    
    shutil.move(str(source),str(destination))

    del metadata[file_name]

    with open(metadata_file,"w") as f:
        json.dump(metadata,f,indent=4)
    
    print(f"{file_name} geri yüklendi")

if __name__ == "__main__":
    file_input = input("Trash deki dosya adı: ")
    restore(file_input)