class BackgroundEntity:
    paper:str = ""
    default:str = ""
    neutral:str = ""

    def __init__(self,option:dict):
        self.paper = option["paper"]
        self.default = option["default"]
        self.neutral = option["neutral"]
