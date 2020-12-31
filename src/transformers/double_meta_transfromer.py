# TODO 二元匹配的MD转换器
# 如 [example](http://example.com) or ![example](http://example.com)
from src.err.pattern_not_match_error import PatternNotMatchError
from src.transformers.transformer import Transformer
import re


class DoubleMetaTransformer(Transformer):
    def __init__(self,
                 text,
                 tag_name,
                 id_name,
                 class_name,
                 **tag_limitations) -> None:
        super().__init__(text, tag_name=tag_name, id_name=id_name,
                         class_name=class_name, **tag_limitations)

        self.pattern = re.compile(r'\[(.+?)]\(([^<>]+)\)', re.IGNORECASE)

        self.group_id = 1
        self.extra_id = 2
        self.extra_name = "href"

        self.tag_limitations[self.extra_name] = ""

    def generateExtraLimitation(self):
        match = self.pattern.match(self.text)
        if match is None:
            raise PatternNotMatchError(self.text, self.pattern.pattern)
        else:
            return match.group(self.extra_id)

    def updateExtraLimtation(self):
        self.tag_limitations[
            self.extra_name] = self.generateExtraLimitation()

    def generateEmptyTag(self):
        self.updateExtraLimtation()
        return super().generateEmptyTag()
