from enum import Enum
import re

def markdown_to_blocks(markdown):
    blocks_list = markdown.split("\n\n")
    blocks = []
    for block in blocks_list:
        blocks.append(block.strip())
    blocks = [block for block in blocks if block != ""]
    return blocks

class BlockType(Enum):
    HEADINGS = "headings"
    CODE = "code blocks"
    QUOTE = "quote blocks"
    UNORDERED = "unordered list"
    ORDERED = "ordered list"
    NORMAL = "normal paragraph"

def block_to_blocktype(md_block: str):
    if re.match(r"^#{1,6} ", md_block):
        return BlockType.HEADINGS
    elif re.match(r"^`{3}\n", md_block) and md_block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in md_block.splitlines()):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in md_block.splitlines()):
        return BlockType.UNORDERED
    elif all(line.startswith(f"{i+1}. ") for i, line in enumerate(md_block.splitlines())):
        return BlockType.ORDERED
    else:
        return BlockType.NORMAL
