from PySide6.QtWidgets import QHBoxLayout,QWidget,QFrame
from PySide6.QtGui import QColor
from ..btn_close  import CircularButton
from ..icon import Icon
from ..text_label import TextLabel

    
class StandartAlert(QWidget):
    def __init__(self,
                 link_icon="src/view/icon/info.png",
                 width_icon=24,
                 height_icon=24,
                 text = "This is an info alert — check it out!",
                 color = "rgb(0, 55, 104)",
                 color_enter = "rgb(153, 243, 228)",
                 color_leave = "rgb(202, 253, 245)",
                 width_close = 26,
                 height_close = 26,
                 background_color = "rgb(202, 253, 245)",
                 border_radius = "8px"
                 ):
        super().__init__()
        frame = QFrame()
        frame.setFixedSize(380,50)
        
        layout_small=QHBoxLayout(frame)
        icon1 = Icon(link_icon,width_icon,height_icon)
        layout_small.addWidget(icon1)

        txt_label = TextLabel(text,color)
        layout_small.addWidget(txt_label)

        
        btn_click=CircularButton(color_enter, color_leave,width_close,height_close)
        btn_click.clicked.connect(self.close)
        
        layout_small.addWidget(btn_click)

        frame.setStyleSheet(f"background-color:{background_color};border-radius: {border_radius}")
        layout=QHBoxLayout()
        layout.addWidget(frame)
        self.setLayout(layout)

    

