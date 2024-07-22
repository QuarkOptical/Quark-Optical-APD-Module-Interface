from PyQt6.QtWidgets import QMainWindow, QMessageBox,QButtonGroup
from PyQt6.QtCore import QTimer, QThread
from PyQt6.QtSerialPort import QSerialPortInfo
import re
from ui_setup import setup_ui
from section_com_port_selection import setup_com_port_selection_connections,start_connection,stop_connection
from section_configure import setup_configure_connections,start_process,stop_process
from section_dialogs import setup_dialog_connection
from section_set_configuration import setup_set_configuration_connection
from section_terminal import setup_terminal_connections
from PyQt6 import uic
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_variables()
        setup_ui(self)
        setup_com_port_selection_connections(self)
        setup_configure_connections(self)
        setup_dialog_connection(self)
        setup_set_configuration_connection(self)
        setup_terminal_connections(self)
    
    def initialize_variables(self):
        uic.loadUi("ui/main_window.ui",self)
        self.buttongroup=QButtonGroup(self)
        self.min_hv=100
        self.max_hv=200
        self.min_temp=0
        self.max_temp=50
        self.scale = 0.01
        self.time = 0.0
        self.status="OKAY"
        self.previous_status="previous"
        self.times_v = []
        self.times_t = []
        self.is_configuring = False
        self.temp_data = []
        self.hv_data = []
        self.serial_thread = None
        self.is_connected = False
        self.is_started = False
        
        self.qss_file = "assets/styles/slider.qss"
        self.qss_file2 = "assets/styles/slider.qss"

     
        self.timer = QTimer()
        self.terminal_timer=QTimer()
        self.terminal_timer.setInterval(100)
        self.terminal_timer.setSingleShot(True)
        self.terminal_timer.timeout.connect(self.enable_terminal)
        
        
        self.timer.start(100)
        self.command_timer = QTimer()
        self.command_timer.timeout.connect(self.send_periodic_command)
        self.command_timer.start(100)
        
    def handle_error(self, error):
        if self.is_started:
            stop_process(self)
            
        if self.serial_thread:
            stop_connection(self)
            QMessageBox.critical(self, "Error", f"Error:\n{error}")
    
    def populateSerialPorts(self):
        self.comPorts.clear()
        ports = QSerialPortInfo.availablePorts()
        sorted_ports = sorted(ports, key=lambda port: port.portName())
        for port in sorted_ports:
            self.comPorts.addItem(port.portName())
            
    def update_data(self, data):
        status_match=re.match(r"i/DEVICE_STATUS=(\d+)", data)
        if status_match:
            self.status= float(status_match.group(1))
        temp_match = re.match(r"i/CURRENT_TEMP=(\d+)", data)
        hv_match = re.match(r"i/CURRENT_HV=(\d+)", data)
        if self.status!=self.previous_status:
            self.previous_status=self.status
            if self.status in [2,3,4]:
                self.aaaa.setStyleSheet("background-color: #A01526;")
            elif self.status==1:
                self.aaaa.setStyleSheet("background-color: #096bb2;")
            elif self.status==0:
                self.aaaa.setStyleSheet("background-color: #3A7900;")
            elif self.status in [5,"CALIBRATING"]:
                self.aaaa.setStyleSheet("background-color: #A9A9A9;")
            
        if self.status in [2,3,4]:
            pass
        elif self.status in [1,"CALIBRATING"]:
            pass
        elif self.status==0:
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
        
    def enable_terminal(self):
        self.sendLineEdit.setEnabled(True)
        self.sendCommandButton.setEnabled(True)
        
    def send_periodic_command(self):
        if self.is_connected and self.serial_thread and not self.is_configuring:
            try:
                self.serial_thread.send_command_signal.emit()
                self.serial_thread.toggle_command()
            except Exception as e:
                self.serial_thread.error_occurred.emit(str(e))
                
    
    def setup_config(self):
        if self.is_connected:
            try:
 
                self.is_configuring = True
                commands = [
                    "r/MIN_TEMP",
                    "r/MAX_TEMP",
                    "r/MIN_HV",
                    "r/MAX_HV",
                    "r/LED_MODE"
                ]

                self.serial_thread.start_configure()
                self.serial_thread.data_received.connect(self.setupconfigsection)

                for command in commands:
                    self.serial_thread.send_configure_signal.emit(command)
                    QThread.msleep(10)
                self.serial_thread.data_received.disconnect(self.setupconfigsection)
                self.serial_thread.stop_configure()
                self.is_configuring = False
            except Exception as e:
                self.handle_error(str(e))

    def setupconfigsection(self,data):
        min_temp_match = re.match(r"i/MIN_TEMP=(\d+)", data)
        max_temp_match = re.match(r"i/MAX_TEMP=(\d+)", data)
        min_hv_match = re.match(r"i/MIN_HV=(\d+)", data)
        max_hv_match = re.match(r"i/MAX_HV=(\d+)", data)
        led_match = re.match(r"i/LED_MODE=(\d+)", data)
        
        if min_temp_match:
            min_temp_value = float(min_temp_match.group(1))
            self.minTempSpinBox.setValue(min_temp_value*self.scale)
 
            
        elif max_temp_match:
            max_temp_value = float(max_temp_match.group(1))
            self.maxTempSpinBox.setValue(max_temp_value*self.scale)

            
        elif min_hv_match:
            min_hv_value = float(min_hv_match.group(1)) 
            self.minVoltageSpinBox.setValue(min_hv_value*self.scale)
            
        elif max_hv_match:
            max_hv_value = float(max_hv_match.group(1))
            self.maxVoltageSpinBox.setValue(max_hv_value*self.scale)
        
        elif led_match:
            led_value = float(led_match.group(1))
            if led_value==0:
                self.allRadioButton.setChecked(True)
            elif led_value==1:
                self.onlyErrorRadioButton.setChecked(True)
            elif led_value==2:
                self.offRadioButton.setChecked(True)

        else:
            self.handle_error("Unable to establish a UART connection. Please check the connection and try again. If the issue persists, contact support.")
  
        
    def set_controls_enabled(self, enabled):
        self.minVoltageSlider.setEnabled(enabled)
        self.maxVoltageSlider.setEnabled(enabled)
        self.minTempSlider.setEnabled(enabled)
        self.maxTempSlider.setEnabled(enabled)
        self.minVoltageSpinBox.setEnabled(enabled)
        self.maxVoltageSpinBox.setEnabled(enabled)
        self.minTempSpinBox.setEnabled(enabled)
        self.maxTempSpinBox.setEnabled(enabled)
        
    def list_files(self):
        hedef_dizin = "Product Calibrations"
        os.makedirs(hedef_dizin, exist_ok=True)
        dosya_adlari = os.listdir(hedef_dizin)
        self.configsComboBox.clear()
        self.configsComboBox.addItems(dosya_adlari)