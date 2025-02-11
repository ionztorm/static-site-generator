import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter


class TestMarkdownSplitter(unittest.TestCase):
    def test_delimiter_bold(self) -> None:
        old_nodes = [TextNode("This sentence has **bold** text.", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This sentence has ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
        self.assertEqual(len(new_nodes), 3)

    def test_delimiter_italic(self) -> None:
        old_nodes = [TextNode("This sentence has *italic* text.", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.ITALIC)
        expected = [
            TextNode("This sentence has ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
        self.assertEqual(len(new_nodes), 3)

    def test_delimiter_code(self) -> None:
        old_nodes = [TextNode("This sentence has `code` text.", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        expected = [
            TextNode("This sentence has ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
        self.assertEqual(len(new_nodes), 3)

    def test_delimiter_no_delimiter(self) -> None:
        old_nodes = [TextNode("This sentence has no delimiters.", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
        expected = [TextNode("This sentence has no delimiters.", TextType.TEXT)]
        self.assertEqual(new_nodes, expected)
        self.assertEqual(len(new_nodes), 1)

    def test_delimiter_multiple(self) -> None:
        old_nodes = [
            TextNode(
                "This sentence has **bold** and *italic* text, and even more **bold** text.",
                TextType.TEXT,
            )
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        expected = [
            TextNode("This sentence has ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text, and even more ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
        self.assertEqual(len(new_nodes), 7)


if __name__ == "__main__":
    _ = unittest.main()
