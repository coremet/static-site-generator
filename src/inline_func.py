from textnode import TextType, TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_list = old_node.text.split(f"{delimiter}")
        if len(split_list) == 1:
            new_nodes.append(TextNode(split_list[0], TextType.TEXT))
            continue
        if len(split_list) % 2 == 0:
            raise Exception("this is an invalid Markdown syntax")
        for i in range(len(split_list)):
            if i % 2 == 0:
                new_nodes.extend([TextNode(split_list[i], TextType.TEXT)])
            else:
                new_nodes.extend([TextNode(split_list[i], text_type)])
    return new_nodes

def extract_markdown_images(text):
    image_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_matches

def extract_markdown_links(text):
    link_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_matches