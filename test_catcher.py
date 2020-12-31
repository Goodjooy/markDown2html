from io import StringIO
from src.catchers.catcher import Catcher
import re
import unittest
from src.extra_feature import ExtraFeatureStruct

f1 = ExtraFeatureStruct(None, None, 0,
                        "test1-id", "test1-class", test_ex="test1-ex")

str_io = StringIO("abcdefgd\nbbbb\nccc\n")
catch = Catcher("dir")
catch.pattern = re.compile(r"a(.{2}).+\n?", re.IGNORECASE)
catch.addExtraFeature(f1)


def readline(str_io):
    s = str_io.readline()
    pos = str_io.tell()
    str_io.seek(pos-len(s))

    return s


class CatcherTest(unittest.TestCase):
    def test002_generate_catch_string(self):
        string = catch.generateCatchStringSlice(str_io)

        self.assertEqual("bbbb\n", readline(str_io))
        self.assertEqual("abcdefgd\n", string)

        str_io.seek(0)

    def test001_match_catcher_not_change_file_fp(self):
        sta = catch.matchCatcher(str_io)

        self.assertEqual("abcdefgd\n", readline(str_io))
        self.assertTrue(sta)

    def test003_generate_transformer(self):
        str_io.seek(0)
        f = ExtraFeatureStruct(None, None, None,
                               "test-id", "test-class", test_ex="test-ex")
        t = catch.generateMatchTransfromer(str_io, f)

        self.assertEqual(t.generateHtml(),
                         "<dir id=\"test-id\" class=\"test-class\" test_ex=\"test-ex\">bc</dir>")

    def test004_match_extra_feature_exist(self):
        is_ok, feature = catch.matchExtraFeatures(None, None, 0)

        self.assertEqual(is_ok, True)
        self.assertEqual(feature, f1)

    def test005_match_extra_feature_not_exist(self):
        is_ok, feature = catch.matchExtraFeatures(None, None, 2)

        self.assertEqual(is_ok, False)
        self.assertEqual(feature.empty, ExtraFeatureStruct.NoneFeature().empty)

    def test006_read_end_action(self):
        a = str_io.readline()
        b = str_io.readline()
        c = str_io.readline()
        e = str_io.readline()

        #print(a, b, c, e, str_io.readable())

        str_io.seek(0)

    def test007_match_catcher_len(self):
        lenght = catch.matchCatherLenght(readline(str_io))

        self.assertEqual(9, lenght)

    def test008_regex_match(self):
        matcher = re.match(r"ddd", "aadddaaddd")

        self.assertEqual(matcher, None)


unittest.main()
