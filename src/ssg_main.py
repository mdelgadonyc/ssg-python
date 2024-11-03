from markdown_parser import text_to_textnodes, markdown_to_blocks
from markdown_detector import block_to_block_type
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
import re

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == "normal":
            children.append(normalblock_helper(block))
        elif block_type == "heading":
            children.append(header_helper(block))
        elif block_type == "quoteblock":
            children.append(blockquote_helper(block))
        elif block_type == "codeblock":
            children.append(codeblock_helper(block))
        elif block_type == "unordered_list":
            children.append(unordered_helper(block))
        elif block_type == "ordered_list":
            children.append(ordered_helper(block))
        else:
            print(f"second hit of block_type: {block_type}\n\n")
            continue
    return ParentNode(tag="div", children=children)

def text_to_children(text, block_type, url=None):
    if block_type == TextType.TEXT:
        return LeafNode(tag=None, value=text, props=None)
    if block_type == TextType.BOLD:
        child_node = text_to_children(text, TextType.TEXT)
        return ParentNode(tag="b", value=text, children=child_node)
    elif block_type == TextType.ITALIC:
        child_node = text_to_children(text, TextType.TEXT)
        return ParentNode(tag="i", value=text, children=child_node)
    elif block_type == TextType.CODE:
        return code_helper(text)
    elif block_type == TextType.LINK:
        return link_helper(text, url)
    elif block_type == TextType.IMAGE:
        return image_helper(text, url)

    else:
        print(f"hit the end of text_to_children. block_type: {block_type}")
        print(f"text: {text}")

def normalblock_helper(block):
    textnode_list = text_to_textnodes(block)

    paragraph_node = ParentNode(tag="p", value="", children=[])
    for textnode in textnode_list:
        node = text_to_children(textnode.text, textnode.text_type, textnode.url)
        paragraph_node.children.append(node)
    return paragraph_node

def header_helper(block):
    textnode_list = text_to_textnodes(block)
    text = textnode_list[0].text
    tag = f"h{text.count('#')}"
    text = text.replace("#", "").lstrip()
    text2 = text.lstrip()
    child_node = [text_to_children(text, TextType.TEXT)]
    for textnode in textnode_list[1:]:
        child_node.append([text_to_children(textnode.text, textnode.text_type)])
    return ParentNode(tag=tag, children=child_node)

def normaltext_helper(text):
    return(LeafNode(tag=None, value=text, props=None))

def blockquote_helper(block):
    textnode_list = text_to_textnodes(block)
    text = textnode_list[0].text
    text = text.replace(">", "").strip()
    child_node = [text_to_children(text, TextType.TEXT)]
    return ParentNode(tag="blockquote", children=child_node)

def codeblock_helper(text):
    text = text.replace("`", "").strip()
    child_node = [text_to_children(text, TextType.TEXT)]
    child_node = [ParentNode(tag="code", children=child_node)]
    return ParentNode(tag="pre", children=child_node)

def code_helper(text):
    child_node = [text_to_children(text, TextType.TEXT)]
    return ParentNode(tag="code", children=child_node)

def link_helper(text, url):
    child_node = [text_to_children(text, TextType.TEXT)]
    return ParentNode(tag="a", value=None, children=child_node, props={"href": url})

def image_helper(text, url):
    return LeafNode(tag="img", value=None, props={"src": url, "alt": text})

def unordered_helper(block):
    pattern = r'^[*-] (.+?)(?:\n|$)'
    items = re.split(pattern, block, flags=re.MULTILINE)
    items = [item for item in items if item.strip()]

    children = []
    for item in items:
        text_nodes = text_to_textnodes(item)
        child = []
        for text_node in text_nodes:
            child.append(text_to_children(text_node.text, text_node.text_type))
        children.append(ParentNode(tag="li", children=child, props=None))
    return(ParentNode(tag="ul", children=children))

def ordered_helper(block):
    pattern = r'(?=\d+\.\s)'
    items = re.split(pattern, block, flags=re.MULTILINE)
    items = [item.strip() for item in items if item.strip()]

    children = []
    for item in items:
        item = item[3:] # remove preceeding list item number
        text_nodes = text_to_textnodes(item)
        child = []
        for text_node in text_nodes:
            child.append(text_to_children(text_node.text, text_node.text_type))
        children.append(ParentNode(tag="li", children=child, props=None))

    return(ParentNode(tag="ol", children=children))
    

def create_list_items(textnode_list):
    # choose regex pattern based on whether list items belong to unordered "*" or ordered list
    if textnode_list[0].startswith("1. "):
        items_pattern = r'^\d+\. (.+)'
    else:
        items_pattern = r'^[*-] (.+)'
    
    items = re.findall(items_pattern, textnode_list, re.MULTILINE)

    children = []
    item_nodes = []
    for item in items:
        text_nodes = text_to_textnodes(item)

        item_children = []        
        for text_node in text_nodes:
            child=text_to_children(text_node.text, text_node.text_type)
            item_children.append(child)
        children.append(ParentNode(tag="li", children=item_children, props=None))
    return children
    

