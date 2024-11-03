import os
import shutil
import re
from ssg_main import markdown_to_html_node

from_path = "content/majesty/index.md"
template_path = "template.html"
dest_path = "public/index.html"

def main():
    destination_dir = "public"
    source_dir = "static"

    dir_path_content = "content"

    if os.path.exists(destination_dir) and os.path.exists(source_dir):
        print("Deleting and recreating public directory...")
        shutil.rmtree(destination_dir)
        os.mkdir(destination_dir)

        copy_files(source_dir, destination_dir)
    
    generate_pages_recursive(dir_path_content=dir_path_content, template_path=template_path, dest_dir_path=destination_dir)
                
def copy_files(src, dst):
    files = os.listdir(src)
    for file in files:
        if os.path.isfile(os.path.join(src, file)):
            print(f"Copying file {file} to {dst}")
            shutil.copy(os.path.join(src, file), dst)
        else:
            print(f"Creating directory {file} in {dst}")
            os.mkdir(os.path.join(dst, file))
            copy_files(os.path.join(src, file), os.path.join(dst, file))

def extract_title(markdown):
    result = re.findall(r"^#(?!#).*", markdown, re.MULTILINE)
    if not result:
        raise ValueError("No title found")
    title = result.pop()
    title = title[2:]
    return title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir_path, os.path.relpath(from_path, dir_path_content))
                dest_path = os.path.splitext(dest_path)[0] + ".html"
                generate_page(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    title = extract_title(markdown)

    with open(template_path, "r") as f:
        template = f.read()

    template = template.replace(" {{ Title }} ", title)

    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    template = template.replace("{{ Content }}", html_content)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as f:
        f.write(template)

    
main()

