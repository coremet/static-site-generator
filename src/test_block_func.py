import unittest
from block_func import markdown_to_blocks, BlockType, block_to_blocktype

class TestTextNode(unittest.TestCase):
# 
    def test_markdown_to_blocks1(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks2(self):
        md = """
This is _italic_ paragraph



This is another paragraph with **bold** text




This is a new paragraph on a new line with `code`

- This is a list
- with items

- and further items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is _italic_ paragraph",
                "This is another paragraph with **bold** text",
                "This is a new paragraph on a new line with `code`",
                "- This is a list\n- with items",
                "- and further items",
            ],
        )

    def test_block_to_type_headings(self):
        md_block = "# Heading text"
        block_type = block_to_blocktype(md_block)
        self.assertEqual(block_type, BlockType.HEADINGS)
    
    def test_block_to_type_code(self):
        md_block ="""```
        Code block
        ```"""
        block_type = block_to_blocktype(md_block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_type_quote1(self):
        md_block = ">This is a quote block"
        block_type = block_to_blocktype(md_block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_type_quote2(self):
        md_block = "> This is another quote block"
        block_type = block_to_blocktype(md_block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_type_quote3(self):
        md_block ="""> This is another quote block
> that has multiple
> quotes"""
        block_type = block_to_blocktype(md_block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_type_unordered1(self):
        md_block = """- Let us
- write
- an unordered
- list"""
        block_type = block_to_blocktype(md_block)
        self.assertEqual(block_type, BlockType.UNORDERED)

    def test_block_to_type_unordered2(self):
        md_block ="""-Let us
-write
-an incorrectly formatted
-unordered list"""
        block_type = block_to_blocktype(md_block)
        self.assertNotEqual(block_type, BlockType.UNORDERED)

    def test_block_to_type_ordered1(self):
        md_block = """1. Let us
2. write
3. an ordered
4. list"""
        block_type = block_to_blocktype(md_block)
        self.assertEqual(block_type, BlockType.ORDERED)

    def test_block_to_type_ordered2(self):
        md_block ="""1. Let us
3. write
2. an incorrectly formatted
4. unordered list"""
        block_type = block_to_blocktype(md_block)
        self.assertNotEqual(block_type, BlockType.ORDERED)

    def test_block_to_type_ordered3(self):
        md_block ="""1.Let us
2. write
3. an incorrectly formatted
4. unordered list"""
        block_type = block_to_blocktype(md_block)
        self.assertNotEqual(block_type, BlockType.ORDERED)

    def test_block_to_type_normal(self):
        md_block = """I am going
    to write a normal 
    paragraph block"""
        block_type = block_to_blocktype(md_block)
        self.assertEqual(block_type, BlockType.NORMAL)

if __name__ == "__main__":
    unittest.main()