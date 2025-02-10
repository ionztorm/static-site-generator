import unittest

from textnode import TextNode, TextType
from markdown_parser import text_to_textnode


class TestTextToTextnode(unittest.TestCase):
    def test_simple_string(self) -> None:
        text = "This is a simple string."
        expected = [TextNode("This is a simple string.", TextType.TEXT)]

        self.assertEqual(text_to_textnode(text), expected)

    def test_bold(self) -> None:
        text = "This is a simple string with a **bold** word."
        expected = [
            TextNode("This is a simple string with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word.", TextType.TEXT),
        ]

        self.assertEqual(text_to_textnode(text), expected)

    def test_italic(self) -> None:
        text = "This is a simple string with an *italic* word."
        expected = [
            TextNode("This is a simple string with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word.", TextType.TEXT),
        ]

        self.assertEqual(text_to_textnode(text), expected)

    def test_code(self) -> None:
        text = "This is a simple string with a `code` block."
        expected = [
            TextNode("This is a simple string with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" block.", TextType.TEXT),
        ]

        self.assertEqual(text_to_textnode(text), expected)

    def test_italic_before_bold(self) -> None:
        text = "This is a simple string with an *italic* word and a **bold** word."
        expected = [
            TextNode("This is a simple string with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word.", TextType.TEXT),
        ]

        self.assertEqual(text_to_textnode(text), expected)

    def test_code_befor_bold_before_italic(self) -> None:
        text = "This is a simple string with a `code block`, a **bold** word and an *italic* word."
        expected = [
            TextNode("This is a simple string with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(", a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word.", TextType.TEXT),
        ]

        self.assertEqual(text_to_textnode(text), expected)

    def test_all_with_links_and_images(self) -> None:
        text = (
            "This text has "
            + "an image of boots ![image of boots](https://www.boot.dev/boots.jpg)"
            + " and a **bold** word, a `code block` and an *italic* word. "
            + "It also has a link [to boot dev](https://www.boot.dev)."
        )
        expected = [
            TextNode("This text has an image of boots ", TextType.TEXT),
            TextNode("image of boots", TextType.IMAGE, "https://www.boot.dev/boots.jpg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word, a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word. It also has a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(text_to_textnode(text), expected)


if __name__ == "__main__":
    _ = unittest.main()
