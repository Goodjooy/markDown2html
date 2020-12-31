

class ExtraFeatureStruct(object):

    def __init__(self, parent_type, privous_type, indent_level=0, id_name=None, class_name=None, **othor_featrues) -> None:
        self.privous_type = privous_type
        self.parent_type = parent_type
        self.indent_level = indent_level

        self.id_name = id_name
        self.class_name = class_name

        self.othor_featrues = othor_featrues

        self.empty = False

    @staticmethod
    def NoneFeature():
        """
        生成空白特征
        """
        t = ExtraFeatureStruct(None, None, 0, None, None)
        t.empty = True
        return t
