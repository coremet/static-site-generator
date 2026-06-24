import unittest
from htmlnode import HTMLNode

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