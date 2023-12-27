
class TextEntity:
    primary: str = ""
    secondary: str = ""
    disabled: str = ""

    def __init__(self, option:dict):
        self.primary= option["primary"]
        self.secondary= option["secondary"]
        self.disabled= option["disabled"]
