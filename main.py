import sys
from PyQt6.QtWidgets import QApplication
from seri_port_okuyucu import SeriPortOkuyucu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = SeriPortOkuyucu()
    pencere.show()
    sys.exit(app.exec())


