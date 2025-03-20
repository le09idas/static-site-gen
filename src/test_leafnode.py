import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "Some text")
        node2 = LeafNode("p", "Some text")
        print("testing LeafNode equality")
        self.assertEqual(node, node2)
        print("")

    def test_not_eq(self):
        node = LeafNode("p", "Some text")
        node2 = LeafNode("h1", "Some text")
        print("testing LeafNode inequality")
        self.assertNotEqual(node, node2)
        print("")

    def test_children_is_none(self):
        node = LeafNode("p", "Some text")
        print("testing LeafNode attribute is None")
        self.assertIsNone(node.children)
        print("")

    def test_no_value_detected(self):
        print("testing LeafNode no value given exception")
        with self.assertRaises(ValueError):
            node = LeafNode(None, "p", {"href": "localhost:8080"})
        print("")
            


if __name__ == "__main__":
    unittest.main()