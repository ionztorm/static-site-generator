import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self) -> None:
        node = HTMLNode("a", "Click Me", None, {"href": "www.boot.dev", "class": "link"})
        expected = (
            "HTMLNode(a, Click Me, children: None, {'href': 'www.boot.dev', 'class': 'link'})"
        )
        self.assertEqual(repr(node), expected)

    def test_props_to_html(self) -> None:
        node = HTMLNode("a", "Click Me", None, {"href": "www.boot.dev", "class": "link"})
        expected = " href='www.boot.dev' class='link'"
        self.assertEqual(node.props_to_html(), expected)

    def test_parameters(self) -> None:
        node = HTMLNode("a", "Click Me", None, {"href": "www.boot.dev", "class": "link"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click Me")
        self.assertIsNone(node.children, None)
        self.assertEqual(node.props, {"href": "www.boot.dev", "class": "link"})


if __name__ == "__main__":
    _ = unittest.main()
