import re

from typing import Callable

from textnode import TextNode, TextType


def split_nodes_delimiter(
    nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    delimited_nodes: list[TextNode] = []

    for node in nodes:
        # NOTE: if the type is not TEXT then it ir already converted, so add it right away and loop.
        # This allows single lines that contain multi-markdown syntax to be re-checked.
        if node.text_type != TextType.TEXT:
            delimited_nodes.append(node)
            continue

        # split the node text into it's parts
        segments = node.text.split(delimiter)

        # If markdown syntax is properly closed, there should always be an odd number of items in
        # the split list. If not, a markdown tag wasn't closed propertly.
        if len(segments) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax. A {delimiter} has not bee closed.")

        # even numbers should now be the text wrapped by the delimiter.
        # Create a new TextNode using the passed text_type for wrapped text, else TextType.TEXT.
        splits: list[TextNode] = [
            TextNode(segment, text_type if index % 2 else TextType.TEXT)
            for index, segment in enumerate(segments)
            if segment
        ]

        delimited_nodes.extend(splits)
    return delimited_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_by_type(
    nodes: list[TextNode],
    extract_function: Callable[[str], list[tuple[str, str]]],
    text_type: TextType,
) -> list[TextNode]:
    split_nodes: list[TextNode] = []

    for node in nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            continue

        node_string = node.text
        elements = extract_function(node_string)
        if not elements:
            split_nodes.append(node)
            continue

        for display_text, source in elements:
            segments = node_string.split(
                f"[{display_text}]({source})"
                if text_type == TextType.LINK
                else f"![{display_text}]({source})"
            )

            if len(segments) != 2:
                raise ValueError(f"Markdown syntax error for {display_text}.")

            if segments[0] != "":
                split_nodes.append(TextNode(segments[0], TextType.TEXT))

            split_nodes.append(TextNode(display_text, text_type, source))
            node_string = segments[1]

        if node_string != "":
            split_nodes.append(TextNode(node_string, TextType.TEXT))

    return split_nodes


def split_nodes_link(nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_by_type(nodes, extract_markdown_links, TextType.LINK)


def split_nodes_image(nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_by_type(nodes, extract_markdown_images, TextType.IMAGE)


def split_nodes_link_and_image(nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_image(split_nodes_link(nodes))
