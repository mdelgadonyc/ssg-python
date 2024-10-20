import unittest
#from textnode import TextNode, TextType
from markdown_detector import *

class TestMarkdownDetector(unittest.TestCase):
    def test_detect_heading_2(self):
        markdown_text = "## This is a heading"
        type_result = block_to_block_type(markdown_text)
        self.assertEqual("heading", type_result)

    def test_detect_codeblock(self):
        markdown_text = "```This is a codeblock```"
        type_result = block_to_block_type(markdown_text)
        self.assertEqual("codeblock", type_result)

    def test_detect_quoteblock(self):
        markdown_text = "> This is the first line of a quote\n> This is the second line"
        type_result = block_to_block_type(markdown_text)
        self.assertEqual("quoteblock", type_result)

    def test_detect_unordered(self):
        markdown_text = "* an item\n* another item\n* one last item"
        type_result = block_to_block_type(markdown_text)
        self.assertEqual("unordered_list", type_result)

    def test_detect_ordered(self):
        markdown_text = "1. the first item\n2. the second item\n3. third item"
        type_result = block_to_block_type(markdown_text)
        self.assertEqual("ordered_list", type_result)

    def test_detect_normal(self):
        markdown_text = "too many pounds to be a heading"
        type_result = block_to_block_type(markdown_text)
        self.assertEqual("normal", type_result)
