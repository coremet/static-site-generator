import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase): # 6 tests
    def test_eq(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        node2 = TextNode("This is a italic node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a code node", TextType.CODE)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a italic node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        node = TextNode("This is an exampe link node", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a different link node", TextType.LINK, "https://different.com")
        self.assertNotEqual(node, node2)
    
    def test_not_eq4(self):
        node = TextNode("This is an example link node", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, None)
        self.assertNotEqual(node, node2)

# text_node_to_html_node # 6 tests
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://example.com"})
    
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://different.com" )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://different.com","alt": "This is an image node"})
    
if __name__ == "__main__":
    unittest.main()