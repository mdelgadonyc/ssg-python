from markdown_parser import text_to_textnodes, markdown_to_blocks
from markdown_detector import block_to_block_type
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
import re

def markdown_to_html_node(markdown):
    markdown = markdown.rstrip()
    blocks = markdown_to_blocks(markdown)
    children = []

    for index, block in enumerate(blocks):
        textnode_list = text_to_textnodes(block)
        # determine block type
        if textnode_list[0].text == "" and textnode_list[0].text_type == TextType.TEXT:
            continue
        if block_to_block_type(textnode_list[0].text) == "normal":
            paragraph_node = ParentNode(tag="p", value="", children=[])
            for textnode in textnode_list:
                if textnode.url:
                    node = text_to_children(textnode.text, textnode.text_type, textnode.url)
                else:
                    node = text_to_children(textnode.text, textnode.text_type)
                paragraph_node.children.append(node)
            children.append(paragraph_node)
        else:
            for textnode in textnode_list:
                if textnode.text_type == TextType.TEXT:
                    text_type = block_to_block_type(textnode.text)
                    if text_type == "normal":
                        text_type = TextType.TEXT
                    children.append(text_to_children(textnode.text, text_type))
    return ParentNode(tag="div", children=children)

def text_to_children(text, block_type, url=None):
    if block_type == "heading":
        return header_helper(text)
    elif block_type == TextType.TEXT:
        return normaltext_helper(text)
    elif block_type == TextType.BOLD:
        child_node = text_to_children(text, TextType.TEXT)
        return ParentNode(tag="strong", value=text, children=child_node)
    elif block_type == TextType.ITALIC:
        child_node = text_to_children(text, TextType.TEXT)
        return ParentNode(tag="em", value=text, children=child_node)
    elif block_type == "unordered_list":
        return unordered_helper(text)
    elif block_type == "ordered_list":
        return ordered_helper(text)
    elif block_type == TextType.CODE:
        return code_helper(text)
    elif block_type == "quoteblock":
        return blockquote_helper(text)
    elif block_type == "codeblock":
        return codeblock_helper(text)
    elif block_type == TextType.LINK:
        return link_helper(text, url)
    else:
        print(f"hit the end of text_to_children. block_type: {block_type}")

def header_helper(text):
    tag = f"h{text.count('#')}"
    text = text.replace("#", "").strip()
    child_node = [text_to_children(text, TextType.TEXT)]
    return ParentNode(tag=tag, children=child_node)

def normaltext_helper(text):
    return(LeafNode(tag=None, value=text, props=None))

def blockquote_helper(text):
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

def unordered_helper(text):
    children = create_list_items(text)
    return(ParentNode(tag="ul", children=children))

def ordered_helper(text):
    children = create_list_items(text)
    return(ParentNode(tag="ol", children=children))

def create_list_items(text):
    # choose regex pattern based on whether list items belong to unordered "*" or ordered list
    if text[0] == "*":
        items_pattern = r'^\* (.+)'
    else:
        items_pattern = r'^\d+\. (.+)'
    items = re.findall(items_pattern, text, re.MULTILINE)

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
    

