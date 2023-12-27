from .h_entity import HEntity
from .subtitle import SubtitleEntity
from .body import BodyEntity
from .caption import CaptionEntity
from .overline import OverlineEntity
from .button import ButtonEntity
class TypographyEntity:
    font_family : str =""
    font_weight_regular: str =""
    font_weight_medium: str =""
    font_weight_bold: str =""
    h1 : HEntity = None
    h2 : HEntity = None
    h3 : HEntity = None
    h4 : HEntity = None
    h5 : HEntity = None
    h6 : HEntity = None
    subtitle1 : SubtitleEntity = None
    subtitle2 : SubtitleEntity = None
    body1 : BodyEntity = None
    body2 : BodyEntity = None
    caption : CaptionEntity = None
    overline : OverlineEntity = None
    button : ButtonEntity = None


    def __init__(self,options):
        self.font_family = options["font_family"]
        self.font_weight_regular = options["font_weight_regular"]
        self.font_weight_medium = options["font_weight_medium"]
        self.font_weight_bold = options["font_weight_bold"]
        self.h1 = options["h1"]
        self.h2 = options["h2"]
        self.h3 = options["h3"]
        self.h4 = options["h4"]
        self.h5 = options["h5"]
        self.h6 = options["h6"]
        self.subtitle1 = options["subtitle1"]
        self.subtitle2 = options["subtitle2"]
        self.body1 = options["body1"]
        self.body2 = options["body2"]
        self.caption = options["caption"]
        self.overline = options["overline"]
        self.button = options["button"]