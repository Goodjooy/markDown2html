import re
from .transformer import Transformer


class ParagraphTransformer(Transformer):
    """
    段落转发器
    """

    def __init__(self,
                 text, id_name,
                 class_name,
                 **tag_limitations) -> None:
        super().__init__(text, tag_name="p", id_name=id_name,
                         class_name=class_name, **tag_limitations)

        self.pattern=re.compile(r"^(?:\*|-)\s+(.+)$\n",re.IGNORECASE)
        