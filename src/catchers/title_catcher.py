from io import TextIOWrapper
import re
from src.extra_feature import ExtraFeatureStruct
from typing import Text
from .catcher import Catcher
from ..transformers.title_transformer import TitleTransfromer


class TitleCatcher(Catcher):
    """
    标题捕获器
    """

    def __init__(self) -> None:
        super().__init__(tag_name="h1")

        self.pattern = re.compile(r"^(#+)\s+(.+)$\n")

    def substructMatchCatcher(self, text: str):
        return False

    def generateSubStructMatchTransformer(self,
                                          text,
                                          feature: ExtraFeatureStruct):
        t = TitleTransfromer(text, feature.id_name, feature.class_name,
                             **feature.othor_featrues)
        t.setCatcher(self)
        t.setMatcher(self.marcher)
        t.feature = feature
        return t
