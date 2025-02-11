import shutil

from pathlib import Path

from copy_static import copy_static
from generate_page import generate_page


def main() -> None:
    static_path = Path("static")
    public_path = Path("public")
    content = Path("content/index.md")
    template = Path("template.html")
    destiation = Path("public/index.html")

    if not static_path.exists():
        print("Static path is missing. Closing.")
        return

    if public_path.exists():
        print("Public path aready exists. Removing.")
        shutil.rmtree(public_path)

    copy_static(static_path, public_path)

    generate_page(content, template, destiation)


main()
