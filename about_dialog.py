from PyQt6.QtWidgets import QMainWindow, QMessageBox, QComboBox,QDialog,QVBoxLayout,QLabel,QDialogButtonBox
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QFileSystemWatcher


class AboutDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("About")
        uic.loadUi('ui/info.ui',self)
