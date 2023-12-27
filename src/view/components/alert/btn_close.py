from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QPainter, QColor,QPen
from PySide6.QtCore import Qt
from ....utils import alpha_hex_to_rgb
class CircularButton(QPushButton):
    
    def __init__(self,
                # color_enter = "#7A0916",
                # color_leave = "#FFAB00",
                color_enter = "rgb(153, 243, 228)",
                color_leave = "rgb(202, 253, 245)",
                width_close = 26,
                height_close = 26
                ):
        super().__init__()
        self.setFixedSize(width_close, height_close)  # Đặt kích thước cố định cho nút
        self.hovered = False  # Trạng thái chuột hover 
        if (color_enter[0] == "r"):

            self.color_tuple_enter=list(map(int, color_enter[4:-1].split(',')))   #[153,243,228]
        if (color_leave[0] == "r"):
            self.color_tuple_leave=list(map(int, color_leave[4:-1].split(',')))
            
        if (color_enter[0] == "#"):
            self.color_enter = alpha_hex_to_rgb(color_enter)
            self.color_tuple_enter=list(map(int, self.color_enter[4:-1].split(',')))
        if (color_leave[0] == "#"):
            self.color_leave = alpha_hex_to_rgb(color_leave)
            self.color_tuple_leave=list(map(int, self.color_leave[4:-1].split(',')))
        self.width_close = width_close
        self.height_close = height_close

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # giảm răng cưa
        painter.setPen(Qt.NoPen)  # Không dùng bút để vẽ viền
        if self.hovered:
            painter.setBrush(QColor(self.color_tuple_enter[0],self.color_tuple_enter[1],self.color_tuple_enter[2]))  
        else:
            painter.setBrush(QColor(self.color_tuple_leave[0],self.color_tuple_leave[1],self.color_tuple_leave[2]))  
        

        painter.drawEllipse(0, 0, self.width(), self.height())  # Vẽ hình tròn
        #VẼ DẤU x
        pen = QPen(Qt.black)
        pen.setWidth(2)  # Đặt độ dày của đường

        painter.setPen(pen)
        painter.drawLine(7,7,self.width_close-7,self.width_close-7)
        painter.drawLine(7,self.width_close-7,self.width_close-7,7)
        # print(str(self.color_enter))

        
    def enterEvent(self, event):
        self.hovered = True
        self.update()  # Yêu cầu vẽ lại nút

    def leaveEvent(self, event):
        self.hovered = False
        self.update()  # Yêu cầu vẽ lại nút


    # color = rgb_to_Qcolor("rgb(56,76,98)")
    # print(str(color))

