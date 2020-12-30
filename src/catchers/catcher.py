from io import TextIOWrapper
import re
from typing import IO

from extra_feature import ExtraFeatureStruct


class Catcher(object):

    def __init__(self) -> None:
        self.pattern = re.compile(r"(*.)", re.IGNORECASE)

        self.extra_features = []

    def matchCatcher(self, fileHandle: TextIOWrapper):
        text = fileHandle.readline()
        pos = fileHandle.tell()
        fileHandle.seek(pos-len(text))

        return self.pattern.match(text) is not None
    
    def generateMatchTransfromer(self):
        pass
    def substructMatchCatcher(self,text:str):
        return self.pattern.search(text) is not None

    def matchExtraFeatures(self,privous_transformer,parent_transformer,indent_level):
        for feature in self.extra_features:
            feature:ExtraFeatureStruct
            #TODO: 检查当前捕获状态是否要添加额外特征
            if feature.parent_type is not None:
                pass


