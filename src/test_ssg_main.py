import unittest
from ssg_main import markdown_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode

class TestMarkdownToHtml(unittest.TestCase):
     def test_markdown_to_html_node_paragraph(self):
          markdown = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
          block_result = markdown_to_html_node(markdown)

          block_expected = [
               HTMLNode(tag="p", value=None, children=[
                         HTMLNode(tag=None, value="This is a paragraph of text. It has some ", children=None, props=None), 
                         HTMLNode(tag="strong", value=None, children=
                                   HTMLNode(tag=None, value="bold", children=None, props=None), 
                                   props=None), 
                         HTMLNode(tag=None, value=" and ", children=None, props=None), 
                         HTMLNode(tag="em", value=None, children=
                                   HTMLNode(tag=None, value="italic", children=None, props=None), 
                                   props=None), 
                         HTMLNode(tag=None, value=" words inside of it.", children=None, props=None)
               ], props=None)
          ]
          block_expected = HTMLNode(tag="div", children=block_expected)
          self.assertEqual(block_result, block_expected)
          
     def test_markdown_to_html_node_heading(self):
        markdown = "# This is a heading"
        block_result = markdown_to_html_node(markdown)

        block_expected = [
             HTMLNode(tag="h1", value=None, children=[
                        HTMLNode(tag=None, value="This is a heading", children=None, props=None),
             ], props=None)
        ]
        block_expected = HTMLNode(tag="div", children=block_expected)
        self.assertEqual(block_result, block_expected)
        
     def test_markdown_to_html_node_unordered_list(self):
        markdown = """* This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        block_result = markdown_to_html_node(markdown)

        block_expected = [
             HTMLNode(tag="ul", value=None, children=[
                        HTMLNode(tag="li", value=None, children=
                                 HTMLNode(tag=None, value="This is the first list item in a list block", children=None, props=None), props=None),
                        HTMLNode(tag="li", value=None, children=
                                 HTMLNode(tag=None, value="This is a list item", children=None, props=None), props=None),
                        HTMLNode(tag="li", value=None, children=
                                 HTMLNode(tag=None, value="This is another list item", children=None, props=None), props=None),
                        
             ], props=None)
        ]
        block_expected = HTMLNode(tag="div", children=block_expected)
        self.assertEqual(block_result, block_expected)

     def test_markdown_to_html_node_ordered_list(self):
        markdown = """1. This is the first list item in a list block
        2. This is the second item
        3. This is the third list item"""
        block_result = markdown_to_html_node(markdown)

        block_expected = [
             HTMLNode(tag="ol", value=None, children=[
                        HTMLNode(tag="li", value=None, children=
                                 HTMLNode(tag=None, value="This is the first list item in a list block", children=None, props=None), props=None),
                        HTMLNode(tag="li", value=None, children=
                                 HTMLNode(tag=None, value="This is the second item", children=None, props=None), props=None),
                        HTMLNode(tag="li", value=None, children=
                                 HTMLNode(tag=None, value="This is the third list item", children=None, props=None), props=None),
                        
             ], props=None)
        ]
        block_expected = HTMLNode(tag="div", children=block_expected)
        self.assertEqual(block_result, block_expected)

     def test_markdown_to_html_node_quoteblock(self):
         markdown = '> “Friendship is born at the moment when one man says to another "What! You too? I thought that no one but myself.” ~C.S. Lewis, The Four Loves'
         block_result = markdown_to_html_node(markdown)
         block_expected = [
             HTMLNode(tag="blockquote", value=None, children=[
                 HTMLNode(tag=None, value='“Friendship is born at the moment when one man says to another "What! You too? I thought that no one but myself.” ~C.S. Lewis, The Four Loves', children=None, props=None),
             ], props=None)
        ]
         block_expected = HTMLNode(tag="div", children=block_expected)
         self.assertEqual(block_result, block_expected)

     def test_markdown_to_html_node_code_inline(self):
         markdown = "At the command prompt, type `nano`."
         block_result = markdown_to_html_node(markdown)
         block_expected = [
             HTMLNode(tag="p", value=None, children=[
                 HTMLNode(tag=None, value="At the command prompt, type ", children=None, props=None),
                 HTMLNode(tag="code", value=None, children=[
                     HTMLNode(tag=None, value="nano", children=None, props=None),
                 ], props=None),
                 HTMLNode(tag=None, value=".", children=None, props=None),
             ], props=None),     
          ]
         
         block_expected = HTMLNode(tag="div", children=block_expected)
         self.assertEqual(block_result, block_expected)

     def test_markdown_to_html_node_codeblock(self):
         markdown = """```
         def say_hello():
          print("Hello world!")
          ```"""
         block_result = markdown_to_html_node(markdown)
         block_expected = [
             HTMLNode(tag="pre", value=None, children=[
                 HTMLNode(tag="code", value=None, children=[
                     HTMLNode(tag=None, value='def say_hello():\nprint("Hello world!")', children=None, props=None),
                 ], props=None),
             ], props=None)
          ]
         block_expected = HTMLNode(tag="div", children=block_expected)
         self.assertEqual(block_result, block_expected)
     
     def test_markdown_to_html_node_blocks(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""

        header_block = [
             HTMLNode(tag="h1", value=None, children=[
                        HTMLNode(tag=None, value="This is a heading", children=None, props=None),
             ], props=None)
        ]

        paragraph_block = [
             HTMLNode(tag="p", value=None, children=[
                        HTMLNode(tag=None, value="This is a paragraph of text. It has some ", children=None, props=None), 
                        HTMLNode(tag="strong", value=None, children=
                                HTMLNode(tag=None, value="bold", children=None, props=None), 
                                props=None), 
                        HTMLNode(tag=None, value=" and ", children=None, props=None), 
                        HTMLNode(tag="em", value=None, children=
                                HTMLNode(tag=None, value="italic", children=None, props=None), 
                                props=None), 
                        HTMLNode(tag=None, value=" words inside of it.", children=None, props=None)
             ], props=None)
        ]

        list_block = [
             HTMLNode(tag="ul", value=None, children=[
                        HTMLNode(tag="li", value=None, children=
                                 HTMLNode(tag=None, value="This is the first list item in a list block", children=None, props=None), props=None),
                        HTMLNode(tag="li", value=None, children=
                                 HTMLNode(tag=None, value="This is a list item", children=None, props=None), props=None),
                        HTMLNode(tag="li", value=None, children=
                                 HTMLNode(tag=None, value="This is another list item", children=None, props=None), props=None),
                        
             ], props=None)
        ]

        blocks = [
            *header_block,
            *paragraph_block,
            *list_block
        ]

        blocks_expected = HTMLNode(tag="div", children=blocks, props=None)
        blocks_result = markdown_to_html_node(markdown)
        self.assertEqual(blocks_result, blocks_expected)

if __name__ == "__main__":
    unittest.main()