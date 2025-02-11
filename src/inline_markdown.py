import re

from typing import Callable

from textnode import TextNode, TextType


def split_nodes_delimiter(
    nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    delimited_nodes: list[TextNode] = []

    for node in nodes:
        if node.text_type != TextType.TEXT:
            delimited_nodes.append(node)
            continue

        segments = node.text.split(delimiter)

        if len(segments) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax. A {delimiter} has not bee closed.")

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
    type_checked_nodes: list[TextNode] = []

    for node in nodes:
        if node.text_type != TextType.TEXT:
            type_checked_nodes.append(node)
            continue

        type_checked_nodes.extend(process_node(node, extract_function, text_type))

    return type_checked_nodes


def process_node(
    node: TextNode,
    extract_function: Callable[[str], list[tuple[str, str]]],
    text_type: TextType,
) -> list[TextNode]:
    type_checked_nodes: list[TextNode] = []

    node_string = node.text
    elements = extract_function(node_string)
    if not elements:
        type_checked_nodes.append(node)
        return type_checked_nodes

    for display_text, source in elements:
        segments = node_string.split(
            f"[{display_text}]({source})"
            if text_type == TextType.LINK
            else f"![{display_text}]({source})"
        )

        if len(segments) != 2:
            raise ValueError(f"Markdown syntax error for {display_text}.")

        if segments[0] != "":
            type_checked_nodes.append(TextNode(segments[0], TextType.TEXT))

        type_checked_nodes.append(TextNode(display_text, text_type, source))
        node_string = segments[1]

    if node_string != "":
        type_checked_nodes.append(TextNode(node_string, TextType.TEXT))

    return type_checked_nodes


def split_nodes_bold(nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_delimiter(nodes, "**", TextType.BOLD)


def split_nodes_italic(nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_delimiter(nodes, "*", TextType.ITALIC)


def split_nodes_code(nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_delimiter(nodes, "`", TextType.CODE)


def split_nodes_link(nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_by_type(nodes, extract_markdown_links, TextType.LINK)


def split_nodes_image(nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_by_type(nodes, extract_markdown_images, TextType.IMAGE)


def split_nodes_link_and_image(nodes: list[TextNode]) -> list[TextNode]:
    return split_nodes_link(split_nodes_image(nodes))


def text_to_textnode(text: str) -> list[TextNode]:
    return split_nodes_link_and_image(
        split_nodes_code(split_nodes_italic(split_nodes_bold([TextNode(text, TextType.TEXT)])))
    )
