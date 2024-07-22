import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow
from PyQt6.QtGui import QPalette, QColor

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))  # Window background
    palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))  # Text on the window
    palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))  # Background for text input
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(240, 240, 240))  # Alternate background
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(0, 0, 0))  # Tooltip background
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))  # Tooltip text
    palette.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0))  # Plain text
    palette.setColor(QPalette.ColorRole.Button, QColor(255, 255, 255))  # Button background
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(0, 0, 0))  # Button text
    palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))  # Bright text (like error text)
    palette.setColor(QPalette.ColorRole.Highlight, QColor(0, 120, 215))  # Item selection
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))  # Selected text

    app.setPalette(palette)


    pencere = MainWindow()
    pencere.show()
    sys.exit(app.exec())