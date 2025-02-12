import unittest

from textnode import *
from htmlnode import HTMLNode
from node_functions import NodeFunc


class TestHTMLNode(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = NodeFunc.split_nodes_delimiter([node], "`", TextType.CODE)
        print("testing code textnode text type")
        self.assertTrue(new_nodes[1].text_type == TextType.CODE)

    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = NodeFunc.split_nodes_delimiter([node], "**", TextType.BOLD)
        print("testing bold textnode text type")
        self.assertTrue(new_nodes[1].text_type == TextType.BOLD)

    def test_italic_delimiter(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        new_nodes = NodeFunc.split_nodes_delimiter([node], "*", TextType.ITALIC)
        print("testing italic textnode text type")
        self.assertTrue(new_nodes[1].text_type == TextType.ITALIC)

    def test_bold_then_italic_delimiter(self):
        node = TextNode("This is text with a *italic* word that is **bold**", TextType.TEXT)
        new_nodes = NodeFunc.split_nodes_delimiter([node], "**", TextType.BOLD)
        newer_nodes = NodeFunc.split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        print("testing bold then italic textnode text type")
        print(new_nodes)
        print(newer_nodes)
        self.assertTrue(new_nodes[1].text_type == TextType.BOLD and
                        newer_nodes[1].text_type == TextType.ITALIC)

    def test_images_extractor(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = NodeFunc.extract_markdown_images(text)
        print("testing image extractor")
        self.assertTrue(("rick roll", "https://i.imgur.com/aKaOqIh.gif") == images[0])
        
    def test_links_extractor(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = NodeFunc.extract_markdown_links(text)
        print("testing link extractor")
        self.assertTrue(("to boot dev", "https://www.boot.dev") == links[0])

    def test_split_nodes_images(self):
        split_image_node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        print("testing split_nodes_images")
        split_nodes = NodeFunc.split_nodes_image([split_image_node])
        self.assertTrue(split_nodes[1].text_type == TextType.IMAGE and 
                        split_nodes[3].text_type == TextType.IMAGE)

    def test_split_nodes_links(self):
        split_image_node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        print("testing split_nodes_links")
        split_nodes = NodeFunc.split_nodes_link([split_image_node])
        self.assertTrue(split_nodes[1].text_type == TextType.LINK and 
                        split_nodes[3].text_type == TextType.LINK)

if __name__ == "__main__":
    unittest.main()