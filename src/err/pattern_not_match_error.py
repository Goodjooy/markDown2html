
class PatternNotMatchError(RuntimeError):
    def __init__(self, text,pattern,*args) -> None:
        super().__init__(f"目标字符串“{text}”无法与“{pattern}”格式匹配")