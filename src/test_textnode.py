import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        print("testing textnode equality")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        print("testing textnode inequality")
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This has no url", TextType.NORMAL)
        print("testing textnode if url is None")
        self.assertIsNone(node.url)
    
    def test_text_types_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        print("testing textnode different text types")
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_text_nodes_diff(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.google.com/")
        node2 = TextNode("This is a text node", TextType.BOLD)
        print("testing textnode difference in TextNode attributes")
        if node.url != node2.url:
            self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()