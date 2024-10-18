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
        node = split_nodes_image(node)
    
    if "[" in text:
        node = split_nodes_link(node)

    #node.pop()
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
        
def split_nodes_link(old_nodes) -> list[TextNode]:
    new_nodes = []

    if isinstance(old_nodes, TextNode):
        old_nodes = [old_nodes]

    for node in old_nodes:
        if "[" in node.text:
            links = extract_markdown_links(node.text)    
            text_segments = re.split(r"(?<!!)\[(?:[^\[\]]*)\]\((?:[^()]*)\)", node.text)

            for segment in text_segments:
                if segment:
                    new_nodes.append(TextNode(segment, TextType.TEXT))
                if links:
                    text, url = links.pop(0)
                    new_nodes.append(TextNode(text, TextType.LINK, url))
        else:
            new_nodes.append(node)

    return new_nodes

def split_nodes_image(old_nodes) -> list[TextNode]:
    new_nodes = []

    if isinstance(old_nodes, TextNode):
        old_nodes = [old_nodes]

    for node in old_nodes:
        if "![" in node.text:
            images = extract_markdown_images(node.text)    
            text_segments = re.split(r"!\[(?:[^\[\]]*)\]\((?:[^()]*)\)", node.text)

            for segment in text_segments:
                if segment:
                    new_nodes.append(TextNode(segment, TextType.TEXT))
                if images:
                    text, url = images.pop(0)
                    new_nodes.append(TextNode(text, TextType.IMAGE, url))

        else:
            new_nodes.append(node)

    return new_nodes


def extract_markdown_images(text):
    return re.findall("!\[([^\[\]]*)\]\(([^()]*)\)", text)
    
def extract_markdown_links(text):
    return re.findall("(?<!!)\[([^\[\]]*)\]\(([^()]*)\)", text)


