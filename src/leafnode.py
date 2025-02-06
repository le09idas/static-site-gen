from htmlnode import *

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value")
        html = self.value
        open_tag = ""
        close_tag = ""
        if self.tag != None:
            tag_props = self.props_to_html()
            open_tag = f"<{self.tag}{tag_props}>"
            close_tag = f"</{self.tag}>"
        return open_tag + html + close_tag
    
    def __eq__(self, node):
        if self.tag != node.tag:
            return False
        if self.value != node.value:
            return False
        if self.props != node.props:
            return False
        return True
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"