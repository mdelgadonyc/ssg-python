import unittest
from textnode import TextNode, TextType
from markdown_parser import split_nodes_delimiter

class TestMarkdownParser(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        old_node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "`", TextType.CODE)

        new_nodes2 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, new_nodes2)        

    def test_split_nodes_delimiter_bold(self):
        old_node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)

        new_nodes2 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, new_nodes2)    
        
    def test_split_nodes_delimiter_italic(self):
        old_node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "*", TextType.ITALIC)

        new_nodes2 = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, new_nodes2)    

    

if __name__ == "__main__":
    unittest.main()