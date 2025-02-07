from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        if tag == None:
            raise ValueError("no tag given for parent node")
        if children == None or len(children) == 0:
            raise ValueError("no children given for parent node")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag given for parent node")
        if self.children == None or len(self.children) == 0:
            raise ValueError("no children given for parent node")
        html = ""
        for child in self.children:
            html = html + child.to_html()
        open_tag = f"<{self.tag}{self.props_to_html()}>"
        close_tag = f"</{self.tag}>"
        return open_tag + html + close_tag
    
    def __eq__(self, node):
        if self.tag != node.tag:
            return False
        if self.children != node.children:
            return False
        if self.props != node.props:
            return False
        return True
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
        