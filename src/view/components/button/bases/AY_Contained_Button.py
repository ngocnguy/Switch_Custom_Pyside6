from PySide6.QtWidgets import QPushButton,QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
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

    }}
    '''
# rgb(255, 255, 255)  rgb(33, 43, 54)
class AY_Contained_Button(QPushButton):
    def __init__(self,
                 text="AY_Contained_Button",
                 outline="0px",
                 border="0px",
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
                 background_color="rgb(33, 43, 54)",
                 background_color_hover="rgb(22,55,11)",
                 disable="False",
                 strshadow="5 5 2 rgba(54, 65, 76, 0.24)"
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
                                        disable
                                        ))
        self.setText(text)
        if disable=="True":
            self.setEnabled(False)
        else:
            self.setCursor(Qt.PointingHandCursor)
        elements = strshadow.split()
        opacity=elements[3]
        q_color=list(map(float,strshadow.split("(")[1].split(")")[0].split(", ")))

        print(q_color)
        opacity_qcolor=q_color[3]*255

        shadow = QGraphicsDropShadowEffect()
        # shadow.setBlurRadius(int(elements[2]))
        # shadow.setColor(QColor(int(q_color[0]),int(q_color[1]),int(q_color[2]),round(opacity_qcolor)))
        # shadow.setOffset(int(elements[0]), int(elements[1]))
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(Qt.black))
        shadow.setOffset(5,5)
        self.setGraphicsEffect(shadow)
        