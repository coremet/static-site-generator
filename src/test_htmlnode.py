import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase): # 3 tests
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

class TestLeafNode(unittest.TestCase): # 4 tests
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

class TestParentNode(unittest.TestCase): # 9 tests
    def test_no_tag_error(self): # see pythonic version below
        child_nodes = []
        ch_node = LeafNode("p", "Hello, world!")
        child_nodes.append(ch_node)
        node = ParentNode(None, child_nodes)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_child_error(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    # following are .to_html unit tests - 7 tests
    def test_one_child(self):
        child_nodes = [LeafNode("b", "Hello, world!")] 
        node = ParentNode("p", child_nodes)
        expected_string = "<p><b>Hello, world!</b></p>"
        self.assertEqual(node.to_html(), expected_string)

    def test_one_ch_prop(self):
        child_nodes = [LeafNode("a", "Example!", {"href": "https://example.com"})] 
        node = ParentNode("p", child_nodes)
        expected_string = '<p><a href="https://example.com">Example!</a></p>'
        self.assertEqual(node.to_html(), expected_string)
    
    def test_two_children(self):
        child_nodes = [LeafNode("b", "Hello, world!"), LeafNode("i", "How are you?")] 
        node = ParentNode("p", child_nodes)
        expected_string = "<p><b>Hello, world!</b><i>How are you?</i></p>"
        self.assertEqual(node.to_html(), expected_string)

    def test_one_parent(self):
        child_nodes = [LeafNode("b", "Hello, world!"), LeafNode("i", "How are you?")] 
        parent_nodes = [ParentNode("p", child_nodes)]
        node = ParentNode("code", parent_nodes)
        expected_string = "<code><p><b>Hello, world!</b><i>How are you?</i></p></code>"
        self.assertEqual(node.to_html(), expected_string)
    
    def test_two_parents(self):
        child_nodes = [LeafNode("b", "Hello, world!"), LeafNode("i", "How are you?")]
        child_nodes2 = [LeafNode("b", "Rise and grind"), LeafNode("i", "Let's move it!")] 
        parent_nodes = [ParentNode("p", child_nodes), ParentNode("p", child_nodes2)]
        node = ParentNode("code", parent_nodes)
        expected_string = "<code><p><b>Hello, world!</b><i>How are you?</i></p><p><b>Rise and grind</b><i>Let's move it!</i></p></code>"
        self.assertEqual(node.to_html(), expected_string)    

    def test_two_parents_prop(self):
        child_nodes = [LeafNode("b", "Hello, world!"), LeafNode("a", "Example!", {"href": "https://example.com"})]
        child_nodes2 = [LeafNode("b", "Rise and grind"), LeafNode("a", "The same?", {"href": "https://different.com"})] 
        parent_nodes = [ParentNode("p", child_nodes), ParentNode("p", child_nodes2)]
        node = ParentNode("code", parent_nodes)
        expected_string = '<code><p><b>Hello, world!</b><a href="https://example.com">Example!</a></p><p><b>Rise and grind</b><a href="https://different.com">The same?</a></p></code>'
        self.assertEqual(node.to_html(), expected_string)

    def test_two_grandparents(self):
        child_nodes = [LeafNode("h1", "Where is this going?")]
        pa_ch_nodes = [LeafNode("b", "Hello, world!"), ParentNode("i", child_nodes)]
        child_nodes2 = [LeafNode("b", "Rise and grind"), LeafNode("i", "Let's move it!")] 
        parent_nodes = [ParentNode("p", pa_ch_nodes), ParentNode("p", child_nodes2)]
        node = ParentNode("code", parent_nodes)
        expected_string = "<code><p><b>Hello, world!</b><i><h1>Where is this going?</h1></i></p><p><b>Rise and grind</b><i>Let's move it!</i></p></code>"
        self.assertEqual(node.to_html(), expected_string) 


 