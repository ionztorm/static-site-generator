from typing import override


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str | None] | None = None,
    ) -> None:
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list[HTMLNode] | None = children
        self.props: dict[str, str | None] | None = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        return "".join(f' {key}="{value}"' for key, value in self.props.items())

    @override
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list["HTMLNode"],
        props: dict[str, str | None] | None = None,
    ) -> None:
        super().__init__(tag, None, children, props)

    @override
    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")

        children_html = "".join(child.to_html() for child in self.children)

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    @override
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None, value: str, props: dict[str, str | None] | None = None
    ) -> None:
        super().__init__(tag, value, None, props)

    @override
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if not self.tag:
            return self.value

        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    @override
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
