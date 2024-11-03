from htmlnode import HTMLNode

SELF_CLOSING_TAGS = {"img", "br", "hr"}

class LeafNode(HTMLNode):
    def __init__(self, value=None, tag=None, props=None) -> None:
        super().__init__(tag, value, None, props)
    
    def props_to_html(self):
        if self.props == None:
            return ""
        props_string = ""
        for prop in self.props:
            props_string += f' {prop}="{self.props[prop]}"'

        return props_string
    
    def to_html(self):
        if self.tag in SELF_CLOSING_TAGS:
            return f"<{self.tag}{self.props_to_html()}/>"
        if self.value == None:
            raise ValueError("Missing value")
        if self.tag == None:
            return self.value
        
        html_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return html_string