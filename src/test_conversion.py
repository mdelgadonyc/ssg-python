import unittest
from textnode import TextNode, TextType, text_node_to_html
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_node_to_html_bold(self):
        text_node = TextNode("This is a text node", TextType.BOLD)
        leaf_node1 = text_node_to_html(text_node)
        leaf_node2 = LeafNode(tag="b", value="This is a text node")
        self.assertEqual(leaf_node1, leaf_node2)

    def test_node_to_html_italic(self):
        text_node = TextNode("This is a text node", TextType.ITALIC)
        leaf_node1 = text_node_to_html(text_node)
        leaf_node2 = LeafNode(tag="i", value="This is a text node")
        self.assertEqual(leaf_node1, leaf_node2)

    def test_node_to_html_wrong_type(self):
        node = TextNode("This is a text node", TextType.UNKNOWN)
        with self.assertRaises(ValueError) as context:
            text_node_to_html(node)
        self.assertEqual(str(context.exception), "Invalid text type")

if __name__ == "__main__":
    unittest.main()