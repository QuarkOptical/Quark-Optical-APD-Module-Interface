from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class AboutDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("About")
        uic.loadUi('ui/info.ui',self)
