from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog,QLCDNumber,QProgressBar,QLabel,QLayout
from PyQt6.QtGui import QColor, QPalette,QPainter,QPen
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QFileSystemWatcher, QThread,Qt
from PyQt6.QtSerialPort import QSerialPortInfo
import pyqtgraph as pg
import re
import os
import shutil

from serial_thread import SerialThread
from dialog import PopupDialog
from about_dialog import AboutDialog 
from user_guide import UserGuide
from GaugeWidget import GaugeWidget

class CustomProgressBar(QProgressBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setTextVisible(False)
    
    def paintEvent(self, event):
        super().paintEvent(event)
        
        painter = QPainter(self)
        #painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Çizgilerin rengini ve kalınlığını ayarlama
        pen = QPen(QColor('black'))
        pen.setWidthF(0.2)
        painter.setPen(pen)
        
        # Ölçek çizgilerini çizme
        
        for i in range(1,10 ):
            x = int(i * self.width() / 10)  # int türüne dönüştürme
            painter.drawLine(x, 0, x, self.height())
        
        painter.end()










class SeriPortOkuyucu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initialize_variables()
        self.setup_ui()
        #self.load_stylesheet()
        self.setup_connections()
        self.populateSerialPorts()
        self.listeDosyaAdlari()

    def setup_ui(self):
        uic.loadUi(os.path.dirname(os.path.abspath(__file__))+"/ui/main_window.ui", self)
        self.setWindowTitle("APD Interface - Quark Optical")
        #self.setFixedHeight(600)
        #self.setFixedWidth(1000)

        palette = self.palette()
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Window, QColor(255, 255, 255))
        self.setPalette(palette)
        
        self.minVoltageSlider.setRange(10000,20000)
        self.maxVoltageSlider.setRange(10000,20000)
        
        self.minTempSlider.setRange(0,5000)
        self.maxTempSlider.setRange(0,5000)
    
        self.minVoltageSpinBox.setRange(0,200)
        self.maxVoltageSpinBox.setRange(0,200)
        self.minTempSpinBox.setRange(0,50)
        self.maxTempSpinBox.setRange(0,50)
        
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.volt_pen = pg.mkPen(color='r', width=2)
        self.temp_pen = pg.mkPen(color='b', width=2)

        self.setup_graphs()
        self.setup_gauges()
        
        stylesheet=self.load_stylesheet2()
        self.setStyleSheet(stylesheet)

        self.label1=QLabel()
        self.label1.setText("100")
        self.label2=QLabel()
        self.label2.setText("200")
        self.HVProgressBar = CustomProgressBar(self)
        self.HVProgressBar.setRange(100,200)
        
        self.horizontalLayout_8.addWidget(self.label1)
        self.horizontalLayout_8.addWidget(self.HVProgressBar)
        self.horizontalLayout_8.addWidget(self.label2)
        
        self.HVProgressBar.setFormat( "%v")
        
        self.aaaa.setStyleSheet("background-color: #096bb2;")
        self.label_4.setStyleSheet("color:white;")
        
        self.load_stylesheet()
        
        self.configureButton.setEnabled(False)
        self.startProcessButton.setEnabled(False)
        

        
    def test(self):
        print("AAAAAAAAAAAAAAA")

    def setup_graphs(self):
        self.tempWidget = pg.PlotWidget()
        self.tempWidget.setTitle("Temperature Graph")
        self.tempWidget.setLabel('left', 'Temperature', units='°C')
        self.tempWidget.setLabel('bottom', 'Time', units='s')
        
        self.tempWidget.showGrid(0,20)

        self.voltWidget = pg.PlotWidget()
        self.voltWidget.setTitle("Voltage Graph")
        self.voltWidget.setLabel('left', 'Voltage', units='V')
        self.voltWidget.setLabel('bottom', 'Time', units='s')
        
        self.voltWidget.showGrid(0,20)

        self.graphLayout.addWidget(self.tempWidget)
        self.graphLayout.addWidget(self.voltWidget)


    def setup_gauges(self):
        self.gaugeLayout.setSpacing(0)
        self.gaugeLayout.setContentsMargins(0, 0, 0, 10)
        self.gaugeWidget = GaugeWidget()
        self.gaugeWidget.setFixedSize(160, 85)
        self.gaugeLayout.addWidget(self.gaugeWidget)

    def initialize_variables(self):
        
        self.scale = 0.01
        self.time = 0.0
        self.times_v = []
        self.times_t = []
        self.is_configuring = False
        self.temp_data = []
        self.hv_data = []
        self.serial_thread = None
        self.is_connected = False
        self.is_started = False
        self.qss_file = os.path.dirname(os.path.abspath(__file__))+"/assets/styles/slider.qss"
        self.qss_file2 = os.path.dirname(os.path.abspath(__file__))+"/assets/styles/settings.qss"

        self.timer = QTimer()
        self.terminal_timer=QTimer()
        self.terminal_timer.setInterval(100)
        self.terminal_timer.setSingleShot(True)
        self.terminal_timer.timeout.connect(self.enable_terminal)
        
        
        self.timer.start(100)
        self.command_timer = QTimer()
        self.command_timer.timeout.connect(self.send_periodic_command)
        self.command_timer.start(100)

        #self.watcher = QFileSystemWatcher([self.qss_file])
        #self.watcher.fileChanged.connect(self.load_stylesheet)
        
        self.watcher = QFileSystemWatcher([self.qss_file2])
        self.watcher.fileChanged.connect(self.load_stylesheet)
        

    def setup_connections(self):
        self.comPorts.currentIndexChanged.connect(self.onPortChanged)
        self.minVoltageSlider.valueChanged.connect(lambda value: self.sliderChange(value, self.minVoltageSpinBox))
        self.maxVoltageSlider.valueChanged.connect(lambda value: self.sliderChange(value, self.maxVoltageSpinBox))
        self.minTempSlider.valueChanged.connect(lambda value: self.sliderChange(value, self.minTempSpinBox))
        self.maxTempSlider.valueChanged.connect(lambda value: self.sliderChange(value, self.maxTempSpinBox))
        self.minVoltageSpinBox.valueChanged.connect(lambda value: self.spinboxChange(value, self.minVoltageSlider))
        self.maxVoltageSpinBox.valueChanged.connect(lambda value: self.spinboxChange(value, self.maxVoltageSlider))
        self.minTempSpinBox.valueChanged.connect(lambda value: self.spinboxChange(value, self.minTempSlider))
        self.maxTempSpinBox.valueChanged.connect(lambda value: self.spinboxChange(value, self.maxTempSlider))

        self.addConfigButton.clicked.connect(self.show_popup)
        self.sendCommandButton.clicked.connect(self.send_data)
        self.sendLineEdit.returnPressed.connect(self.send_data)
        self.infoButton.clicked.connect(self.show_info)
        self.userGuideButton.clicked.connect(self.show_guide)
        self.configsComboBox.currentIndexChanged.connect(self.onComboBoxIndexChanged)
        self.connectButton.clicked.connect(self.toggle_connection)
        self.startProcessButton.clicked.connect(self.toggle_process)
        self.configureButton.clicked.connect(self.send_configuration)
        self.addToolButton.clicked.connect(self.upload_data)
        self.refreshButton.clicked.connect(self.populateSerialPorts)
        self.settings.clicked.connect(self.test)

    def enable_terminal(self):
        self.sendLineEdit.setEnabled(True)
        self.sendCommandButton.setEnabled(True)

    def show_guide(self):
        info = UserGuide(parent=self)
        if info.exec():
            print("Kayıt edilen veriler:")
    def show_info(self):
        info = AboutDialog(parent=self)
        if info.exec():
            print("Kayıt edilen veriler:")


    def load_stylesheet(self):
        with open("assets/styles/settings.qss", "r") as file:
            #return file.read()
            style_sheet=file.read()
            self.settings.setStyleSheet(style_sheet)
            self.infoButton.setStyleSheet(style_sheet)
        self.settings.update()
        self.infoButton.update()
        
        
    def load_stylesheet2(self):
        with open(self.qss_file, "r") as file:
            return file.read()

    def populateSerialPorts(self):
        self.comPorts.clear()
        ports = QSerialPortInfo.availablePorts()
        sorted_ports = sorted(ports, key=lambda port: port.portName())
        for port in sorted_ports:
            self.comPorts.addItem(port.portName())

    def onPortChanged(self, index):
        if self.serial_thread:
            selectedPortName = self.comPorts.currentText()
            print("Selected port:", selectedPortName)
            self.serial_thread.set_port_name(selectedPortName)

    def toggle_process(self):
        if not self.is_started:
            self.start_process()
        else:
            self.stop_process()

    def start_process(self):
        self.serial_thread.start_reading()
        self.serial_thread.data_received.connect(self.update_data)
        self.serial_thread.error_occurred.connect(self.handle_error)
        self.command_timer.start(100)
        self.is_started = True
        self.serial_thread.start_command()
        self.configureButton.setEnabled(False)
        self.connectButton.setEnabled(False)
        self.comPorts.setEnabled(False)
        self.refreshButton.setEnabled(False)
        self.set_controls_enabled(False)
        self.startProcessButton.setText("Stop Process")

    def stop_process(self):
        self.serial_thread.stop_reading()
        self.serial_thread.data_received.disconnect()
        self.command_timer.stop()
        self.is_started = False
        self.serial_thread.stop_command()
        self.configureButton.setEnabled(True)
        self.connectButton.setEnabled(True)
        self.comPorts.setEnabled(True)
        self.refreshButton.setEnabled(True)
        self.set_controls_enabled(True)
        self.startProcessButton.setText("Start Process")

    def set_controls_enabled(self, enabled):
        self.minVoltageSlider.setEnabled(enabled)
        self.maxVoltageSlider.setEnabled(enabled)
        self.minTempSlider.setEnabled(enabled)
        self.maxTempSlider.setEnabled(enabled)
        self.minVoltageSpinBox.setEnabled(enabled)
        self.maxVoltageSpinBox.setEnabled(enabled)
        self.minTempSpinBox.setEnabled(enabled)
        self.maxTempSpinBox.setEnabled(enabled)

    def toggle_connection(self):
        if not self.is_connected:
            self.start_connection()
        else:
            self.stop_connection()

    def start_connection(self):
        selected_port = self.comPorts.currentText()
        if not selected_port:
            QMessageBox.warning(self, "Hata", "Lütfen bir seri port seçin.")
            return
        print("Starting serial thread")
        self.serial_thread = SerialThread()
        self.serial_thread.set_port_name(selected_port)
        self.serial_thread.start()
        self.is_connected = True
        self.configureButton.setEnabled(True)
        self.startProcessButton.setEnabled(True)
        self.HVProgressBar.setEnabled(True)
        self.set_controls_enabled(True)
        self.connectButton.setText("Disconnect")

    def stop_connection(self):
        print("Stopping serial thread")
        self.serial_thread.stop()
        self.serial_thread = None
        self.is_connected = False
        self.configureButton.setEnabled(False)
        self.startProcessButton.setEnabled(False)
        self.HVProgressBar.setEnabled(False)
        self.set_controls_enabled(False)
        self.connectButton.setText("Connect")

    def send_periodic_command(self):
        if self.is_connected and self.serial_thread and not self.is_configuring:
            self.serial_thread.send_command_signal.emit()
            self.serial_thread.toggle_command()

    def update_data(self, data):
        temp_match = re.match(r"i/CURRENT_TEMP=(\d+)", data)
        hv_match = re.match(r"i/CURRENT_HV=(\d+)", data)

        if temp_match:
            temp_value = float(temp_match.group(1)) / 100
            self.temp_data.append(temp_value)
            self.times_t.append(self.time)
            self.tempWidget.plot(self.times_t,self.temp_data, pen=self.temp_pen, clear=True)
            self.gaugeWidget.setValue(temp_value)
            self.tempWidget.setYRange(temp_value-5,temp_value+5)
            
            if self.time>=30:
                self.tempWidget.setXRange(self.time-20,self.time)

        elif hv_match:
            hv_value = float(hv_match.group(1)) / 100
            self.hv_data.append(hv_value)
            self.times_v.append(self.time)
            self.voltWidget.plot(self.times_v, self.hv_data, pen=self.volt_pen, clear=True)
            self.HVProgressBar.setValue(int(hv_value))
            self.HVReadingLabel.setText(f"High Voltage Reading:{hv_value}")
            self.voltWidget.setYRange(hv_value-100,hv_value+100)
            if self.time>=30:
                self.voltWidget.setXRange(self.time-20,self.time)
        
    
        self.time += 0.1

    def handle_error(self, error):
        print(f"Error: {error}")

    def send_data(self):
        if self.sendLineEdit.text()=='/help' or self.sendLineEdit.text()== '/h':
            help_text="""
                Commands:<br>
                w/VOLTAGE=(number) - Sets desired voltage to number.<br>
                w/MODE=(number) - Sets operating mode to number.<br>
                w/MIN_TEMP=(number) - Sets minimum temperature threshold to number.<br>
                w/MAnumber_TEMP=(number) - Sets maximum temperature threshold to number.<br>
                w/MIN_HV=(number) - Sets minimum high voltage threshold to number.<br>
                w/MAnumber_HV=(number) - Sets maximum high voltage threshold to number.<br>
                w/LED_MODE=(number) - Sets LED mode to number.<br><br>
                
                r/OUTPUT_VOLTAGE - Displays output voltage value from system.<br>
                r/DESIRED_VOLTAGE - Displays desired voltage value.<br>
                r/MIN_TEMP - Displays minimum temperature threshold.<br>
                r/MAX_TEMP - Displays maximum temperature threshold.<br>
                r/MIN_HV - Displays minimum high voltage threshold.<br>
                r/MAX_HV - Displays maximum high voltage threshold.<br>
                r/CURRENT_TEMP - Displays  current temperature.<br>
                r/MODE - Displays operating mode.<br>
                r/STATUS - Displays system status.<br>
                r/LED_MODE - Displays LED mode.<br>
                r/MANUFACTURER_ID - Displays manufacturer ID.<br>
                r/DUMP - Displays system information dump.<br><br>
        
                /clear - Clears  terminal.<br>"""
            self.terminalTextEdit.append(help_text)
                   
        elif self.is_connected:
            data = self.sendLineEdit.text()
            self.serial_thread.port.write(data.encode())
            received=self.serial_thread.port.readline().decode().strip()
            print(received)
            self.terminalTextEdit.append(received)

        self.sendLineEdit.setEnabled(False)
        self.sendCommandButton.setEnabled(False)
        self.terminal_timer.start()

    

    def send_configuration(self):
        if self.is_connected:
            self.is_configuring = True
            commands = [
                "w/DEVICE_MODE=1",
                f"w/MIN_HV={self.minVoltageSpinBox.value()}",
                f"w/MAX_HV={self.maxVoltageSpinBox.value()}",
                f"w/MIN_TEMP={self.minTempSpinBox.value()}",
                f"w/MAX_TEMP={self.maxTempSpinBox.value()}"
            ]

            self.serial_thread.start_configure()
            self.serial_thread.data_received.connect(self.terminalTextEdit.append)

            for command in commands:
                print(command)
                self.serial_thread.send_configure_signal.emit(command)
                QThread.msleep(10)  # Short delay between commands

            self.serial_thread.data_received.disconnect(self.terminalTextEdit.append)
            self.serial_thread.stop_configure()
            self.is_configuring = False 

    def sliderChange(self, value, spinbox):
        spinbox.setValue(value*self.scale)

    def spinboxChange(self, value, slider):
        slider.setValue(int(value/self.scale))

    def upload_data(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Dosya Seç")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Text files (*.txt)")

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                file_path = selected_files[0]
                current_directory = os.path.dirname(os.path.abspath(__file__))
                target_directory = os.path.join(current_directory, "Product Calibrations")
                try:
                    os.makedirs(target_directory, exist_ok=True)
                    shutil.copy(file_path, target_directory)
                    print(f"{file_path} dosyası {target_directory} dizinine başarıyla kopyalandı.")
                except Exception as e:
                    print(f"Dosya kopyalama hatası: {e}")
        self.listeDosyaAdlari()

    def listeDosyaAdlari(self):
        hedef_dizin = "Product Calibrations"
        os.makedirs(hedef_dizin, exist_ok=True)
        dosya_adlari = os.listdir(hedef_dizin)
        self.configsComboBox.clear()
        self.configsComboBox.addItems(dosya_adlari)

    def show_popup(self):
        dialog = PopupDialog(parent=self)
        if dialog.exec():
            print("Kayıt edilen veriler:")

    def onComboBoxIndexChanged(self, index):
        file="Product Calibrations/"+self.configsComboBox.itemText(index)
        try:
            with open(file, 'r') as dosya:
                satirlar = dosya.readlines()

                sayi1 = float(satirlar[0].strip()) if len(satirlar) > 0 else None
                sayi2 = float(satirlar[1].strip()) if len(satirlar) > 1 else None
                sayi3 = float(satirlar[2].strip()) if len(satirlar) > 2 else None
                sayi4 = float(satirlar[3].strip()) if len(satirlar) > 3 else None
                
                print(sayi1,sayi2,sayi3,sayi4,)
                print(int(sayi1/self.scale))
                self.minVoltageSlider.setValue(int(sayi1/self.scale))
                self.maxVoltageSlider.setValue(int(sayi2/self.scale))
                self.minTempSlider.setValue(int(sayi3/self.scale))
                self.maxTempSlider.setValue(int(sayi4/self.scale))

        except FileNotFoundError:
            print(f"{file} dosyası bulunamadı.")
