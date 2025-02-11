import shutil

from pathlib import Path


def copy_static(source: Path, destination: Path) -> None:
    if not destination.exists():
        destination.mkdir()

    for item in source.iterdir():
        dest = destination / item.name
        print(f"Copying {item} to {dest}")

        if item.is_file():
            shutil.copy(item, dest)
        else:
            copy_static(item, dest)
