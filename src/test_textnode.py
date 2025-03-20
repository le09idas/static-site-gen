import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        print("testing textnode equality")
        self.assertEqual(node, node2)
        print("")

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        print("testing textnode inequality")
        self.assertNotEqual(node, node2)
        print("")

    def test_url_is_none(self):
        node = TextNode("This has no url", TextType.TEXT)
        print("testing textnode if url is None")
        self.assertIsNone(node.url)
        print("")
    
    def test_text_types_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        print("testing textnode different text types")
        self.assertNotEqual(node.text_type, node2.text_type)
        print("")

    def test_text_nodes_diff(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.google.com/")
        node2 = TextNode("This is a text node", TextType.BOLD)
        print("testing textnode difference in TextNode attributes")
        if node.url != node2.url:
            self.assertNotEqual(node, node2)
        print("")

    def test_text_t2html_func(self):
        node = TextNode("This is a text node", TextType.TEXT)
        leaf = node.text_node_to_html_node()
        print("testing text to html")
        self.assertTrue(leaf.tag == None and leaf.children == None and leaf.props == None)
        print("")

    def test_bold_t2html_func(self):
        node = TextNode("This is a text node", TextType.BOLD)
        leaf = node.text_node_to_html_node()
        print("testing bold to html")
        self.assertTrue(leaf.tag == "b" and leaf.children == None)
        print("")

    def test_italic_t2html_func(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        leaf = node.text_node_to_html_node()
        print("testing italic to html")
        self.assertTrue(leaf.tag == "i" and leaf.children == None)
        print("")

    def test_code_t2html_func(self):
        node = TextNode("This is a text node", TextType.CODE)
        leaf = node.text_node_to_html_node()
        print("testing code to html")
        self.assertTrue(leaf.tag == "code" and leaf.children == None)
        print("")

    def test_link_t2html_func(self):
        node = TextNode("This is a text node", TextType.LINK)
        leaf = node.text_node_to_html_node()
        print("testing link to html")
        self.assertTrue(leaf.tag == "a" and 
                         leaf.children == None and 
                         "href" in leaf.props.keys())
        print("")

    def test_image_t2html_func(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        leaf = node.text_node_to_html_node()
        print("testing image to html")
        self.assertTrue(leaf.tag == "img" and 
                         leaf.children == None and 
                         "href" in leaf.props.keys() and
                         leaf.value == "")
        print("")
        
if __name__ == "__main__":
    unittest.main()