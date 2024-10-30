import os
import shutil
import re
from ssg_main import markdown_to_html_node

from_path = "content/index.md"
template_path = "template.html"
dest_path = "public/index.html"

def main():
    destination_dir = "public"
    source_dir = "static"

    if os.path.exists(destination_dir) and os.path.exists(source_dir):
        print("Deleting and recreating public directory...")
        shutil.rmtree(destination_dir)
        os.mkdir(destination_dir)

        copy_files(source_dir, destination_dir)
    
    generate_page(from_path, template_path, dest_path)
                
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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    title = extract_title(markdown)
    print(f"Title: {title}")

    with open(template_path, "r") as f:
        template = f.read()

    template = template.replace(" {{ Title }} ", title)

    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    template = template.replace("{{ Content }}", html_content)

    with open(dest_path, "w") as f:
        f.write(template)

    
main()

