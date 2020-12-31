import re

from .transformer import Transformer


class TitleTransfromer(Transformer):

    def __init__(self, text, id_name, class_name, **tag_limitations) -> None:
        super().__init__(text, tag_name="h{}", id_name=id_name,
                         class_name=class_name, **tag_limitations)

        self.pattern = re.compile(r"^(#+)\s+(.+)\s*$\n")

        self.group_id = 2
        self.tag_group_id = 1

    def tag_transfrom(self, data):
        return str(len(data))
