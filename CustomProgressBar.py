from PyQt6.QtGui import QColor,QPainter,QPen
from PyQt6.QtWidgets import QProgressBar

class CustomProgressBar(QProgressBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setTextVisible(False)
    
    def paintEvent(self, event):
        super().paintEvent(event)
        
        painter = QPainter(self)

        pen = QPen(QColor('black'))
        pen.setWidthF(0.2)
        painter.setPen(pen)
        

        for i in range(1,10 ):
            x = int(i * self.width() / 10)
            painter.drawLine(x, 0, x, self.height())
        
        painter.end()