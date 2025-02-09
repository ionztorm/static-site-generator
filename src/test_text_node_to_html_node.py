import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self) -> None:
        node = TextNode("This is a text node", TextType.TEXT)
        html = text_node_to_html_node(node)
        self.assertIsNone(html.tag, None)
        self.assertEqual(html.value, "This is a text node")

    def test_text_node_to_html_node_bold(self) -> None:
        node = TextNode("This is a bold node", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "This is a bold node")

    def test_text_node_to_html_node_italic(self) -> None:
        node = TextNode("This is an italic node", TextType.ITALIC)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "i")
        self.assertEqual(html.value, "This is an italic node")

    def test_text_node_to_html_node_code(self) -> None:
        node = TextNode("This is a code node", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "code")
        self.assertEqual(html.value, "This is a code node")

    def test_text_node_to_html_node_link(self) -> None:
        node = TextNode("This is a link node", TextType.LINK, "https://example.com")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.value, "This is a link node")
        self.assertEqual(html.props, {"href": "https://example.com"})

    def test_text_node_to_html_node_image(self) -> None:
        node = TextNode("This is an image node", TextType.IMAGE, "https://example.com/image.jpg")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")
        self.assertEqual(
            html.props, {"src": "https://example.com/image.jpg", "alt": "This is an image node"}
        )
