import sys
from .delete import delete_file
from .restore import restore
from .list import list_trash
from .empty import empty_trash
from .remove import remove_file

def print_help():
    print("Rebin - Terminal Trash Tool")
    print("Usage:")
    print("  rebin delete <file>    -> Move file to trash")
    print("  rebin restore <file>   -> Restore file from trash")
    print("  rebin list             -> List trash contents")
    print("  rebin empty            -> Empty the trash completely")
    print("  rebin remove <file>    -> Permanently delete a file from trash")

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
    elif command == "remove" and len(sys.argv) == 3:
        remove_file(sys.argv[2])
    else:
        print_help()
