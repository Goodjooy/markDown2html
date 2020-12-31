import unittest
import re

pattern=re.compile(r"(?<=\|)\s*(\S+?)\s*(?=\|)")


class RegexTest(unittest.TestCase):
    def test_mutpli_group(self):
        s=pattern.findall("|-|-|-|")

        print(s)
unittest.main()