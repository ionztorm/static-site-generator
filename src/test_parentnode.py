import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_one_leafnode(self) -> None:
        child = LeafNode("p", "This is a parent node")
        parent = ParentNode("div", [child])
        expected = "<div><p>This is a parent node</p></div>"
        self.assertEqual(parent.to_html(), expected)

    def test_to_html_two_leafnodes(self) -> None:
        child1 = LeafNode("p", "This is a parent node")
        child2 = LeafNode("p", "This is another parent node")
        parent = ParentNode("div", [child1, child2])
        expected = "<div><p>This is a parent node</p><p>This is another parent node</p></div>"
        self.assertEqual(parent.to_html(), expected)

    def test_to_html_nested_parentnode(self) -> None:
        grandchild = LeafNode("em", "This is a parent node")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [ParentNode("p", [child])])
        expected = "<div><p><span><em>This is a parent node</em></span></p></div>"
        self.assertEqual(parent.to_html(), expected)

    def test_to_html_many_children(self) -> None:
        child1 = LeafNode("p", "This is parent node 0")
        child2 = LeafNode("p", "This is parent node 1")
        child3 = LeafNode("p", "This is parent node 2")
        child4 = LeafNode("p", "This is parent node 3")
        parent = ParentNode("div", [child1, child2, child3, child4])
        expected = (
            "<div>"
            "<p>This is parent node 0</p>"
            "<p>This is parent node 1</p>"
            "<p>This is parent node 2</p>"
            "<p>This is parent node 3</p>"
            "</div>"
        )
        self.assertEqual(parent.to_html(), expected)

    def test_repr(self) -> None:
        child1 = LeafNode("p", "This is parent node 0")
        child2 = LeafNode("p", "This is parent node 1")
        parent = ParentNode("div", [child1, child2])
        expected = (
            "ParentNode(div, children: [LeafNode(p, This is parent node 0, None), "
            "LeafNode(p, This is parent node 1, None)], None)"
        )
        self.assertEqual(repr(parent), expected)


if __name__ == "__main__":
    _ = unittest.main()
