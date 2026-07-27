import unittest
from block_to_html import markdown_to_htmlnode
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headings1(self):
        md = """
# Heading 1 text

This is **bolded** paragraph
text in a p
tag here

### Heading 3 text

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1 text</h1><p>This is <b>bolded</b> paragraph text in a p tag here</p><h3>Heading 3 text</h3><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered1(self):
        md = """- List items correctly
- Item A
- Item B
- Item C"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>List items correctly</li><li>Item A</li><li>Item B</li><li>Item C</li></ul></div>",
        )

    def test_unordered2(self):
        md = """- List items incorrectly
- Item A
-Item B
- Item C"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertNotEqual(
            html,
            "<div><ul><li>List items incorrectly</li><li>Item A</li><li>Item B</li><li>Item C</li></ul></div>",
        )

    def test_ordered1(self):
        md = """1. Order items correctly
2. Item A
3. Item B
4. Item C"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Order items correctly</li><li>Item A</li><li>Item B</li><li>Item C</li></ol></div>",
        )

    def test_ordered2(self):
        md = """1. Order items incorrectly
3. Item A
2. Item B
4. Item C"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertNotEqual(
            html,
            "<div><ol><li>Order items incorrectly</li><li>Item A</li><li>Item B</li><li>Item C</li></ol></div>",
        )

    def test_quote1(self):
        md = "> To be or not to be, that is the question"
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>To be or not to be, that is the question</blockquote></div>",
        )

    def test_quote2(self):
        md = """> Any fool can write code that a computer can understand. 
>Good programmers write code that humans can understand."""
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Any fool can write code that a computer can understand.\nGood programmers write code that humans can understand.</blockquote></div>",
        )

if __name__ == "__main__":
    unittest.main()