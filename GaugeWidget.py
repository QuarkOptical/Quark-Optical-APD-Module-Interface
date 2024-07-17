import sys
from PyQt6.QtWidgets import  QWidget
from PyQt6.QtGui import QPainter, QColor, QFont, QPen
from PyQt6.QtCore import Qt, QRectF, QSize

class GaugeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0 # Set initial value of the gauge

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

        # Draw the base arc
        pen = QPen(QColor(200, 200, 200), 25, Qt.PenStyle.SolidLine, Qt.PenCapStyle.FlatCap)
        painter.setPen(pen)
        painter.drawArc(rect, start_angle, -span_angle)



        if self.value < 20:
            pen.setColor(QColor(9, 107, 178))  # Blue
        elif 20<=self.value<30:
            pen.setColor(QColor(58, 121, 0))  # Green
        elif 30 <= self.value < 40:
            pen.setColor(QColor(207,204,27))  # Yellow
        else:
            pen.setColor(QColor(160,21,38))  # Red

        painter.setPen(pen)
        painter.drawArc(rect, -start_angle, int(-span_angle * (self.value / 70.0)))

        # Draw the text
        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont('Arial', 12))
        text_rect = QRectF(30, 50, width - 60, (height - 60) / 2)
        painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, f'{self.value}')
