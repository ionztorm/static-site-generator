import unittest

from textnode import TextNode, TextType
from markdown_parser import (
    split_nodes_link,
    split_nodes_image,
    split_nodes_by_type,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_link_and_image,
)


class TestSplitImageLink(unittest.TestCase):
    def test_split_by_image(self) -> None:
        node = TextNode(
            "This is text with an image of ![boots](https://www.boot.dev/image.png)",
            TextType.TEXT,
        )
        expected = [
            TextNode("This is text with an image of ", TextType.TEXT),
            TextNode("boots", TextType.IMAGE, "https://www.boot.dev/image.png"),
        ]
        self.assertEqual(split_nodes_image([node]), expected)
        self.assertEqual(
            split_nodes_by_type([node], extract_markdown_images, TextType.IMAGE), expected
        )

    def test_split_by_images(self) -> None:
        node = TextNode(
            "This is text with an image of ![boots](https://www.boot.dev/image.png) and "
            + "![lane](https://www.boot.dev/lane.png)",
            TextType.TEXT,
        )
        expected = [
            TextNode("This is text with an image of ", TextType.TEXT),
            TextNode("boots", TextType.IMAGE, "https://www.boot.dev/image.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("lane", TextType.IMAGE, "https://www.boot.dev/lane.png"),
        ]
        self.assertEqual(split_nodes_image([node]), expected)
        self.assertEqual(
            split_nodes_by_type([node], extract_markdown_images, TextType.IMAGE), expected
        )

    def test_split_by_link(self) -> None:
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertEqual(split_nodes_link([node]), expected)
        self.assertEqual(
            split_nodes_by_type([node], extract_markdown_links, TextType.LINK), expected
        )

    def test_split_by_links(self) -> None:
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and "
            + "[to google](https://www.google.com)",
            TextType.TEXT,
        )
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to google", TextType.LINK, "https://www.google.com"),
        ]
        self.assertEqual(split_nodes_link([node]), expected)
        self.assertEqual(
            split_nodes_by_type([node], extract_markdown_links, TextType.LINK), expected
        )

    def test_split_by_link_w_img(self) -> None:
        node = TextNode(
            "This is text with an image of ![boots](https://www.boot.dev/image.png) "
            + "and a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        expected = [
            TextNode(
                "This is text with an image of ![boots](https://www.boot.dev/image.png) "
                + "and a link ",
                TextType.TEXT,
            ),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]

        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_by_image_w_link(self) -> None:
        node = TextNode(
            "This is text with an image of ![boots](https://www.boot.dev/image.png) "
            + "and a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        expected = [
            TextNode(
                "This is text with an image of ",
                TextType.TEXT,
            ),
            TextNode("boots", TextType.IMAGE, "https://www.boot.dev/image.png"),
            TextNode(" and a link [to boot dev](https://www.boot.dev)", TextType.TEXT),
        ]

        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_by_image_and_link(self) -> None:
        node = TextNode(
            "This is text with an image of ![boots](https://www.boot.dev/image.png) "
            + "and a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        expected = [
            TextNode(
                "This is text with an image of ",
                TextType.TEXT,
            ),
            TextNode("boots", TextType.IMAGE, "https://www.boot.dev/image.png"),
            TextNode(" and a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]

        self.assertEqual(split_nodes_link_and_image([node]), expected)


if __name__ == "__main__":
    _ = unittest.main()
