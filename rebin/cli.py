import sys
from .delete import delete_file
from .restore import restore
from .list import list_trash
from .empty import empty_trash  # Bu dosyayı az önce yaptığımız gibi kaydet

def print_help():
    print("Rebin - Terminal Trash Tool")
    print("Kullanım:")
    print("  python3 rebin.py delete <dosya>   -> Dosyayı trash'e taşı")
    print("  python3 rebin.py restore <dosya>  -> Trash'ten geri yükle")
    print("  python3 rebin.py list             -> Trash içeriğini listele")
    print("  python3 rebin.py empty            -> Çöp kutusunu tamamen boşalt")

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()

    if command == "delete" and len(sys.argv) == 3:
        delete_file(sys.argv[2])
    elif command == "restore" and len(sys.argv) == 3:
        restore(sys.argv[2])
    elif command == "list":
        list_trash()
    elif command == "empty":
        empty_trash()
    else:
        print_help()
