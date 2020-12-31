import unittest

from src.transformers.double_meta_transfromer import DoubleMetaTransformer

test_s_1="[aaa#sfdf](sdsds)"


transformer=DoubleMetaTransformer(test_s_1,"a",None,None)

class DoubleMetaTransformerTest(unittest.TestCase):
    """
    测试双元捕获器
    """
    def test_generate_extra_limitation(self):
        """
        测试生成额外限制条件
        """
        s=transformer.generateExtraLimitation()

        self.assertEqual(s,"sdsds")
    
    def test_generate_html(self):
        html=transformer.generateHtml()

        self.assertEqual(html,
        "<a href=\"sdsds\">aaa#sfdf</a>")
    

unittest.main()