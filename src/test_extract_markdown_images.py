import unittest

from inline_markdown import extract_markdown_images


class TestExtractMarkdownImage(unittest.TestCase):
    def test_extract_markdown_images_one_image(self) -> None:
        markdown = "This text has an image ![alt text](https://www.example.com/image.jpg)"
        matches = extract_markdown_images(markdown)
        expected = [("alt text", "https://www.example.com/image.jpg")]
        self.assertEqual(matches, expected)

    def test_extract_markdown_images_two_images(self) -> None:
        markdown = (
            "This text has an image ![alt text](https://www.example.com/image.jpg)"
            "and another ![alt text](https://www.example.com/image.jpg)"
        )
        matches = extract_markdown_images(markdown)
        expected = [
            ("alt text", "https://www.example.com/image.jpg"),
            ("alt text", "https://www.example.com/image.jpg"),
        ]
        self.assertEqual(matches, expected)

    def test_extract_markdown_images_links_no_images(self) -> None:
        markdown = "This text has no images but has a link [link text](https://www.example.com)"
        matches = extract_markdown_images(markdown)
        self.assertEqual(matches, [])


if __name__ == "__main__":
    _ = unittest.main()
