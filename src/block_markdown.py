import re

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnode


def markdown_to_blocks(markdown: str) -> list[str]:
    return [block.strip() for block in markdown.split("\n\n") if block.strip()]


def block_to_block_type(block: str) -> str:
    match block:
        case _ if re.match(r"^#{1,6} ", block):
            return "heading"

        case _ if block.startswith("```") and block.endswith("```"):
            return "code"

        case _ if all(line.startswith(">") for line in block.split("\n")):
            return "quote"

        case _ if all(re.match(r"^(\*|-) ", line) for line in block.split("\n")):
            return "unordered_list"

        case _ if all(re.match(r"^\d+\. ", line) for line in block.split("\n")):
            numbers = [int(line.split(".")[0]) for line in block.split("\n")]

            if numbers != list(range(1, len(numbers) + 1)):
                raise ValueError(f"Invalid ordered list formatting: {numbers}")

            return "ordered_list"

        case _:
            return "paragraph"


def markdown_to_html(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children: list[HTMLNode] = []

    for block in blocks:
        if not block.strip():
            continue
        block_type = block_to_block_type(block)
        html_node = block_to_html_node(block, block_type)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block: str, block_type: str) -> HTMLNode:
    match block_type:
        case "paragraph":
            return paragraph_to_html(block)
        case "code":
            return code_to_html(block)
        case "quote":
            return quote_to_html(block)
        case "heading":
            return header_to_html(block)
        case "ordered_list":
            return ol_to_html(block)
        case "unordered_list":
            return ul_to_html(block)
        case _:
            raise ValueError("Block is invalid.")


def get_children(text: str) -> list[HTMLNode]:
    nodes = text_to_textnode(text)
    children: list[HTMLNode] = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children


def paragraph_to_html(block: str) -> HTMLNode:
    paragraph = " ".join(block.split("\n"))
    children = get_children(paragraph)
    if len(children) == 1 and isinstance(children[0], LeafNode):
        if children[0].tag in ["img", "a"]:
            return children[0]
    return ParentNode("p", children)


def code_to_html(block: str) -> ParentNode:
    text = block[3:-3].strip()
    children = get_children(text)
    code_element = ParentNode("code", children)
    return ParentNode("pre", [code_element])


def quote_to_html(block: str) -> ParentNode:
    quote_lines = block.split("\n")

    if not all(line.startswith(">") for line in quote_lines):
        raise ValueError("Invalid quote: All lines should start with '>'")
    quote_text = "<br>".join(line.lstrip("> ").strip() for line in quote_lines)

    children = get_children(quote_text)
    return ParentNode("blockquote", children)


def header_to_html(block: str) -> ParentNode:
    level = block[:6].count("#")
    if level + 1 >= len(block):
        raise ValueError("Invalid header: you forgot the heading text.")
    text = block[level:].lstrip("#").strip()
    children = get_children(text)
    return ParentNode(f"h{level}", children)


def ol_to_html(block: str) -> ParentNode:
    list_items = block.split("\n")
    html_items: list[HTMLNode] = [
        ParentNode("li", get_children(re.sub(r"^\d+\.\s*", "", item))) for item in list_items
    ]
    return ParentNode("ol", html_items)


def ul_to_html(block: str) -> ParentNode:
    list_items = block.split("\n")
    html_items = []
    html_items: list[HTMLNode] = [
        ParentNode("li", get_children(item.lstrip("*-").strip())) for item in list_items
    ]
    return ParentNode("ul", html_items)
