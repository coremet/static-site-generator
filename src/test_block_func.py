import unittest
from block_func import markdown_to_blocks

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


if __name__ == "__main__":
    unittest.main()