import sys
from PyQt6 import QtWidgets
import pyqtgraph as pg

class DynamicColorChanger(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.layout = QtWidgets.QVBoxLayout()

        # Create the PyQtGraph plot
        self.plotWidget = pg.PlotWidget()
        self.layout.addWidget(self.plotWidget)
        
        # Add buttons to change colors
        self.bgButton = QtWidgets.QPushButton("Change Background Color")
        self.bgButton.clicked.connect(self.changeBackgroundColor)
        self.layout.addWidget(self.bgButton)
        
        self.fgButton = QtWidgets.QPushButton("Change Foreground Color")
        self.fgButton.clicked.connect(self.changeForegroundColor)
        self.layout.addWidget(self.fgButton)
        
        self.setLayout(self.layout)
        
        # Set initial plot data
        self.plotWidget.plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        
        # Set initial colors
        self.current_bg_color = '#ffffff'  # White
        self.current_fg_color = 'k'        # Black
        
        self.setWindowTitle('PyQtGraph Dynamic Color Change')
        self.show()
    
    def changeBackgroundColor(self):
        # Toggle background color between white and black
        if self.current_bg_color == '#ffffff':
            self.current_bg_color = '#000000'
        else:
            self.current_bg_color = '#ffffff'
        self.plotWidget.setBackground(self.current_bg_color)
    
    def changeForegroundColor(self):
        # Toggle foreground color between black and red
        if self.current_fg_color == 'k':
            self.current_fg_color = 'r'
        else:
            self.current_fg_color = 'k'
        pg.setConfigOption('foreground', self.current_fg_color)
        
        # Update the pen color for axes and grid
        
        self.plotWidget.getAxis('left').setPen(pg.mkPen(self.current_fg_color))
        self.plotWidget.getAxis('bottom').setPen(pg.mkPen(self.current_fg_color))
        self.plotWidget.showGrid(x=True, y=True, alpha=0.5)  # Adjust grid color dynamically

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = DynamicColorChanger()
    sys.exit(app.exec())
