import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_no_props(self) -> None:
        node = LeafNode("p", "This is a leaf node")
        expected = "<p>This is a leaf node</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_props(self) -> None:
        node = LeafNode("p", "This is a leaf node", {"class": "paragraph"})
        expected = "<p class='paragraph'>This is a leaf node</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_multiple_props(self) -> None:
        node = LeafNode("p", "This is a leaf node", {"class": "paragraph", "id": "1"})
        expected = "<p class='paragraph' id='1'>This is a leaf node</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_no_tag(self) -> None:
        node = LeafNode(None, "This is a leaf node")
        expected = "This is a leaf node"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_no_value(self) -> None:
        with self.assertRaises(ValueError) as context:
            node = LeafNode("p", "")
            _ = node.to_html()

        self.assertEqual(str(context.exception), "LeafNode must have a value")


if __name__ == "__main__":
    _ = unittest.main()
