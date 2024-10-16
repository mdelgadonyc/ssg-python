import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        childnode1 = LeafNode(tag=None, value="Hello, world! Here is some ")
        childnode2 = LeafNode(tag="b", value="bold text")
        childnode3 = LeafNode(tag=None, value=" and some ")
        childnode4 = LeafNode(tag="i", value="italic text")
        childnode5 = LeafNode(tag=None, value=".")
        children = [childnode1, childnode2, childnode3, childnode4, childnode5]
        node = ParentNode(tag="p", children=children)
        html_string = node.to_html()
        self.assertEqual(html_string, '<p>Hello, world! Here is some <b>bold text</b> and some <i>italic text</i>.</p>')

    def test_no_tag_raises_error(self):
        node = ParentNode(tag=None, children=[
            LeafNode(None, "Hello, world!")
        ])

        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), "Missing tag")

    def test_no_children_error(self):
        node = ParentNode(tag="h1")
        
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Missing children")

if __name__ == "__main__":
    unittest.main()