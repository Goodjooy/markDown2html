import functools
import re
from src.substrunct_catcher import SubstructCatcherStruct
from src.extra_feature import ExtraFeatureStruct
from src.err.pattern_not_match_error import PatternNotMatchError


class Transformer(object):
    def __init__(self, text,
                 tag_name="div",
                 id_name=None,
                 class_name=None,
                 **tag_limitations
                 ) -> None:
        self.pattern = re.compile(r'(.*)', re.IGNORECASE)
        self.group_id = 1

        self.tag_group_id = -1

        self.text = text

        self.tag_name: str = tag_name

        self.id_name = id_name
        self.class_name = class_name

        self.tag_limitations = tag_limitations

        self.catch = None
        self.match = None

        self.feature: ExtraFeatureStruct = None

    def generateTag(self):
        if self.need_tag_info_from_text():
            return self.tag_name.format(self.catch_tag_from_text())
        else:
            return self.tag_name

    def generateEmptyTag(self):
        tag_limits = functools.reduce(
            lambda x, y: f"{x} {y[0]}=\"{y[1]}\"",
            self.tag_limitations.items(), "")
        id_limit = (" id=\"%s\"" % self.id_name) if self.need_id() else ""
        class_limit = (" class=\"%s\"" %
                       self.class_name) if self.need_class() else ""
        return "<{0}{1}{2}{3}>%s</{0}>".format(self.generateTag(),
                                               id_limit,
                                               class_limit,
                                               tag_limits)

    def generateTagBody(self):
        return self.generateBodyStruct()

    def generateHtml(self):
        return self.generateEmptyTag() % (self.generateTagBody())

    def need_id(self):
        """
        need id
        """
        return self.id_name != None

    def need_class(self):
        """
        need class
        """
        return self.class_name != None

    def generateBodyStruct(self):
        body = self.catch_body()
        substructs = self.catch_substruct(body)

        for substruct in substructs:
            substruct: SubstructCatcherStruct
            html = substruct.catcher.generateSubStructMatchTransformer(
                body[substruct.start_pos:substruct.end_pos],
                self.feature).generateHtml()

            body.replace(
                body[substruct.start_pos:substruct.end_pos], html)
        return body

    def catch_substruct(self, text):
        if self.match is None:
            return []
        return self.match.subSturctMatchCatchers(text)

    def catch_body(self):
        """
        获取文本
        """
        match = self.pattern.match(self.text)
        if match is None:
            raise PatternNotMatchError(self.text, self.pattern.pattern)
        else:
            return match.group(self.group_id)

    def catch_tag_from_text(self):
        match = self.pattern.match(self.text)
        if match is None:
            raise PatternNotMatchError(self.text, self.pattern.pattern)
        else:
            return self.tag_transfrom(match.group(self.tag_group_id)
                                      )

    def need_tag_info_from_text(self):
        if self.tag_group_id == -1:
            return False
        return True

    def tag_transfrom(self, data):
        return str(len(data))

    def setCatcher(self, catcher):
        self.catch = catcher

    def setMatcher(self, match):
        self.match = match
