from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt
style='''
    QPushButton{{
        outline: {};
        border: {};
        margin: {};
        font-weight: {};
        line-height: {};
        font-size: {};
        text-transform: {};
        font-family: {};
        min-width: {};
        padding: {} {};
        border-radius: {};
        color:{} ;
        background-color: {};
        
    }}
    
    QPushButton::hover{{
        background-color: {};
        border-color:{};
    }}
    '''
# rgb(255, 255, 255)  rgb(33, 43, 54)
class AY_OutLined_Button(QPushButton):
    def __init__(self,
                 text="AY_Contained_Button",
                 outline="0px",
                 border="1px solid rgb(16, 16, 18)",
                 margin="0px",
                 font_weight="700",
                 line_height="1.71429",
                 font_size="0.875rem",
                 text_transform="unset",
                 font_family='"Public Sans", sans-serif',
                 min_width="64px",
                 padding_x="6px",
                 padding_y="12px",
                 border_radius="8px",
                 color="rgb(255, 255, 255)",
                 background_color="rgb(255, 255, 255)",
                 
                 background_color_hover="rgb(22,55,11)",
                 bode_hover_color="1px solid rgb(16, 16, 18)",
                 disable="False"
                 ):
        super().__init__()
        
        self.setStyleSheet(style.format(outline,
                                        border,
                                        margin,
                                        font_weight,
                                        line_height,
                                        font_size,
                                        text_transform,
                                        font_family,
                                        min_width,
                                        padding_x,
                                        padding_y,
                                        border_radius,
                                        color,
                                        background_color,
                                        
                                        background_color_hover,
                                        bode_hover_color,
                                        disable
                                        ))
        self.setText(text)
        if disable=="True":
            self.setEnabled(False)
        else:
            self.setCursor(Qt.PointingHandCursor)
        