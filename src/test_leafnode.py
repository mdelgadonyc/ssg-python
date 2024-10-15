import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag="h1", value="Hello, world!")
        node2 = LeafNode(tag="h1", value="Hello, world!")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = LeafNode(tag="h1", value="Hello, world!")
        node2 = LeafNode(tag="p", value="Not a header")
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = LeafNode(tag="a", value="Check out www.example.com", props={"href" : "https://www.example.com", "target": "_blank"})
        props = node.props_to_html()
        self.assertEqual(props, ' href="https://www.example.com" target="_blank"')

    def test_to_html(self):
        node = LeafNode(tag="a", value="Check out www.example.com", props={"href" : "https://www.example.com", "target": "_blank"})
        html_string = node.to_html()
        self.assertEqual(html_string, '<a href="https://www.example.com" target="_blank">Check out www.example.com</a>')


if __name__ == "__main__":
    unittest.main()