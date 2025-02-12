from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from node_functions import *

def main():

    print("****** Step 1 ******")
    print("testing text_node creation")
    text_node1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(text_node1)
    print("")

    print("****** Step 2 ******")
    print("testing htmlnode props")
    test_props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    html_node1 = HTMLNode("p", "Paragraph", [], test_props)
    print(html_node1.props_to_html())
    print(str(html_node1))
    print("")

    print("****** Step 3 ******")
    print("testing leaf node creationg and to_html")
    leaf_node1 = LeafNode("p", "This is a paragraph of text.")
    leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leaf_node1)
    print(leaf_node2)
    print(leaf_node1.to_html())
    print(leaf_node2.to_html())
    print("")

    print("****** Step 4 ******")
    print("testing parent node creation and to_html")
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
    print("")

    print("****** Step 5 ******")
    print("testing text to html method")
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
    print("")

    print("****** Step 6 ******")
    print("testing delimiter function")
    node_func = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = NodeFunc.split_nodes_delimiter([node_func], "`", TextType.CODE)
    print(new_nodes)
    print("")

    print("****** Step 7 ******")
    print("testing extrac markdown images function")
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(NodeFunc.extract_markdown_images(text))
    print("")

    print("****** Step 8 ******")
    print("testing extract markdown links function")
    text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(NodeFunc.extract_markdown_links(text2))
    print("")

    print("****** Step 9 ******")
    print("testing split image node function")
    split_image_node = TextNode(
        "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev links.",
        TextType.TEXT,
    )
    print(NodeFunc.split_nodes_image([split_image_node]))
    print("")

    print("****** Step 10 ******")
    print("testing split link node function")
    split_image_node2 = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) links.",
        TextType.TEXT,
    )
    print(NodeFunc.split_nodes_link([split_image_node2]))
    print("")

    print("****** Step 11 ******")
    print("testing text to textnodes function")
    node_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print("text_to_textnodes test")
    text_nodes = NodeFunc.text_to_textnodes(node_text)
    for node in text_nodes:
        print(node)
    print("")


main()