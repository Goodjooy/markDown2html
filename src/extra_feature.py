import src.transformers.transformer


class ExtraFeatureStruct(object):

    def __init__(self, parent_type, privous_type, indent_level=0, id_name=None, class_name=None) -> None:
        self.privous_type = privous_type
        self.parent_type = parent_type
        self.indent_level = indent_level

        self.id_name = id_name
        self.class_name = class_name
