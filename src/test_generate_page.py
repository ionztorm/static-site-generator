import unittest

from generate_page import extract_title


class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self) -> None:
        md = "# Title"
        result = extract_title(md)
        expected = "Title"
        self.assertEqual(result, expected)

    def test_extract_title_mid(self) -> None:
        md = """paragraph
# Title

Paragraph"""
        result = extract_title(md)
        expected = "Title"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    _ = unittest.main()
