from PyQt6.QtWidgets import QLabel
from PyQt6 import uic
import pyqtgraph as pg
from PyQt6.QtCore import Qt
from custom_ui.CustomProgressBar import CustomProgressBar
from custom_ui.GaugeWidget import GaugeWidget

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
        
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')

    main_window.volt_pen = pg.mkPen(color='r', width=2)
    main_window.temp_pen = pg.mkPen(color='b', width=2)

    setup_graphs(main_window)
    setup_gauges(main_window)
        
    stylesheet=load_stylesheet(main_window)
    main_window.setStyleSheet(stylesheet)

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
        
    main_window.aaaa.setStyleSheet("background-color: #A9A9A9;")

        
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
    
    
def setup_graphs(main_window):
    main_window.tempWidget = pg.PlotWidget()
    main_window.tempWidget.setTitle("Temperature Graph")
    main_window.tempWidget.setLabel('left', 'Temperature', units='°C')
    main_window.tempWidget.setLabel('bottom', 'Time', units='s')
        
    main_window.tempWidget.showGrid(0,20)

    main_window.voltWidget = pg.PlotWidget()
    main_window.voltWidget.setTitle("Voltage Graph")
    main_window.voltWidget.setLabel('left', 'Voltage', units='V')
    main_window.voltWidget.setLabel('bottom', 'Time', units='s')
        
    main_window.voltWidget.showGrid(0,20)

    main_window.graphLayout.addWidget(main_window.tempWidget)
    main_window.graphLayout.addWidget(main_window.voltWidget)


def setup_gauges(main_window):
    main_window.gaugeLayout.setSpacing(0)
    main_window.gaugeLayout.setContentsMargins(0, 0, 0, 10)
    main_window.gaugeWidget = GaugeWidget() 
    main_window.gaugeWidget.setFixedSize(160, 85)   
    main_window.gaugeLayout.addWidget(main_window.gaugeWidget, alignment=Qt.AlignmentFlag.AlignTop)

def load_stylesheet(self):
    with open(self.qss_file, "r") as file:
        return file.read()