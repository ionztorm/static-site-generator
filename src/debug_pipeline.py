from htmlnode import HTMLNode
from textnode import text_node_to_html_node
from block_markdown import markdown_to_html, markdown_to_blocks, block_to_block_type
from inline_markdown import text_to_textnode


page_test = """
# Page test

## Paragraph Elements

### Text features

This paragraph has **bold text**, *italic text*, a `code block`.

### Images

![an image](https://www.boot.dev/boots.jpg)

### Links

[to boot dev](https://www.boot.dev)

## Code

```
The code block is for code.
```

## Quotes

> quotes should all start
> with this arrow.
> Even new lines.

## Lists

* Unordered lists
* start witn ah asterisk
* for each point

1. ordered lists
2. must start with a digit followed by a .
3. The digits must be in order, starting from 1.

"""

# ### Step 1 - Get Blocks
# print("\n=== STEP 1 ===\n")
# blocks = markdown_to_blocks(page_test)

# ### Step 2 - Get block types
# print("\n=== STEP 2 ===\n")
# for block in blocks:
#     block_type = block_to_block_type(block)


### Step 3: Convert to TextNodes ###
print("\n=== STEP 3 ===\n")


def markdown_to_html(md):
    blocks = markdown_to_blocks(md)
    for block in blocks:
        print("---------------------")
        block_type = block_to_block_type(block)
        node = block_to_node(block, block_type)
        print("---------------------\n")


def block_to_node(block, type) -> None:
    match type:
        case "paragraph":
            node = paragraph_to_html(block)
            print(f"Block: {block}\nType: {type}\nNode: {node}")
        case "heading":
            print(f"Block: {block}\nType: {type}\n")
        case "code":
            print(f"Block: {block}\nType: {type}\n")
        case "quote":
            print(f"Block: {block}\nType: {type}\n")
        case "ordered_list":
            print(f"Block: {block}\nType: {type}\n")
        case "unordered_list":
            print(f"Block: {block}\nType: {type}\n")
        case _:
            raise ValueError("invalid block type")


def text_to_children(text):
    nodes = text_to_textnode(text)
    print(f"Creating children: {nodes}")
    children: list[HTMLNode] = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children


def paragraph_to_html(block):
    paragraph = " ".join(block.split("\n"))
    children = text_to_children(paragraph)
    return f"ParentNode(''p', {children})"


markdown_to_html(page_test)
