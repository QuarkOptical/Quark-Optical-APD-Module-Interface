import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle('Fusion')



    pencere = MainWindow()
    pencere.show()
    sys.exit(app.exec())