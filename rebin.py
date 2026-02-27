import argparse
from delete import delete_file
from restore import restore
from list import list_trash

def main():
    parser = argparse.ArgumentParser(description="Rebin Terminal Trash Tool")
    subparsers = parser.add_subparsers(dest="command")

    dp = subparsers.add_parser("delete")
    dp.add_argument("path", help="Silinecek dosya yolu")

    rp = subparsers.add_parser("restore")
    rp.add_argument("name", help="Trash'teki dosya adı")

    lp = subparsers.add_parser("list", help="Trash içeriğini listele")

    args = parser.parse_args()

    if args.command == "delete":
        delete_file(args.path)
    elif args.command == "restore":
        restore(args.name)
    elif args.command == "list":
        list_trash()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()