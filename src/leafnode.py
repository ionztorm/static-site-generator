"""LeafNode, child of HTMLNode, represents a leaf node in the HTML tree.

A leaf node is a node that has a value and no children. It is the lowest level of the HTML tree.

For example:
    <p>This is a leaf node</p>
    <p>Thes paragraph is not a leaf node, <b>but this bold text is.</b</p>

A leaf node could also be raw text, like:
    This is a leaf node

"""

from typing import override

from .htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    @override
    def to_html(self) -> str:
        if not self.value:
            raise ValueError("LeafNode must have a value")

        if not self.tag:
            return self.value

        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
