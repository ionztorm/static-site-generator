import unittest

from inline_markdown import extract_markdown_links


class TestExtractMarkdownLink(unittest.TestCase):
    def test_extract_markdown_images_one_link(self) -> None:
        markdown = "This text has an image [link text](https://www.example.com)"
        matches = extract_markdown_links(markdown)
        expected = [("link text", "https://www.example.com")]
        self.assertEqual(matches, expected)

    def test_extract_markdown_images_two_links(self) -> None:
        markdown = (
            "This text has an image [link text](https://www.example.com)"
            "and another [link text](https://www.example.com)"
        )
        matches = extract_markdown_links(markdown)
        expected = [
            ("link text", "https://www.example.com"),
            ("link text", "https://www.example.com"),
        ]
        self.assertEqual(matches, expected)

    def test_extract_markdown_images_images_no_links(self) -> None:
        markdown = (
            "This text has no images but has a link ![alt text](https://www.example.com/image.jpg)"
        )
        matches = extract_markdown_links(markdown)
        self.assertEqual(matches, [])


if __name__ == "__main__":
    _ = unittest.main()
