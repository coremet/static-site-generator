import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_return_empty(self):
        node = HTMLNode(props=None)
        expected_string = ""
        self.assertEqual(node.props_to_html(), expected_string)
    
    def test_one_prop(self):
        node = HTMLNode(props={"href": "https://example.com"})
        expected_string = ' href="https://example.com"'
        self.assertEqual(node.props_to_html(), expected_string)

    def test_two_prop(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        expected_string = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_string)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        expected_string = "<p>Hello, world!</p>"
        self.assertEqual(node.to_html(), expected_string )
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Example!", {"href": "https://example.com"})
        expected_string = '<a href="https://example.com">Example!</a>'
        self.assertEqual(node.to_html(), expected_string)

    def test_leaf_no_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        expected_string = "Hello, world!"
        self.assertEqual(node.to_html(), expected_string)