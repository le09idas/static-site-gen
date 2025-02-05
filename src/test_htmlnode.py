import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "Some text")
        node2 = HTMLNode("p", "Some text")
        print("testing htmlnode equality")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("p", "Some text")
        node2 = HTMLNode("h1", "Some text")
        print("testing htmlnode inequality")
        self.assertNotEqual(node, node2)

    def test_attribute_is_none(self):
        node = HTMLNode("p", "Some text")
        print("testing htmlnode attribute is None")
        self.assertIsNone(node.children)

if __name__ == "__main__":
    unittest.main()