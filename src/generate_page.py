from block_to_html import markdown_to_htmlnode
from extract_title import extract_title
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        md_file_content = f.read()
    title = extract_title(md_file_content)
    htmlnodes_list = markdown_to_htmlnode(md_file_content)
    htmlstr = htmlnodes_list.to_html()
    with open(template_path, "r", encoding="utf-8") as f:
            template_file_content = f.read()
    title_in_template = template_file_content.replace("{{ Title }}", title)
    content_in_template = title_in_template.replace("{{ Content }}", htmlstr)
    # dest_path is already the full file path, e.g. "public/index.html"
    # Make sure the parent directory exists (the folder, not the file)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    # Write to the file
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(content_in_template)