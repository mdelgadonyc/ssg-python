import unittest
from textnode import TextNode, TextType
from markdown_parser import *


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

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = extract_markdown_images(text)
        expected_images = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted_images, expected_images)

    def test_extract_markdown_no_images(self):
        text = "This is text with a missing image"
        extracted_images = extract_markdown_images(text)
        expected_images = []
        self.assertEqual(extracted_images, expected_images)
        

    def test_extract_markdown_no_alt_text(self):
        text = "Empty alt: ![](http://example.com/cat.jpg)"
        extracted_images = extract_markdown_images(text)
        expected_images = [('', "http://example.com/cat.jpg")]
        self.assertEqual(extracted_images, expected_images)


    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = extract_markdown_links(text)
        expected_links = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extracted_links, expected_links)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", 
            TextType.TEXT
            )
        
        expected_node = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev") ]
        new_nodes = split_nodes_link(node)
        self.assertEqual(new_nodes, expected_node)

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT
            )
        
        expected_node = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg") ]
        new_nodes = split_nodes_image(node)
        self.assertEqual(new_nodes, expected_node)        
            
if __name__ == "__main__":
    unittest.main()