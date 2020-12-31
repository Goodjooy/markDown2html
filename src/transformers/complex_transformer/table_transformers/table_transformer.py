from src.transformers.transformer import Transformer


class TableTransformer(Transformer):
    """
    表格转换器
    """

    def __init__(self,
                 text,
                 id_name,
                 class_name,
                 **tag_limitations) -> None:
        super().__init__(text, tag_name="table", id_name=id_name,
                         class_name=class_name, **tag_limitations)

        self.text_line = self.text.split("\n")

        