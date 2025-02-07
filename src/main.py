"""Static Site Generator.

This static site generator was built for the Bootdev ssg project.

How the SSG Works:
    The vast majority of our coding will happen in the src/ directory because almost all of the work
    is done in steps 2 and 3 above. Here's a rough outline of what the final program will do when it
    runs:

    - Delete everything in the /public directory.
    - Copy any static assets (HTML template, images, CSS, etc.) to the /public directory.
    - Generate an HTML file for each Markdown file in the /content directory. For each MD file:
    - Open the file and read its contents.
    - Split the markdown into “blocks” (e.g. paragraphs, headings, lists, etc.).
    - Convert each block into a tree of HTMLNode objects. For inline elements (bold text, links,
        etc.) we will convert:
    - Raw markdown -> TextNode -> HTMLNode
    - Join all the HTMLNode blocks under one large parent HTMLNode for the pages.
    - Use a recursive to_html() method to convert the HTMLNode and all its nested nodes to a giant
    HTML string and inject it in the HTML template.
    - Write the full HTML string to a file for that page in the /public directory.

"""

from textnode import TextNode, TextType


def main() -> None:
    test_text_node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
    print(test_text_node)


main()
