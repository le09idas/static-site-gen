from functools import reduce

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method is not implemented")
    
    def props_to_html(self):

        if self.props == None:
            return ""
        
        def combine_string(x, y):
            return x + y
        html_string = ""
        
        props_list = list(map(lambda key, value: f' {key}="{value}"', self.props.keys(), self.props.values()))
        html_string = reduce(combine_string, props_list)
        return html_string
    
    def __eq__(self, node):
        if self.tag != node.tag:
            return False
        if self.value != node.value:
            return False
        if self.children != node.children:
            return False
        if self.props != node.props:
            return False
        return True
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"