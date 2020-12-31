from io import TextIOWrapper
import re
from typing import Text
from src.extra_feature import ExtraFeatureStruct
from .catcher import Catcher

from ..transformers.paragraph_transformer import ParagraphTransformer


class ParagraphCatcher(Catcher):
    """
    段落捕获器
    """

    def __init__(self) -> None:
        super().__init__(tag_name="p")

        self.pattern = re.compile(r"^(:?\*|-)\s(.+)$\n", re.IGNORECASE)

    def substructMatchCatcher(self, text: str):
        return False

    def generateSubStructMatchTransformer(self,
                                          text,
                                          feature: ExtraFeatureStruct):
        t = ParagraphTransformer(
            text, feature.id_name, feature.class_name, **feature.othor_featrues)

        t.setCatcher(self)
        t.setMatcher(self.marcher)
        t.feature = feature

        return t
