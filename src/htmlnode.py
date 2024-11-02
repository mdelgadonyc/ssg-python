class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children if isinstance(children, list) else [children] if children else []
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        
        props_result = ""
        for prop in self.props:
            props_result += f' {prop}="{self.props[prop]}"'

        return props_result

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.props == other.props and
            self.children == other.children
        )
    
    def __repr__(self) -> str:
        return f'HTMLNode(tag="{self.tag}", value="{self.value}", children={self.children}, props="{self.props}")'


    