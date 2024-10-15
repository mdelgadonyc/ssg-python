import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="h1", value="Hello, world!", props=None)
        node2 = HTMLNode(tag="h1", value="Hello, world!", props=None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode(tag="h1", value="Hello, world!", props=None)
        node2 = HTMLNode(tag="a", value="Check out www.example.com", props={"href" : "https://www.example.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="Check out www.example.com", props={"href" : "https://www.example.com", "target": "_blank"})
        props = node.props_to_html()
        self.assertEqual(props, ' href="https://www.example.com" target="_blank"')



if __name__ == "__main__":
    unittest.main()