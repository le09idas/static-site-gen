import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    
    def test_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        print("testing ParentNode equality")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("p", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        print("testing ParentNode inequality")
        self.assertNotEqual(node, node2)

    def test_attribute_is_none(self):
        node = ParentNode(
            "p",
            [
                LeafNode("p", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        print("testing ParentNode value attribute is None")
        self.assertIsNone(node.value)

    def test_no_tag_detected(self):
        print("testing ParentNode no tag given exception")
        with self.assertRaises(ValueError):
            node = ParentNode(
                None,
                [
                    LeafNode("p", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            
    
    def test_no_children_detected_none(self):
        print("testing ParentNode no children None given exception")
        with self.assertRaises(ValueError):
            node = ParentNode(
                "p",
                None,
            )
            

    def test_no_children_detected_empty(self):
        print("testing ParentNode no children empty list given exception")
        with self.assertRaises(ValueError):
            node = ParentNode(
                "p",
                [],
            )
            
    
    def test_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("p", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        print("testing ParentNode multiple children test")
        self.assertTrue(len(node.children) > 1)

    def test_nested_parents(self):
        node = ParentNode(
            "p",
            [
                LeafNode("p", "Bold text1"),
                LeafNode(None, "Normal text1"),
                LeafNode("i", "italic text1"),
                LeafNode(None, "Normal text1"),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                node,
                LeafNode("p", "Bold text2"),
                LeafNode(None, "Normal text2"),
                LeafNode("i", "italic text2"),
                LeafNode(None, "Normal text2"),
            ],
        )
        print("testing ParentNode nested parents")
        self.assertTrue(type(node2) == type(node2.children[0]))


if __name__ == "__main__":
    unittest.main()