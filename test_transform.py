import re
import unittest

from src.transformers.transformer import Transformer



transformer=Transformer("#### test-String","h{}",
"test-id","test-class",width="600")
transformer.pattern=re.compile(r"^(#+)\s(.+)$",re.IGNORECASE)
transformer.tag_group_id=1
transformer.group_id=2

class TramsformTest(unittest.TestCase):

    def test_tag_generate(self):
        """
        docstring
        """
        out_str=transformer.generateTag()

        self.assertEqual(out_str,"h4")

    def test_tag_id_generate(self):
        out_str=transformer.generateEmptyTag()
        print(out_str)

        self.assertEqual(
            "<h4 id=\"test-id\" class=\"test-class\" width=\"600\">%s</h4>",out_str)

    def test_body_generate(self):
        out_str=transformer.generateTagBody()

        print(out_str)

        self.assertEqual(out_str,"test-String")
    
    def test_html_tag_generate(self):
        out_str=transformer.generateHtml()
        print(out_str)
        self.assertEqual(out_str,"<h4 id=\"test-id\" class=\"test-class\" width=\"600\">test-String</h4>","pass!")

unittest.main()