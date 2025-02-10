import textwrap
import unittest

from block_markdown import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_one_block(self) -> None:
        markdown = "# This is a header."
        expected = ["# This is a header."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_two_blocks(self) -> None:
        markdown = """# This is a header.

        And this is a paragraph with **bold** text."""
        expected = ["# This is a header.", "And this is a paragraph with **bold** text."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_ullist_blocks(self) -> None:
        markdown = textwrap.dedent("""# This is a header.

        And this is a paragraph with **bold** text.

* And an unordered list with
* three
* items
        """)
        expected = [
            "# This is a header.",
            "And this is a paragraph with **bold** text.",
            "* And an unordered list with\n* three\n* items",
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_ollist_blocks(self) -> None:
        markdown = textwrap.dedent("""# This is a header.

        And this is a paragraph with **bold** text.

* And an unordered list with
* three
* items

1. and an
2. ordered list
        """)
        expected = [
            "# This is a header.",
            "And this is a paragraph with **bold** text.",
            "* And an unordered list with\n* three\n* items",
            "1. and an\n2. ordered list",
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)


if __name__ == "__main__":
    _ = unittest.main()
