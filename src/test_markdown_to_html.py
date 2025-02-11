import unittest

from block_markdown import markdown_to_html

paragrapth_test_md = """
This is a paragraph
with **bold** and
*italic* text.
"""

quote_test = """
> This is a quote
> on multiple lines
"""

list_test = """
* this is an
* unordered list

1. this is an
2. ordered list
"""

page_test = """
# Page test

## Paragraph Elements

### Text features

This paragraph has **bold text**, *italic text*, a `code block`.

### Images

![an image](https://www.boot.dev/boots.jpg)

### Links

[to boot dev](https://www.boot.dev)

## Code

```
The code block is for code.
```

## Quotes

> quotes should all start
> with this arrow.
> Even new lines.

## Lists

* Unordered lists
* start witn ah asterisk
* for each point

1. ordered lists
2. must start with a digit followed by a .
3. The digits must be in order, starting from 1.

"""


codeblock_test_md = "```This is a codetblock.```"


class TestMarkdownToHTML(unittest.TestCase):
    def test_pararaph(self) -> None:
        md = "This is a paragraph with **bold** and *italic* text."
        node = markdown_to_html(md)
        html = node.to_html()
        expected = "<div><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p></div>"
        self.assertEqual(html, expected)

    def test_paragraph_new_lines(self) -> None:
        node = markdown_to_html(paragrapth_test_md)
        html = node.to_html()
        expected = "<div><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p></div>"
        self.assertEqual(html, expected)

    def test_codeblock(self) -> None:
        md = "```This is a code block.```"
        node = markdown_to_html(md)
        html = node.to_html()
        expected = "<div><pre><code>This is a code block.</code></pre></div>"
        self.assertEqual(html, expected)

    def test_headers_1(self) -> None:
        md = "# Heading1"
        node = markdown_to_html(md)
        html = node.to_html()
        expected = "<div><h1>Heading1</h1></div>"
        self.assertEqual(html, expected)

    def test_headers_3(self) -> None:
        md = "### Heading3"
        node = markdown_to_html(md)
        html = node.to_html()
        expected = "<div><h3>Heading3</h3></div>"
        self.assertEqual(html, expected)

    def test_headers_6(self) -> None:
        md = "###### Heading6"
        node = markdown_to_html(md)
        html = node.to_html()
        expected = "<div><h6>Heading6</h6></div>"
        self.assertEqual(html, expected)

    def test_quoteblock(self) -> None:
        node = markdown_to_html(quote_test)
        html = node.to_html()
        expected = "<div><blockquote>This is a quote<br>on multiple lines</blockquote></div>"
        self.assertEqual(html, expected)

    def test_lists(self) -> None:
        node = markdown_to_html(list_test)
        html = node.to_html()
        expected = (
            "<div><ul><li>this is an</li><li>unordered list</li></ul>"
            + "<ol><li>this is an</li><li>ordered list</li></ol></div>"
        )
        self.assertEqual(html, expected)

    def test_page(self) -> None:
        node = markdown_to_html(page_test)
        html = node.to_html()
        expected = (
            "<div>"
            + "<h1>Page test</h1>"
            + "<h2>Paragraph Elements</h2>"
            + "<h3>Text features</h3>"
            + "<p>This paragraph has <b>bold text</b>, <i>italic text</i>, a <code>code block</code>.</p>"
            + "<h3>Images</h3>"
            + '<img src="https://www.boot.dev/boots.jpg" alt="an image">'
            + "<h3>Links</h3>"
            + '<a href="https://www.boot.dev">to boot dev</a>'
            + "<h2>Code</h2>"
            + "<pre><code>The code block is for code.</code></pre>"
            + "<h2>Quotes</h2>"
            + "<blockquote>quotes should all start<br>with this arrow.<br>Even new lines.</blockquote>"
            + "<h2>Lists</h2>"
            + "<ul>"
            + "<li>Unordered lists</li>"
            + "<li>start witn ah asterisk</li>"
            + "<li>for each point</li>"
            + "</ul>"
            + "<ol>"
            + "<li>ordered lists</li>"
            + "<li>must start with a digit followed by a .</li>"
            + "<li>The digits must be in order, starting from 1.</li>"
            + "</ol>"
            + "</div>"
        )
        self.maxDiff: int | None = None
        self.assertEqual(html, expected)


if __name__ == "__main__":
    _ = unittest.main()
