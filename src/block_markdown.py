import re


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
