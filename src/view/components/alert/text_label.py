from PySide6.QtWidgets import QLabel

style='''
    QLabel{{
        color:{} ;
    }}
    
    '''

class TextLabel(QLabel):
    def __init__(self,
                #  font_size="0.875rem",
                 text = "This is an info alert — check it out!",
                 color = "rgb(56,64,23)"
                 ):
        super().__init__()
        self.setText(text)
        self.setStyleSheet(style.format(color))