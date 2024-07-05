from PyQt6.QtWidgets import QMainWindow, QMessageBox, QComboBox,QDialog,QVBoxLayout,QLabel,QDialogButtonBox
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QFileSystemWatcher


class UserGuide(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("User")
        uic.loadUi('ui/user_guide.ui',self)
