from PyQt6.QtGui import QColor,QPainter,QPen
from PyQt6.QtWidgets import QProgressBar



class CustomProgressBar(QProgressBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setTextVisible(False)
    
    def paintEvent(self, event):
        super().paintEvent(event)
        
        painter = QPainter(self)
        #painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Çizgilerin rengini ve kalınlığını ayarlama
        pen = QPen(QColor('black'))
        pen.setWidthF(0.2)
        painter.setPen(pen)
        
        # Ölçek çizgilerini çizme
        
        for i in range(1,10 ):
            x = int(i * self.width() / 10)  # int türüne dönüştürme
            painter.drawLine(x, 0, x, self.height())
        
        painter.end()