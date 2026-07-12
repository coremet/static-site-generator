import unittest
from inline_func import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
# Split delimiters # 6 tests
    def test_not_text(self):
        node = TextNode("This is text with a `code block` word", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a `code block` word", TextType.CODE, None)])

    def test_raise_exp(self):
        node = TextNode("This should be a text with a `code block word", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
    def test_raise_exp2(self):
        node = TextNode("This should be a text with a `code block` word and another `code block word", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_code_delim(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" word", TextType.TEXT, None),
            ])
    
    def test_bold_delim(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("bold", TextType.BOLD, None),
            TextNode(" word", TextType.TEXT, None),
            ])

    def test_italic_delim(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" word", TextType.TEXT, None),
            ])

# extract md images # 2 units  
    def test_extract_md_images1(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_md_images2(self):
        text = "This is text with an image of ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extraction = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extraction, extract_markdown_images(text))

    def test_raise_exp_extract_image1(self):
        node = TextNode("This is a missing image url example with a ![image]()", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = extract_markdown_images(node.text)

# extract md links # 2 units
    def test_extract_md_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extraction = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extraction, extract_markdown_links(text))

    def test_not_extract_images(self):
        text = "This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a link [to example](https://example.com)"
        extraction = [("to example", "https://example.com")]
        self.assertEqual(extraction, extract_markdown_links(text))

    def test_raise_exp_split_link1(self):
        node = TextNode("This is a missing link url example with a [link to]()", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = extract_markdown_links(node.text)

# split nodes image 
    def test_split_image1(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT, None),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT, None),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_image_old(self):
        node = TextNode("This is an image example with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.IMAGE)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is an image example with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.IMAGE, None)], 
            new_nodes
            )

    def test_split_image_no_text(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")], 
            new_nodes
            )



# split nodes links
    def test_split_link1(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_link_old(self):
        node = TextNode("This is an link example with a [link to](https://example.com)", TextType.LINK)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is an link example with a [link to](https://example.com)", TextType.LINK, None)], 
            new_nodes
            )

    def test_split_link_no_text(self):
        node = TextNode("[link to](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("link to", TextType.LINK, "https://example.com")], 
            new_nodes
            )



if __name__ == "__main__":
    unittest.main()