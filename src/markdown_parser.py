from textnode import TextNode, TextType
import re

def text_to_textnodes(text):

    nodes = [TextNode(text, TextType.TEXT)]

    if "**" in text:
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    if "*" in text and text[0:2] != "* ":
        nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    
    if "`" in text and text[0] != "`":
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    if "![" in text:
        nodes = split_nodes(nodes, TextType.IMAGE)
    
    if "[" in text:
        nodes = split_nodes(nodes, TextType.LINK)

    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        if text_type == TextType.BOLD:
            pattern = r'\*\*(.*?)\*\*'
        elif text_type == TextType.ITALIC:
            pattern = r'\*(.*?)\*'
        elif text_type == TextType.CODE:
            pattern = r'`(.*?)`'
        else:
            raise ValueError("Invalid text type")
        
        matches = re.findall(pattern, text)
        for match in matches:
            index = text.index(delimiter + match + delimiter)
            pre_match_text = text[:index]
            if pre_match_text:
                new_nodes.append(TextNode(pre_match_text, TextType.TEXT))
            new_nodes.append(TextNode(match, text_type))
            text = text[index + len(delimiter + match + delimiter):]
        
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes(old_nodes, text_type) -> list[TextNode]:
    new_nodes = []

    if isinstance(old_nodes, TextNode):
        old_nodes = [old_nodes]

    for node in old_nodes:
        if "![" in node.text and text_type == TextType.IMAGE:
            result = extract_markdown_images(node.text)
            text_segments = re.split(r"!\[(?:[^\[\]]*)\]\((?:[^()]*)\)", node.text)
        elif "[" in node.text and text_type == TextType.LINK:
            result = extract_markdown_links(node.text)
            text_segments = re.split(r"(?<!!)\[(?:[^\[\]]*)\]\((?:[^()]*)\)", node.text)
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