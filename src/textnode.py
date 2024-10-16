from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6
    UNKNOWN = 7

class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str = None) -> None:
        super().__init__()
        self.text = text #text content of node passed in
        self.text_type = text_type # Enum type
        self.url = url # URL of the link or image
        
    def __eq__(self, value: object) -> bool:
        if self.text == value.text and self.text_type == value.text_type and self.url == value.url:
            return True
        return False
    
    def __repr__(self) -> str:
        return TextNode(self.text, self.text_type, self.url)

def text_node_to_html(text_node):
    match text_node.text_type:
        case (TextType.TEXT):
            return LeafNode(tag=None, value=text_node.text)
        case (TextType.BOLD):
            return LeafNode(tag="b", value=text_node.text)
        case (TextType.ITALIC):
            return LeafNode(tag="i", value=text_node.text)
        case (TextType.CODE):
            return LeafNode(tag="code", value=text_node.text)
        case (TextType.LINK):
            return LeafNode(tag="a", value=text_node.text, props={"href" : text_node.url, "target": "_blank"})
        case (TextType.IMAGE):
            return LeafNode(tag="img", value=text_node.text, props={"src" : text_node.url, "alt" : text_node.text})
        case _:
            raise ValueError("Invalid text type")

def main():
    pass
    
main()