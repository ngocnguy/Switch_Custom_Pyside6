from .text import TextEntity
from .background import BackgroundEntity
from .action import ActionEntity
from .common import CommonEntity

class LightEntity(CommonEntity):
    mode:str ="light"
    text: TextEntity = None
    background: BackgroundEntity = None
    # action: ActionEntity = None

    def __init__(self,options:dict,common:dict):
        super().__init__(common)
        self.mode=options.get("mode")
        self.text = options.get("text")
        self.background = options.get("background")
        # self.action = options.get("action")

    
    