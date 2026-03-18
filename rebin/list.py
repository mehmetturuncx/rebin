from pathlib import Path
import rebin.utils as utils

def format_size(size):
    if size < 1024:
        return f"{size} B"
    elif size < 1024**2:
        kb = size / 1024
        return f"{round(kb, 1)} KB"
    elif size < 1024**3:
        mb = size / (1024**2)
        return f"{round(mb, 1)} MB"
    else:
        gb = size / (1024**3)
        return f"{round(gb, 1)} GB"

REBIN_ASCII = [
"██████╗ ███████╗██████╗ ██╗███╗   ██╗",
"██╔══██╗██╔════╝██╔══██╗██║████╗  ██║",
"██████╔╝█████╗  ██████╔╝██║██╔██╗ ██║",
"██╔══██╗██╔══╝  ██╔══██╗██║██║╚██╗██║",
"██║  ██║███████╗██████╔╝██║██║ ╚████║",
"╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═══╝"
]

EMPTY_TRASH_ASCII = [
"      ______",
"     /      \\",
"    |        |",
"    |        |",
"    |        |",
"    |________|"
]

FULL_TRASH_ASCII = [
"      ______",
"     /      \\",
"    | ████   |",
"    | ████   |",
"    | ████   |",
"    |________|"
]

def list_trash():
    metadata = utils.load_metadata()
    
    ascii_to_show = FULL_TRASH_ASCII if metadata else EMPTY_TRASH_ASCII
    for head, box in zip(REBIN_ASCII, ascii_to_show):
        print(f"{head}   {box}")
    
    if not metadata:
        print("\nTrash is empty")
        return
    
    print(f"{'File Name':<25} {'Size':>10} {'Type':<8} {'Deleted At':<20}")
    print("-" * 65)
    
    for name, info in metadata.items():
        size = format_size(info["size"])
        file_type = info["type"]
        date = info["deleted_at"]
        print(f"{name:<25} {size:>10} {file_type:<8} {date:<20}")
        if "contents" in info:
            items = info["contents"]
            for i, item in enumerate(items):
                item_size = format_size(item["size"])
                prefix = "└─" if i == len(items) - 1 else "├─"
                print(f"  {prefix} {item['name']:<21} {item_size:>10} {item['type']:<8}")

if __name__ == "__main__":
    list_trash()