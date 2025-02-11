import re

from htmlnode import HTMLNode
from textnode import text_node_to_html_node
from parentnode import ParentNode
from block_markdown import markdown_to_blocks, block_to_block_type
from markdown_parser import text_to_textnode


def markdown_to_html(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children: list[HTMLNode] = []

    for block in blocks:
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
        case "header":
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


def paragraph_to_html(block: str) -> ParentNode:
    paragraph = " ".join(block.split("\n"))
    children = get_children(paragraph)
    return ParentNode("p", children)


def code_to_html(block: str) -> ParentNode:
    text = block[3:-3]
    children = get_children(text)
    code_element = ParentNode("code", children)
    return ParentNode("pre", [code_element])


def quote_to_html(block: str) -> ParentNode:
    quote_lines = block.split("\n")

    if not all(line.startswith(">") for line in quote_lines):
        raise ValueError("Invalid quote: All lines should start with '>'")
    quote_text = " ".join(line.lstrip("> ").strip() for line in quote_lines)

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
    html_items: list[HTMLNode] = [
        ParentNode("li", get_children(item.lstrip("*-").strip())) for item in list_items
    ]
    return ParentNode("ul", html_items)
