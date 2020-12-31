import re
from .double_meta_transfromer import DoubleMetaTransformer


class LinkTransformer(DoubleMetaTransformer):
    """
    超链接捕获
    """

    def __init__(self,
                 text,
                 id_name,
                 class_name,
                 **tag_limitations) -> None:
        super().__init__(text,
                         "a",
                         id_name,
                         class_name,
                         **tag_limitations)

        self.pattern = re.compile(r'(?!<!)\[(.+?)]\(([^<>]+)\)', re.IGNORECASE)

        self.group_id = 1
        self.extra_id = 2

        self.extra_name = "href"

    def generate_substrunct(self):
        return []