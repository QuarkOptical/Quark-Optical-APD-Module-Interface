from PyQt6.QtWidgets import  QWidget
from PyQt6.QtGui import QPainter, QColor, QFont, QPen
from PyQt6.QtCore import Qt, QRectF, QSize

class GaugeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0
        self.gauge_status=0
        self.theme=0
            
    def setValue(self, value):
        self.value = value
        self.update()

    def sizeHint(self):
        return QSize(200, 100)

    def minimumSizeHint(self):
        return QSize(100, 50)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height() * 2

        rect = QRectF(30, 30, width - 60, height - 60)

        start_angle = 180 * 16
        span_angle = 180 * 16

        if self.theme==0:
            self.pen = QPen(QColor(220, 220, 220), 25, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap)
            painter.setPen(self.pen)
            painter.drawArc(rect, start_angle, -span_angle)
            
        elif self.theme==1:
            self.pen = QPen(QColor(60, 63, 65), 25, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap)
            painter.setPen(self.pen)
            painter.drawArc(rect, start_angle, -span_angle)


        if self.gauge_status==0:
            if self.value < 20:
                self.pen.setColor(QColor(45, 110, 252))  # Blue
            elif 20<=self.value<30:
                self.pen.setColor(QColor(50, 99, 7))  # Green
            elif 30 <= self.value < 40:
                self.pen.setColor(QColor(252, 232, 45))  # Yellow
            else:
                self.pen.setColor(QColor(252, 45, 45))  # Red
        elif self.gauge_status==1:
            self.pen.setColor(QColor(211,211,211))

        painter.setPen(self.pen)
        painter.drawArc(rect, -start_angle, int(-span_angle * (self.value / 70.0)))

        if self.theme==0:
            painter.setPen(QColor(0, 0, 0))
            painter.setFont(QFont('Arial', 12))
            text_rect = QRectF(30, 50, width - 60, (height - 60) / 2)
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, f'{self.value}')
        elif self.theme==1:
            painter.setPen(QColor(255, 255, 255))
            painter.setFont(QFont('Arial', 12))
            text_rect = QRectF(30, 50, width - 60, (height - 60) / 2)
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, f'{self.value}')    
        
    def change_theme(self,theme):
        self.theme=theme