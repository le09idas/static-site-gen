from enum import Enum
from leafnode import LeafNode
from htmlnode import HTMLNode

class TextType(Enum):
    
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        if self.text_type != text_node.text_type:
            return False
        if self.text != text_node.text:
            return False
        if self.url != text_node.url:
            return False
        return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(text_node):
        if text_node.text_type not in TextType:
            raise TypeError("TextNode needs a text_type to become HTMLNode")
        match (text_node.text_type):
            case (TextType.TEXT):
                html_node = LeafNode(text_node.text)
            case (TextType.BOLD):
                html_node = LeafNode(text_node.text,"b")
            case (TextType.ITALIC):
                html_node = LeafNode(text_node.text, "i")
            case (TextType.CODE):
                html_node = LeafNode(text_node.text, "code")
            case (TextType.LINK):
                props = {"href": text_node.url}
                html_node = LeafNode(text_node.text, "a", props)
            case (TextType.IMAGE):
                props = {"href": text_node.url,
                         "alt": text_node.text}
                html_node = LeafNode("", "img", props)
        return html_node