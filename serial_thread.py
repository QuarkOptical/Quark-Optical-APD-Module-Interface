from PyQt6.QtCore import QThread, pyqtSignal
import serial
from PyQt6.QtWidgets import QMessageBox
class SerialThread(QThread):
    data_received = pyqtSignal(str)
    error_occurred = pyqtSignal(str)
    send_command_signal = pyqtSignal()
    send_configure_signal = pyqtSignal(str)
    setup_config_signal=pyqtSignal(str)
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.port = None
        self.port_name = None
        self.current_command = "r/CURRENT_TEMP"
        self.reading = False
        
    def start_command(self):
        self.send_command_signal.connect(self.send_command)
        
    def stop_command(self):
        self.send_command_signal.disconnect(self.send_command)
        
    def start_configure(self):
        self.send_configure_signal.connect(self.send_configuration)
    
    def stop_configure(self):
        self.send_configure_signal.disconnect(self.send_configuration)

    def start_setup(self):
        self.setup_config_signal.connect()

    def set_port_name(self, port_name):
        self.port_name = port_name
    
    

    def stop(self):
        self.reading = False
        if self.port:
            self.port.close()

    def start_reading(self):
        self.reading = True

    def stop_reading(self):
        self.reading = False

    def run(self):
        print("Thread started")
        try:
            if not self.port_name:
                raise serial.SerialException("Port name is not set")
            self.port = serial.Serial(self.port_name, 115200)
            print("Serial port opened")
            while True:
                if self.reading:
                    if self.port.in_waiting > 0:
                        data = self.port.readline().decode().strip()
                        self.data_received.emit(data)
                
                QThread.msleep(10)
        except serial.SerialException as e:
            self.error_occurred.emit(str(e))
           # QMessageBox.warning(self,"Error" ,f"Serial exception:{str(e)}")
        except Exception as e:
            self.error_occurred.emit(str(e))
           # QMessageBox.warning(self,"Error" ,f"Exception:{str(e)}")

    def send_command(self):
        if self.port and self.port.is_open:
            try:
                self.port.write((self.current_command).encode())         
            except Exception as e:
                self.error_occurred.emit(str(e))
                #QMessageBox.warning(self,"Error" ,f"Exception:{str(e)}")
    def toggle_command(self):
        if self.current_command == "r/CURRENT_TEMP":
            self.current_command = "r/CURRENT_HV"
        else:
            self.current_command = "r/CURRENT_TEMP"

    def send_configuration(self, command):
        if self.port and self.port.is_open:
            try:
                self.port.write((command).encode())
                response = self.port.readline().decode().strip()
                self.data_received.emit(response)
            except Exception as e:
                self.error_occurred.emit(str(e))
                QMessageBox.warning(self,"Error" ,f"Exception:{str(e)}")
        
    def setup_config(self, command):
        if self.port and self.port.is_open:
            try:
                self.port.write((command).encode())
                response = self.port.readline().decode().strip()
                
            except Exception as e:
                self.error_occurred.emit(str(e))
                QMessageBox.warning(self,"Error" ,f"Exception:{str(e)}")


