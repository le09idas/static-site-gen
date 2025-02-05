from textnode import *
from htmlnode import *
from leafnode import *

def main():
    text_node1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(text_node1)
    test_props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    html_node1 = HTMLNode("p", "Paragraph", [], test_props)
    print(html_node1.props_to_html())
    print(str(html_node1))
    leaf_node1 = LeafNode("p", "This is a paragraph of text.")
    leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leaf_node1)
    print(leaf_node2)
    print(leaf_node1.to_html())
    print(leaf_node2.to_html())

main()