from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".heic",
    ".gif",
    ".bmp",
    ".tiff",
    ".webp",
}


def find_library():
    library = Path.home() / "Pictures" / "Photos Library.photoslibrary"

    if library.exists():
        return library

    return None


def get_original_photos():
    library = find_library()

    if library is None:
        return []

    originals = library / "originals"

    photos = []

    for file in originals.rglob("*"):
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS:
            photos.append(file)

    return photos