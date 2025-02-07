from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

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
    parent_node = ParentNode(
        "p",
        [
            LeafNode("Bold text", "b"),
            LeafNode("Normal text", ""),
            LeafNode("italic text", "i"),
            LeafNode("Normal text", ""),
        ],
    )
    parent_node2 = ParentNode(
        "p",
        [
            parent_node,
            LeafNode("Bold text2", "b"),
            LeafNode("Normal text2", ""),
            LeafNode("italic text2", "i"),
            LeafNode("Normal text2", ""),
        ],
    )
    print(parent_node)
    print(parent_node.to_html())
    print(parent_node2.to_html())
    text_to_html_node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
    text_to_html_node2 = TextNode("This is a text node2", TextType.BOLD, "https://www.boot.dev")
    text_to_html_node3 = TextNode("This is a text node3", TextType.ITALIC, "https://www.boot.dev")
    text_to_html_node4 = TextNode("This is a text node4", TextType.CODE, "https://www.boot.dev")
    text_to_html_node5 = TextNode("This is a text node5", TextType.LINK, "https://www.boot.dev")
    text_to_html_node6 = TextNode("This is a text node6", TextType.IMAGE, "https://www.boot.dev")
    print(TextNode.text_node_to_html_node(text_to_html_node).to_html())
    print(TextNode.text_node_to_html_node(text_to_html_node2).to_html())
    print(TextNode.text_node_to_html_node(text_to_html_node3).to_html())
    print(TextNode.text_node_to_html_node(text_to_html_node4).to_html())
    print(TextNode.text_node_to_html_node(text_to_html_node5).to_html())
    print(TextNode.text_node_to_html_node(text_to_html_node6).to_html())
    


main()