from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    for node in old_nodes:
        if delimiter in node.text:
            node.text_type = text_type
            segments = node.text.split(delimiter)
            new_nodes = []

            text_type_toggle = False

            for segment in segments:
                if text_type_toggle:
                    new_nodes.append(TextNode(segment, text_type))
                    text_type_toggle = False
                else:
                    new_nodes.append(TextNode(segment, TextType.TEXT))
                    text_type_toggle = True
                
            return new_nodes

def extract_markdown_images(text):
    return re.findall("!\[([^\[\]]*)\]\(([^()]*)\)", text)
    
def extract_markdown_links(text):
    return re.findall("(?<!!)\[([^\[\]]*)\]\(([^()]*)\)", text)


