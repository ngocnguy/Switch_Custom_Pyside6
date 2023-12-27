from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
class Icon(QLabel):
    def __init__(self,
                 link_icon="src/view/icon/info.png",
                 width=24,
                 height=24
                 ):
        super().__init__()
        
        pixmap=QPixmap(link_icon)
        
        self.setPixmap(pixmap)
        self.setFixedSize(width,height)
    