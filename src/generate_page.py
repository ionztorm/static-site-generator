from pathlib import Path

from block_markdown import markdown_to_html


def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#") and line[:2].count("#") == 1:
            return line.lstrip("#").strip()
    raise ValueError("The markdow is missing a main header.")


def generate_page(source: Path, template: Path, dest: Path) -> None:
    print(f"Generating page from {source} to {dest} using {template}")

    if not source.exists():
        raise ValueError(f"{source} does not exist.")

    if not template.exists():
        raise ValueError(f"{template} does not exist.")

    markdown = source.read_text()
    template_html = template.read_text()
    title = extract_title(markdown)
    content_html = markdown_to_html(markdown).to_html()
    template_html = template_html.replace("{{ Title }}", title)
    template_html = template_html.replace("{{ Content }}", content_html)

    if not dest.exists():
        dest.touch()

    with dest.open("w") as file:
        _ = file.write(template_html)


def generate_pages_recursively(source: Path, template: Path, dest: Path) -> None:
    for item in source.iterdir():
        if item.is_file() and item.suffix in {".md", ".markdown"}:
            print(f"Converting {item}")
            generate_page(item, template, dest / item.with_suffix(".html").name)
        else:
            print(f"Checking directory {item}")
            new_dest = dest / item.name
            new_dest.mkdir()
            generate_pages_recursively(item, template, new_dest)
