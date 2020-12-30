

from io import TextIOWrapper
import re

from src.catchers.catcher import Catcher
from src.substrunct_catcher import SubstructCatcherStruct


class test(object):
    def generateHtml(x): return "test-page"


def sub_sturct_match():
    """
    docstring
    """
    t = test()

    return t, 0, 15


class PatternMatcher(object):
    def __init__(self) -> None:
        self.catchers = []

        self.indent_lenght = 4

        self.privous_

    def addCatcher(self, catcher):
        self.catchers.append(catcher)

    def matchCatchers(self, file_handle: TextIOWrapper):
        inlent_level = self.getIndentLevel(file_handle)
        for catcher in self.catchers:
            catcher: Catcher
            if catcher.matchCatcher(file_handle):
                return catcher, inlent_level
        return Catcher.faliureCatcher(), inlent_level

    def subSturctMatchCatchers(self, text):
        """
        嵌套结构匹配
        """
        all_substructs = []

        start_pos = 0

        cahtcher_struct = self.update_substruct_catcher(
            self.findMaxLenghtMatchCatcher(text), start_pos)
        start_pos = cahtcher_struct.end_pos
        all_substructs.append(cahtcher_struct)

        while cahtcher_struct.is_find:
            cahtcher_struct = self.update_substruct_catcher(
                self.findMaxLenghtMatchCatcher(text[start_pos:]),
                start_pos=start_pos
            )
            start_pos = cahtcher_struct.end_pos
            all_substructs.append(cahtcher_struct)

        return all_substructs

    def findMaxLenghtMatchCatcher(self, text):
        max_lenght = -1
        min_start = -1
        min_end = -1
        catcher_ret = None

        # 查找距离起点最近，长度最长的匹配
        for catcher in self.catchers:
            catcher: Catcher
            matcher = catcher.getMatcherCatcherMatcher(text)
            if matcher is not None:
                match_len = matcher.group(0)
                start = matcher.start(0)
                if(max_lenght <= match_len and min_start >= start):
                    max_lenght = match_len
                    min_start = start
                    catcher_ret = catcher
                    min_end = matcher.end(0)
        if catcher_ret is None:
            find = False
        else:
            find = True

        t = SubstructCatcherStruct()
        t.catcher = catcher_ret
        t.end_pos = min_end
        t.start_pos = min_start
        t.match_len = max_lenght
        t.is_find = find

        return t

    def update_substruct_catcher(self,
                                 cathcer_struct: SubstructCatcherStruct,
                                 start_pos):
        cathcer_struct.start_pos += start_pos
        cathcer_struct.end_pos += start_pos

        return cathcer_struct

    def getIndentLevel(self, file_handle: TextIOWrapper):
        """
        获取缩进
        """
        count = 0
        char = file_handle.read(1)
        while re.match(r'\s', char):
            count += 1

            char = file_handle.read(1)

        file_handle.seek(file_handle.tell()-1)

        return count // self.indent_lenght
