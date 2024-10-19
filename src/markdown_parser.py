from textnode import TextNode, TextType
import re

def text_to_textnodes(text):

    node = [TextNode(text, TextType.TEXT)]

    if "**" in text:
        node = split_nodes_delimiter(node, "**", TextType.BOLD)
    
    if "*" in text:
        node = split_nodes_delimiter(node, "*", TextType.ITALIC)
    
    if "`" in text:
        node = split_nodes_delimiter(node, "`", TextType.CODE)

    if "![" in text:
        node = split_nodes(node, TextType.IMAGE)
    
    if "[" in text:
        node = split_nodes(node, TextType.LINK)

    return node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if delimiter in node.text:
            node.text_type = text_type
            segments = node.text.split(delimiter)

            text_type_toggle = False

            for segment in segments:
                if text_type_toggle:
                    new_nodes.append(TextNode(segment, text_type))
                    text_type_toggle = False
                else:
                    new_nodes.append(TextNode(segment, TextType.TEXT))
                    text_type_toggle = True
        else:
            new_nodes.append(node)
                
    return new_nodes

def split_nodes(old_nodes, text_type) -> list[TextNode]:
    new_nodes = []

    if isinstance(old_nodes, TextNode):
        old_nodes = [old_nodes]

    for node in old_nodes:
        if "[" in node.text and text_type == TextType.LINK:
            result = extract_markdown_links(node.text)    
            text_segments = re.split(r"(?<!!)\[(?:[^\[\]]*)\]\((?:[^()]*)\)", node.text)
        elif "![" in node.text and text_type == TextType.IMAGE:
            result = extract_markdown_images(node.text)
            text_segments = re.split(r"!\[(?:[^\[\]]*)\]\((?:[^()]*)\)", node.text)
        else:
            text_segments = None
            result = None
            new_nodes.append(node)

        if text_segments:
            for segment in text_segments:
                if segment:
                    new_nodes.append(TextNode(segment, TextType.TEXT))
                if result:
                    text, url = result.pop(0)
                    new_nodes.append(TextNode(text, text_type, url))

    return new_nodes
  
def extract_markdown_images(text):
    return re.findall("!\[([^\[\]]*)\]\(([^()]*)\)", text)
    
def extract_markdown_links(text):
    return re.findall("(?<!!)\[([^\[\]]*)\]\(([^()]*)\)", text)

def markdown_to_blocks(markdown):
    markdown_blocks = markdown.split("\n\n")

    new_markdown_blocks = []
    for block in markdown_blocks:
        new_block = []
        for line in block.split("\n"):
            new_block.append(line.strip())
        new_markdown_blocks.append("\n".join(new_block))

    return new_markdown_blocks