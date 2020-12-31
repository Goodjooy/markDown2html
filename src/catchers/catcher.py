import re
from io import TextIOWrapper
from typing import IO

import pysnooper
from src.err.pattern_not_match_error import PatternNotMatchError
from src.extra_feature import ExtraFeatureStruct
from src.transformers.transformer import Transformer


class Catcher(object):

    def __init__(self, tag_name="div") -> None:
        self.catched = True
        self.pattern = re.compile(r"\n", re.IGNORECASE)

        self.tag_name = tag_name
        self.extra_features = []

        self.marcher = ...

    @staticmethod
    def faliureCatcher():
        """
        未找到的格式捕获器
        """
        t = Catcher("")
        t.catched = False
        return t

    def setMatcher(self, mathcher):
        self.marcher = mathcher

    def matchCatcher(self, fileHandle: TextIOWrapper):
        try:
            pos = fileHandle.tell()
            text = fileHandle.readline()
            matcher = self.pattern.match(text)
            if matcher is None:
                return False
            return True
        finally:
            if self.catched:
                fileHandle.seek(pos)

    def getMatcherCatcherMatcher(self, text):
        return self.pattern.search(text)
    # @pysnooper.snoop()

    def matchCatherLenght(self, text):
        try:
            matcher = self.pattern.match(text)
            if matcher is not None:
                return len(matcher.group(0))
            raise PatternNotMatchError(text, self.pattern.pattern)
        finally:
            pass

    def addExtraFeature(self, feature: ExtraFeatureStruct):
        self.extra_features.append(feature)

    def generateCatchStringSlice(self, fileHandle: TextIOWrapper):
        try:
            text = fileHandle.readline()
            matcher = self.pattern.match(text)
            if matcher is None:
                raise PatternNotMatchError(text, self.pattern.pattern)
            return matcher.group(0)
        finally:
            pass

    def generateMatchTransfromer(self,
                                 fileHandle: TextIOWrapper,
                                 feature: ExtraFeatureStruct):
        text = self.generateCatchStringSlice(fileHandle)
        t = self.generateSubStructMatchTransformer(text, feature)
        return t

    def substructMatchCatcher(self, text: str):
        return self.pattern.search(text) is not None

    def generateSubStructMatchTransformer(self,
                                          text,
                                          feature: ExtraFeatureStruct):
        t = Transformer(text, self.tag_name,
                        feature.id_name, feature.class_name,
                        **feature.othor_featrues)
        t.setCatcher(self)
        t.setMatcher = self.marcher
        t.feature = feature
        t.pattern = self.pattern
        return t

    def matchExtraFeatures(self, privous_transformer,
                           parent_transformer,
                           indent_level):
        for feature in self.extra_features:
            feature: ExtraFeatureStruct
            if (feature.parent_type is None or
                    feature.parent_type == parent_transformer) and (
                        feature.privous_type is None or
                    feature.privous_type == privous_transformer) and (
                        feature.indent_level == indent_level):
                return True, feature
        return False, ExtraFeatureStruct.NoneFeature()
