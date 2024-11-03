from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, value=None,children=None, props=None) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Missing tag")
        if self.children == []:
            raise ValueError("Missing children")
        html_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            if isinstance(child, list):
                for item in child:
                    html_string += item.to_html()
            else:
                html_string += child.to_html()
        html_string += f"</{self.tag}>"
        return html_string
    