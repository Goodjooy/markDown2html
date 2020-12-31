import re
from src.transformers.transformer import Transformer


class TableHeadTransfromer(Transformer):
    def __init__(self,
                 text_head,
                 text_justify,
                 id_name,
                 class_name,
                 **tag_limitations) -> None:
        super().__init__(f"{text_head}\n{text_justify}",
                         tag_name="thead",
                         id_name=id_name,
                         class_name=class_name,
                         **tag_limitations)

        self.pattern = re.compiler(r"(?<=\|)\s*(\S+?)\s*(?=\|)",
                                   re.IGNORECASE)

    # TODO :完全嵌套体,后续由表格头原子转换器完成
