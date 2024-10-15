from enum import Enum

class TextType(Enum):
    HTML = "html"
    BOLD = "bold"

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
    
def main():
    pass
    
main()