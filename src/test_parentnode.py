import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    
    def test_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text"),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text"),
            ],
        )
        print("testing ParentNode equality")
        self.assertEqual(node, node2)
        print("")

    def test_not_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "p"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text")
            ],
        )
        node2 = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text")
            ],
        )
        print("testing ParentNode inequality")
        self.assertNotEqual(node, node2)
        print("")

    def test_attribute_is_none(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "p"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text")
            ]
        )
        print("testing ParentNode value attribute is None")
        self.assertIsNone(node.value)
        print("")

    def test_no_tag_detected(self):
        print("testing ParentNode no tag given exception")
        with self.assertRaises(ValueError):
            node = ParentNode(
                None,
                [
                    LeafNode("Bold text", "p"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text")
                ],
            )
        print("")
            
    
    def test_no_children_detected_none(self):
        print("testing ParentNode no children None given exception")
        with self.assertRaises(ValueError):
            node = ParentNode(
                "p",
                None
            )
        print("")   

    def test_no_children_detected_empty(self):
        print("testing ParentNode no children empty list given exception")
        with self.assertRaises(ValueError):
            node = ParentNode(
                "p",
                []
            )
        print("")    
    
    def test_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "p"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text")
            ]
        )
        print("testing ParentNode multiple children test")
        self.assertTrue(len(node.children) > 1)
        print("")

    def test_nested_parents(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "p"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text")
            ],
        )
        node2 = ParentNode(
            "p",
            [
                node,
                LeafNode("Bold text2", "p"),
                LeafNode("Normal text2"),
                LeafNode("italic text2", "i"),
                LeafNode("Normal text2")
            ],
        )
        print("testing ParentNode nested")
        self.assertTrue(type(node2) == type(node2.children[0]))
        print("")

if __name__ == "__main__":
    unittest.main()