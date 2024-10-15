class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
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

    def __eq__(self, value: object) -> bool:
        if self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props:
            return True
        return False    
    
    def __repr__(self) -> str:
        return HTMLNode(self.tag, self.value, self.children, self.props)


    