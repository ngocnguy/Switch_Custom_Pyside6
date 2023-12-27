from .text import TextEntity
from .background import BackgroundEntity
from .action import ActionEntity

class ThemeEntity:
    mode:str ="dark"
    text: TextEntity = None
    background: BackgroundEntity = None
    action: ActionEntity = None

    def __init__(self,options:dict):
        # self.mode=options.get("screen_resolution").replace()
        # self.profileHash=options.get("profile_hash")
        # self.webglMode=options.get("webl")
        self.mode=options.get("mode")
        self.text = options.get("text")
        self.background = options.get("background")
        self.action = options.get("action")
