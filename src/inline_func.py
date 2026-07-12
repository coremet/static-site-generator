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

def extract_markdown_images(text: str):
    image_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for image_alt, image_url in image_matches:
        if image_alt == "":
            raise Exception("this is an invalid Markdown syntax - missing alt text")
        elif image_url == "":
            raise Exception("this is an invalid Markdown syntax - missing url")
    return image_matches

def extract_markdown_links(text: str):
    link_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for link_alt, link_url in link_matches:
        if link_alt == "":
            raise Exception("this is an invalid Markdown syntax - missing alt text")
        elif link_url == "":
           raise Exception("this is an invalid Markdown syntax - missing url")
    return link_matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for image_alt, image_url in extract_markdown_images(remaining_text):
            sections = remaining_text.split(f"![{image_alt}]({image_url})", 1)
            if sections[0]:    
                new_nodes.append(TextNode(sections[0], TextType.TEXT, None))
            new_nodes.append(TextNode(f"{image_alt}", TextType.IMAGE, f"{image_url}"))
            remaining_text = sections[1]
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT, None))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for link_alt, link_url in extract_markdown_links(remaining_text):
            sections = remaining_text.split(f"[{link_alt}]({link_url})", 1)
            if sections[0]:    
                new_nodes.append(TextNode(sections[0], TextType.TEXT, None))
            new_nodes.append(TextNode(f"{link_alt}", TextType.LINK, f"{link_url}"))
            remaining_text = sections[1]
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT, None))
    return new_nodes