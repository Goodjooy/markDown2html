import re

from transformers.transformer import Transformer

class TitleTransfromer(Transformer):
    
    def __init__(self, text) -> None:
        super().__init__(text, "<>")
