class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        result = "" 
        for k, v in self.props.items():
            result += f' {k}="{v}"'
        return result

    def __repr__(self) -> str:
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props, children=None)
        

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"tag: {self.tag}, value: {self.value}, props: {self.props}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props, value=None)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        if not self.children:
            raise ValueError("All parent nodes must at least have a child")
        result = "" 
        for child in self.children:
            result += f'{child.to_html()}'
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"