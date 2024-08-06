import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow
from PyQt6.QtGui import QPalette, QColor

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle('Fusion')



    pencere = MainWindow()
    pencere.show()
    sys.exit(app.exec())