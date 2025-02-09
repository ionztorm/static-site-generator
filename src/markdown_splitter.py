from textnode import TextNode, TextType


def split_nodes_delimiter(
    nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    delimited_nodes = []

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
