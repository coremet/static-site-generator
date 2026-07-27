from inline_func import text_to_textnodes
from textnode import TextNode, TextType, textnode_to_htmlnode
from block_func import markdown_to_blocks, block_to_blocktype, BlockType
from htmlnode import ParentNode
import re


def text_to_children(text):
    textnodes_list = text_to_textnodes(text)
    htmlnodes_list = []
    for textnode in textnodes_list:
        new_html = textnode_to_htmlnode(textnode)
        htmlnodes_list.append(new_html)
    return htmlnodes_list

def markdown_to_htmlnode(markdown):
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_blocktype(block)
    # Paragraph
        if block_type == BlockType.NORMAL: 
            block_nodes.append(ParentNode("p", text_to_children(block.replace("\n", " "))))
    # Heading
        elif block_type == BlockType.HEADINGS:
            level = len(block) - len(block.lstrip("#")) # "count leading characters = len(s) - len(s.lstrip(char))"
            block_nodes.append(ParentNode(f"h{level}", text_to_children(block.lstrip("#").strip()))) # strip the #, strip leading and trailing spaces

    # Code
        elif block_type == BlockType.CODE:
            raw_text = block.strip("`").lstrip("\n").strip(" \t")
            code_leaf = textnode_to_htmlnode(TextNode(raw_text, TextType.TEXT))
            block_nodes.append(ParentNode("pre", [ParentNode("code", [code_leaf])]))
    # Quote
        elif block_type == BlockType.QUOTE:
            lines = [line.lstrip(">").strip() for line in block.splitlines()] # list comprehension
            raw_text = "\n".join(lines)
            block_nodes.append(ParentNode(f"blockquote", text_to_children(raw_text)))
    # Unordered
        elif block_type == BlockType.UNORDERED:
            raw_lines = [line.lstrip("-").strip() for line in block.splitlines()]
            unordered_leaf = []
            for un_raw_text in raw_lines:
                unordered_leaf.append(ParentNode(f"li", text_to_children(un_raw_text)))
            block_nodes.append(ParentNode("ul", unordered_leaf))
    # Ordered
        elif block_type == BlockType.ORDERED:
            raw_lines = [re.sub(r"^\d+\. ", "", line) for line in block.splitlines()]
            ordered_leaf = []
            for or_raw_text in raw_lines:
                ordered_leaf.append(ParentNode(f"li", text_to_children(or_raw_text)))
            block_nodes.append(ParentNode("ol", ordered_leaf))
    return ParentNode("div", block_nodes)   