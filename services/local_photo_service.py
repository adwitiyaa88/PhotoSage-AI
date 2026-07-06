from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".heic",
    ".gif",
    ".bmp",
    ".tiff",
    ".webp"
}


def scan_folder(folder_path):
    photos = []

    folder = Path(folder_path)

    for file in folder.rglob("*"):
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS:
            photos.append(file)

    return photos