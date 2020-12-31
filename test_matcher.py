import re
import unittest
from io import StringIO

from src.catchers.catcher import Catcher
from src.extra_feature import ExtraFeatureStruct
from src.pattern_matcher import PatternMatcher

str_io = StringIO("    abcdefgd\nbbbb\n# good**aa**  \n  ccc\n")

matcher = PatternMatcher()

f1 = ExtraFeatureStruct(None, None, 0,
                        "test1-id", "test1-class", test_ex="test1-ex")

catch = Catcher("dir")
catch.pattern = re.compile(r"a(.{2}).+\n?", re.IGNORECASE)
catch.addExtraFeature(f1)

catch_t = Catcher("h{}")
catch_t.pattern = re.compile(r"#+\s(.+)\s*\n?", re.IGNORECASE)
catch_t.addExtraFeature(f1)

catch_s = Catcher("strong")
catch_s.pattern = re.compile(r"\*\*([^*]+)\*\*", re.IGNORECASE)
catch_s.addExtraFeature(f1)

catch_d = Catcher("del")
catch_d.pattern = re.compile(r"~~([^~]+)~~", re.IGNORECASE)
catch_d.addExtraFeature(f1)

matcher.addCatcher(catch)
matcher.addCatcher(catch_t)
matcher.addCatcher(catch_s)
matcher.addCatcher(catch_d)


class PatternMatcherTest(unittest.TestCase):
    def test001_match_catchers_success(self):
        """
        测试匹配捕获器
        """
        catcher, inlent_level = matcher.matchCatchers(str_io)

        self.assertEqual(inlent_level, 1)
        self.assertEqual(
            catcher.generateCatchStringSlice(str_io), "abcdefgd\n")

        str_io.seek(0)

    def test002_match_catchers_fail(self):
        str_io.readline()
        catcher, inlent_level = matcher.matchCatchers(str_io)

        self.assertEqual(inlent_level, 0)
        self.assertEqual(catcher.catched, False)

        str_io.seek(0)

    def test003_find_Max_len_matcher_catcher(self):
        res = matcher.findMaxLenghtMatchCatcher("dd# good**aa**sss")

        self.assertEqual(res.start_pos, 2)
        self.assertEqual(res.end_pos, 17)
        self.assertEqual(res.is_find, True)
        self.assertEqual(res.catcher, catch_t)

        str_io.seek(0)

    def test004_find_all_substruct_catcher(self):
        ress = matcher.subSturctMatchCatchers(
            "ddd~~df**ddd**dsf~~ssfs**sfsf** ~~ # dfdf")

        self.assertEqual(len(ress), 3)

        self.assertEqual(ress[0].catcher, catch_d)
        self.assertEqual(ress[1].catcher, catch_s)
        self.assertEqual(ress[2].catcher, catch_t)
    
    def test005_empty_line_inlent_conpute(self):
        level=matcher.getIndentLevel(StringIO("   \n    b"))

        self.assertEqual(level,0)

    def test006_not_complete_inlent_conpute(self):
        level=matcher.getIndentLevel(StringIO("       a\n"))

        self.assertEqual(level,1)

    def test007_no_inlent_conpute(self):
        level=matcher.getIndentLevel(StringIO("a\n"))

        self.assertEqual(level,0)
    
    
    

unittest.main()
