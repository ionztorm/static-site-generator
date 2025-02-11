# Static Site Generator

This project is a Static Site Generator (SSG) for converting Markdown content into HTML pages. It is designed to work with a specific directory structure and uses Python for processing the Markdown files and generating the HTML output.

## Table of Contents

- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Classes and Functions](#classes-and-functions)
- [Testing](#testing)

## Usage

To generate the static site, run the following command:

```sh
sh main.sh
```

This will execute the main.py script, which will copy static files and generate HTML pages from the Markdown content.

## Directory Structure

The project has the following directory structure:

```text
.gitignore
.vscode/
    settings.json
content/
    index.md
    majesty/
main.sh
public/
    images/
    index.css
    index.html
    majesty/
README.md
reference.md
src/
    block_markdown.py
    copy_static.py
    generate_page.py
    htmlnode.py
    inline_markdown.py
    main.py
    test_block_types.py
    test_extract_markdown_images.py
    test_extract_markdown_links.py
    test_generate_page.py
    test_htmlnode.py
    test_leafnode.py
    test_markdown_splitter.py
    test_markdown_to_html.py
    test_parentnode.py
    test_split_blocks.py
    test_split_by_images_and_links.py
    test_text_node_to_html_node.py
    test_text_to_textnode.py
    textnode.py
static/
    ...
template.html
test.sh
```

- content: Contains the Markdown files to be converted to HTML.
- public: The output directory for the generated HTML files and static assets.
- src: Contains the Python source code for the SSG.
- static: Contains static files like CSS and images.
- template.html: The HTML template used for generating the pages.

## Classes and Functions

The project uses several classes and functions to process Markdown and generate HTML. Here are some key components:

- **`block_markdown.py`**: Contains functions to handle block-level Markdown elements.
  - `split_blocks(text)`: Splits the Markdown text into block elements.
  - `parse_block(block)`: Parses a block element into an HTML node.

- **`copy_static.py`**: Contains functions to copy static files from the static directory to the public directory.
  - `copy_static_files()`: Copies static files.

- **`generate_page.py`**: Contains functions to generate HTML pages from Markdown content.
  - `generate_html(markdown_content)`: Converts Markdown content to HTML.

- **`htmlnode.py`**: Defines classes for representing HTML elements.
  - `HtmlNode(tag, attributes, children)`: Initializes an HTML node.
  - `to_html()`: Converts the HTML node to an HTML string.
  - `ParentNode(tag, attributes, children)`: Inherits from `HtmlNode`, represents a node with children.
  - `LeafNode(tag, attributes)`: Inherits from `HtmlNode`, represents a node without children.

- **`inline_markdown.py`**: Contains functions to handle inline Markdown elements.
  - `parse_inline(text)`: Parses inline Markdown elements into HTML.

- **`main.py`**: The main script that orchestrates the static site generation process.
  - `main()`: The main function that runs the SSG.

- **`textnode.py`**: Defines the `TextNode` class for representing text nodes in the HTML.
  - `TextNode(text)`: Initializes a text node.
  - `to_html()`: Converts the text node to an HTML string.

## Testing

To run the tests, execute the following command:

```sh
sh test.sh
```

This will run all the unit tests located in the src directory.
