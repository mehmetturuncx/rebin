from pathlib import Path

def list_trash():
    trash = Path.home() / ".trash"

    if not trash.exists():
        print("trash klasörü yok")
        return
    
    items = list(trash.iterdir())

    if not items:
        print("trash boş")
        return
    
    for item in items:
        type_info = "Dosya" if item.is_file() else "Klasör"
        size = item.stat().st_size
        print(f"{item.name} | {type_info} | {size} bytes")

if __name__ == "__main__":
    list_trash()