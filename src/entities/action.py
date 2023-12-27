class ActionEntity:
    hover: str =""
    selected: str =""
    disabled: str =""
    disabled_background: str =""
    focus: str =""
    hover_opacity:float = 0.08
    disabled_opacity:float = 0.48
    active: str = ""

    def __init__(self,option:dict):
        self.hover = option["hover"]
        self.selected = option["selected"]
        self.disabled = option["disabled"]
        self.disabled_background = option["disabled_background"]
        self.focus = option["focus"]
        self.hover_opacity = option["hover_opacity"]
        self.disabled_opacity = option["disabled_opacity"]
        self.active = option.get('active')

    def update(self, active):
        self.active=active