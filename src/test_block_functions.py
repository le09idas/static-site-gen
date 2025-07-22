import unittest

from textnode import *
from htmlnode import HTMLNode
from block_functions import *

class TestBlockFunctions(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = BlockFunc.markdown_to_blocks(md)
        print("Testing markdown_to_blocks function base case...")
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        print("Test successful!")
        print("")

    def test_markdown_to_blocks_single_line(self):
        md = """
This is **bolded** paragraph
"""
        blocks = BlockFunc.markdown_to_blocks(md)
        print("Testing markdown_to_blocks function single line..")
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph"
            ],
        )
        print("Test successful!")
        print("")

    def test_markdown_to_blocks_with_extra_newlines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = BlockFunc.markdown_to_blocks(md)
        print("Testing markdown_to_blocks function extra newlines...")
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        print("Test successful!")
        print("")

    def test_markdown_to_blocks_empty(self):
        md = """
"""
        blocks = BlockFunc.markdown_to_blocks(md)
        print("Testing markdown_to_blocks function empty...")
        self.assertEqual(
            blocks,
            [],
        )
        print("Test successful!")
        print("")