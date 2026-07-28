from extract_title import extract_title
import unittest

class TestExtractedTitle(unittest.TestCase):
    def test_raise_exp(self):
        md_header = "## This is a h2 header"
        with self.assertRaises(Exception):
            extracted_title = extract_title(md_header)

    def test_extract_title1(self):
        md_header = "# This is a h1 header"
        extracted_title = extract_title(md_header)
        self.assertEqual(extracted_title, "This is a h1 header")

    def test_extract_title2(self):
        md_block = """# This is a h1 header
in the middle of
a markdown block """
        extracted_title = extract_title(md_block)
        self.assertEqual(extracted_title, "This is a h1 header")
    
if __name__ == "__main__":
    unittest.main()