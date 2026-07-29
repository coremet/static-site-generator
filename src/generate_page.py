from block_to_html import markdown_to_htmlnode
from extract_title import extract_title
import os


def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        md_file_content = f.read()
    title = extract_title(md_file_content)
    htmlnodes_list = markdown_to_htmlnode(md_file_content)
    htmlstr = htmlnodes_list.to_html()
    with open(template_path, "r", encoding="utf-8") as f:
            template_file_content = f.read()
    basepath_in_template = template_file_content.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    final_template = basepath_in_template.replace("{{ Title }}", title).replace("{{ Content }}", htmlstr)
    # dest_path is already the full file path, e.g. "public/index.html"
    # Make sure the parent directory exists (the folder, not the file)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    # Write to the file
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(final_template)

def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for filename in files:
            if filename.endswith(".md"):
        # Combine root and file name to get the absolute path
                src_path = os.path.join(root, filename)
                rel_path = os.path.relpath(root, dir_path_content)
                dest_path = os.path.join(dest_dir_path, rel_path, filename.replace(".md", ".html"))
                generate_page(basepath, src_path, template_path, dest_path)