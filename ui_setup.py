from PyQt6.QtWidgets import QLabel
import pyqtgraph as pg
from PyQt6.QtCore import Qt
from CustomProgressBar import CustomProgressBar
from GaugeWidget import GaugeWidget
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor,QIcon
import pyqtgraph as pg

def setup_ui(main_window):
    
    main_window.setWindowTitle("APD Interface - Quark Optical")
        
    main_window.minVoltageSlider.setRange(main_window.min_hv*100,main_window.max_hv*100)
    main_window.maxVoltageSlider.setRange(main_window.min_hv*100,main_window.max_hv*100)
    main_window.minTempSlider.setRange(0,5000)
    main_window.maxTempSlider.setRange(0,5000)
    main_window.minVoltageSpinBox.setRange(0,200)
    main_window.maxVoltageSpinBox.setRange(0,200)
    main_window.minTempSpinBox.setRange(0,50)
    main_window.maxTempSpinBox.setRange(0,50)
        


    main_window.volt_pen = pg.mkPen(color='#ff0000', width=2)
    main_window.temp_pen = pg.mkPen(color='#00bfff', width=2)

    setup_graphs(main_window)
    setup_gauges(main_window)
        
    main_window.label1=QLabel()
    main_window.label1.setText("100")
    main_window.label2=QLabel()
    main_window.label2.setText("200")
    main_window.HVProgressBar = CustomProgressBar(main_window)
    main_window.HVProgressBar.setRange(100,200)
        
    main_window.horizontalLayout_8.addWidget(main_window.label1)
    main_window.horizontalLayout_8.addWidget(main_window.HVProgressBar)
    main_window.horizontalLayout_8.addWidget(main_window.label2)
        
    main_window.HVProgressBar.setFormat( "%v")
        
    main_window.aaaa.setStyleSheet("background-color: #3c3f41;")

        
    main_window.buttongroup.addButton(main_window.allRadioButton)
    main_window.buttongroup.addButton(main_window.onlyErrorRadioButton)
    main_window.buttongroup.addButton(main_window.offRadioButton)

        
    main_window.configureButton.setEnabled(False)
    main_window.startProcessButton.setEnabled(False)
        
    main_window.minVoltageSlider.setEnabled(False)
    main_window.maxVoltageSlider.setEnabled(False)
    main_window.minTempSlider.setEnabled(False)
    main_window.maxTempSlider.setEnabled(False)
        
    main_window.minVoltageSpinBox.setEnabled(False)
    main_window.maxVoltageSpinBox.setEnabled(False)
    main_window.minTempSpinBox.setEnabled(False)
    main_window.maxTempSpinBox.setEnabled(False)
        
    main_window.sendLineEdit.setEnabled(False)
    main_window.terminalTextEdit.setEnabled(False)
    main_window.clearButton.setEnabled(False)
    main_window.dumpButton.setEnabled(False)
    main_window.sendCommandButton.setEnabled(False)
    main_window.allRadioButton.setEnabled(False)
    main_window.offRadioButton.setEnabled(False)
    main_window.onlyErrorRadioButton.setEnabled(False)
    apply_light_palette(main_window)
    
    
def setup_graphs(main_window):
    main_window.tempWidget = pg.PlotWidget()
    main_window.tempWidget.setTitle("Temperature Graph")
    main_window.tempWidget.setLabel('left', 'Temperature', units='°C')
    main_window.tempWidget.setLabel('bottom', 'Time', units='s')
    main_window.tempWidget.setMinimumHeight(200)
    main_window.tempWidget.showGrid(0,20)

    main_window.voltWidget = pg.PlotWidget()
    main_window.voltWidget.setTitle("Voltage Graph")
    main_window.voltWidget.setLabel('left', 'Voltage', units='V')
    main_window.voltWidget.setLabel('bottom', 'Time', units='s')
    main_window.voltWidget.setMinimumHeight(200)   
    main_window.voltWidget.showGrid(0,20)

    main_window.graphLayout.addWidget(main_window.tempWidget)
    main_window.graphLayout.addWidget(main_window.voltWidget)
    main_window.tempWidget.setBackground('#ffffff')
    main_window.voltWidget.setBackground('#ffffff')
    
    
    main_window.toggleThemeButton.clicked.connect(lambda:toggle_theme(main_window))

def toggle_theme(main_window):
    if main_window.theme==0:
        main_window.theme=1
        apply_dark_palette(main_window)
    else:
        main_window.theme=0
        apply_light_palette(main_window)
    

def setup_gauges(main_window):
    main_window.gaugeLayout.setSpacing(0)
    main_window.gaugeLayout.setContentsMargins(0, 0, 0, 10)
    main_window.gaugeWidget = GaugeWidget() 
    main_window.gaugeWidget.setFixedSize(160, 85)   
    main_window.gaugeLayout.addWidget(main_window.gaugeWidget, alignment=Qt.AlignmentFlag.AlignTop)

def load_stylesheet(main_window):
    with open(main_window.qss_file, "r") as file:
        return file.read()
    
    
def apply_light_palette(main_window):
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

    QApplication.instance().setPalette(palette)
    main_window.tempWidget.setBackground('#ffffff') 
    main_window.voltWidget.setBackground('#ffffff')
    main_window.tempWidget.setTitle("Temperature Graph",color="black")
    main_window.voltWidget.setTitle("Voltage Graph",color="black")
    
    main_window.toggleThemeButton.setIcon(QIcon('assets/img/night-mode.png'))

    for i in ['left', 'bottom', 'top','right']:
        main_window.tempWidget.getAxis(i).setPen(pg.mkPen("black"))
        main_window.voltWidget.getAxis(i).setPen(pg.mkPen("black"))
    
       
    main_window.gaugeWidget.change_theme(0)
    with open("assets/styles/light_mode.qss", "r") as file:
        main_window.setStyleSheet(file.read())
    


def apply_dark_palette(main_window):
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(125, 125, 125))  # Window background
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))  # Text on the window
    palette.setColor(QPalette.ColorRole.Base, QColor(80, 80, 80))  # Background for text input
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(102, 102, 102))  # Alternate background
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))  # Tooltip background
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0))  # Tooltip text
    palette.setColor(QPalette.ColorRole.Text, QColor(0, 255, 0))  # Plain text
    palette.setColor(QPalette.ColorRole.Button, QColor(80, 80, 80))  # Button background
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))  # Button text
    palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))  # Bright text (like error text)
    palette.setColor(QPalette.ColorRole.Highlight, QColor(85, 170, 255))  # Item selection
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))  # Selected text
    palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(255, 0, 0))
    
    QApplication.instance().setPalette(palette)
    main_window.tempWidget.setBackground('#3c3f41')
    main_window.voltWidget.setBackground('#3c3f41')
    main_window.tempWidget.setTitle("Temperature Graph",color="white")
    main_window.voltWidget.setTitle("Voltage Graph",color="white")

    main_window.toggleThemeButton.setIcon(QIcon('assets/img/light-mode.png'))
    for i in ['left', 'bottom', 'top','right']:
        main_window.tempWidget.getAxis(i).setPen(pg.mkPen("white"))
        main_window.voltWidget.getAxis(i).setPen(pg.mkPen("white"))
        
    pg.setConfigOption('foreground', 'w')
    main_window.gaugeWidget.change_theme(1)
   
    with open("assets/styles/dark_mode.qss", "r") as file:
        main_window.setStyleSheet(file.read())
        
    
        
    