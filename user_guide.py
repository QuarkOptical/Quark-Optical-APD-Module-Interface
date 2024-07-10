from PyQt6.QtWidgets import QMainWindow, QMessageBox, QComboBox,QDialog,QVBoxLayout,QLabel,QDialogButtonBox
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QFileSystemWatcher
import os
import markdown2
class UserGuide(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("User")
        uic.loadUi(os.path.dirname(os.path.abspath(__file__))+'/ui/user_guide.ui',self)
        path=(os.path.dirname(os.path.abspath(__file__))+'/UserGuide/User Guide.md')
        print(path)
        self.load_markdown(path)
    
    def load_markdown(self,markdown_file):
        with open(markdown_file, 'r', encoding='utf-8') as file:
            markdown_text = file.read()
            
        extras = ["toc", "fenced-code-blocks", "tables", "strike", "footnotes"]
        html = markdown2.markdown(markdown_text,extras=extras)
        self.textBrowser.setHtml(html)