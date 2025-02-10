import unittest

from block_markdown import block_to_block_type


class TestBlockTypes(unittest.TestCase):
    def test_paragraph(self) -> None:
        self.assertEqual(block_to_block_type("This is a simple paragraph"), "paragraph")

    def test_heading(self) -> None:
        self.assertEqual(block_to_block_type("# heading"), "heading")
        self.assertEqual(block_to_block_type("## heading 2"), "heading")
        self.assertEqual(block_to_block_type("### heading 3"), "heading")
        self.assertEqual(block_to_block_type("#### heading 4"), "heading")
        self.assertEqual(block_to_block_type("##### heading 5"), "heading")
        self.assertEqual(block_to_block_type("###### heading 6"), "heading")

    def test_code_block(self) -> None:
        self.assertEqual(
            block_to_block_type("""```python
code block
```"""),
            "code",
        )

    def test_quote(self) -> None:
        self.assertEqual(
            block_to_block_type("""> line 1 of quote
>line 2 of quote
>line 3 of quote"""),
            "quote",
        )
        self.assertEqual(block_to_block_type("> single line quote"), "quote")

    def test_unordered_list(self) -> None:
        block = """* item 1
* item 2
* item 3"""
        self.assertEqual(block_to_block_type(block), "unordered_list")
        self.assertEqual(block_to_block_type("* singl list item"), "unordered_list")

    def test_ordered_list(self) -> None:
        block_correct = """1. ordered
2. List
3. of 4
4. points"""

        block_incorrect = """1. ordered
3. List
2. of 4
4. points"""

        self.assertEqual(block_to_block_type(block_correct), "ordered_list")
        with self.assertRaises(ValueError) as context:
            _ = block_to_block_type(block_incorrect)

        self.assertEqual(str(context.exception), "Invalid ordered list formatting: [1, 3, 2, 4]")
        self.assertEqual(block_to_block_type("1. single list item"), "ordered_list")


if __name__ == "__main__":
    _ = unittest.main()
