import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_is_equal_no_url(self) -> None:
        node = TextNode("Testing eq is equal with no url", TextType.BOLD)
        node2 = TextNode("Testing eq is equal with no url", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_is_not_equal_texttype_no_url(self) -> None:
        node = TextNode("Testing eq is NOT equal with no url", TextType.BOLD)
        node2 = TextNode("Testing eq is NOT equal with no url", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_eq_is_not_equal_text_no_url(self) -> None:
        node = TextNode("Testing eq different text", TextType.BOLD)
        node2 = TextNode("Testing eq has different text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_is_equal_with_url(self) -> None:
        node = TextNode("Testing eq is equal with url", TextType.BOLD, "www.example.com")
        node2 = TextNode("Testing eq is equal with url", TextType.BOLD, "www.example.com")
        self.assertEqual(node, node2)

    def test_eq_is_not_equal_with_url(self) -> None:
        node = TextNode("Testing eq is NOT equal with url", TextType.BOLD, "www.example.com")
        node2 = TextNode("Testing eq is NOT equal with url", TextType.CODE, "www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_repr_url(self) -> None:
        node = TextNode("Testing repr", TextType.BOLD, "www.boot.dev")
        expected = "TextNode(Testing repr, bold, www.boot.dev)"
        self.assertEqual(repr(node), expected)

    def test_repr_no_url(self) -> None:
        node = TextNode("Testing repr", TextType.BOLD)
        expected = "TextNode(Testing repr, bold, None)"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    _ = unittest.main()
