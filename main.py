from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from src.view import AY_Contained_Button, AY_OutLined_Button, StandartAlert

import sys
from src.themes import (
    palette,
    create_shadow,
    func_custom_shadows,
    create_shadows,
    func_shadows,
    func_typography,
    responsive_font_sizes,
)

app = QApplication(sys.argv)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.resize(800, 600)
        layout = QHBoxLayout()

        # FILE PALLETE
        self.theme = palette("light")

        self.theme.common.black 

        # FILE CUSTOM_SHADOW
        self.shadow = func_custom_shadows("dark")

        ##########################FILE TYPOGRAPHY###############################################
        self.typo = func_typography()

        btn1_contained = AY_Contained_Button(
            text="Default",
            border="4px",
            background_color="rgb(69, 79, 91)",
            background_color_hover="rgb(28, 35, 42)",
        )
        btn2_contained = AY_Contained_Button(
            text="Primary",
            border="4px",
            background_color=self.theme.primary.main,
            background_color_hover="rgb(240, 148, 13)",
        )
        btn3_contained = AY_Contained_Button(
            text="Secondary",
            border="4px",
            background_color=self.theme.secondary.main,
            background_color_hover="rgb(85, 43, 118)",
        )
        btn4_contained = AY_Contained_Button(
            text="Disabled",
            border="4px",
            background_color=self.theme.action.disabled,
            disable="True",
        )
        btn5_contained = AY_Contained_Button(
            text="Link",
            border="4px",
            background_color="rgb(33, 43, 54)",
            background_color_hover="rgb(28, 35, 42)",
        )
        btn6_shadow = QPushButton("dbashj")
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(15)  # Đặt bán kính mờ (điều chỉnh cần thiết)
        shadow_effect.setColor(
            QColor(0, 0, 0, 255)
        )  # Đặt màu sắc (điều chỉnh cần thiết)
        shadow_effect.setOffset(0, 0)  # Đặt khoảng cách (điều chỉnh cần thiết)

        btn6_shadow.setGraphicsEffect(shadow_effect)
        btn7_no_shadow = QPushButton("btn7")
        layout.addWidget(btn1_contained)
        layout.addWidget(btn2_contained)
        layout.addWidget(btn3_contained)
        layout.addWidget(btn4_contained)
        layout.addWidget(btn5_contained)
        layout.addWidget(btn6_shadow)
        layout.addWidget(btn7_no_shadow)

        layout2 = QHBoxLayout()

        btn1_outlined = AY_OutLined_Button(
            text="Default",
            border="1px solid rgba(233, 239, 239,1)",
            color="rgba(233, 239, 239,1)",
            bode_hover_color="2px solid rgb(206, 225, 225)",
            background_color_hover="rgb(163, 166, 169)",
        )
        btn2_outlined = AY_OutLined_Button(
            text="Primary",
            border="1px solid rgba(253, 169, 45,1)",
            color="rgba(253, 169, 45,1)",
            bode_hover_color="2px solid rgb(235,146,14)",
            background_color_hover="rgb(236, 207, 164)",
        )
        btn3_outlined = AY_OutLined_Button(
            text="Secondary",
            border="1px solid rgba(142, 51, 255,1)",
            color="rgba(142, 51, 255,1)",
            bode_hover_color="2px solid rgb(112, 14, 235)",
            background_color_hover="rgb(204, 177, 236)",
        )
        btn4_outlined = AY_OutLined_Button(
            text="Disabled",
            border="(1px solid )",
            background_color="rgb(226, 229, 233)",
            disable="True",
        )
        btn5_outlined = AY_OutLined_Button(
            text="Link",
            border="1px solid rgba(233, 239, 239,1)",
            color="rgba(233, 239, 239,1)",
            bode_hover_color="2px solid rgb(206, 225, 225)",
            background_color_hover="rgb(163, 166, 169)",
        )

        layout2.addWidget(btn1_outlined)
        layout2.addWidget(btn2_outlined)
        layout2.addWidget(btn3_outlined)
        layout2.addWidget(btn4_outlined)
        layout2.addWidget(btn5_outlined)

        layout3 = QVBoxLayout()

        alert_info_standard = StandartAlert(
            color_enter=self.theme.info.light, color_leave=self.theme.info.lighter
        )
        print(self.theme.info.light)
        alert_success_standard = StandartAlert(
            link_icon="src/view/icon/success",
            text="This is an success alert — check it out!",
            background_color=self.theme.success.lighter,
            color="rgb(6, 94, 73)",
            color_enter="rgb(224, 216, 183)",
            color_leave="rgb(211,252,210)",
        )
        alert_warning_standard = StandartAlert(
            link_icon="src/view/icon/warning",
            text="This is an warning alert — check it out!",
            background_color=self.theme.warning.lighter,
            color="rgb(122, 65, 0)",
            color_enter="rgb(224, 216, 183)",
            color_leave="rgb(255,245,204)",
        )
        alert_error_standard = StandartAlert(
            link_icon="src/view/icon/error",
            text="This is an error alert — check it out!",
            background_color=self.theme.error.lighter,
            color="rgb(122, 9, 22)",
            color_enter="rgb(224, 216, 183)",
            color_leave="rgb(255,233,213)",
        )

        layout3.addWidget(alert_info_standard)
        layout3.addWidget(alert_success_standard)
        layout3.addWidget(alert_warning_standard)
        layout3.addWidget(alert_error_standard)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout)
        layout_main.addLayout(layout2)
        layout_main.addLayout(layout3)
        widget = QWidget()
        widget.setLayout(layout_main)

        self.setCentralWidget(widget)


window = Window()
window.show()

app.exec()
