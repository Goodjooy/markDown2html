from io import TextIOWrapper
import re
from src.extra_feature import ExtraFeatureStruct
from .catcher import Catcher
from ..transformers.link_transformer import LinkTransformer


class LinkCatcher(Catcher):
    """
    链接捕获
    """

    def __init__(self) -> None:
        super().__init__(tag_name="a")

        self.pattern = re.compile(r'(?!<!)\[(.+?)]\(([^<>]+)\)', re.IGNORECASE)

    def generateSubStructMatchTransformer(self, text, feature: ExtraFeatureStruct):

        t = LinkTransformer(
            text,
            feature.id_name,
            feature.class_name,
            **feature.othor_featrues
        )

        t.setCatcher(self)
        t.setMatcher(self.marcher)
        t.feature = feature

        return t
