from PyQt6.QtWidgets import QMessageBox
from serial_thread import SerialThread
from functools import partial

def setup_com_port_selection_connections(main_window):
    main_window.comPorts.currentIndexChanged.connect(partial(onPortChanged, main_window))
    main_window.refreshButton.clicked.connect(main_window.populateSerialPorts)
    main_window.connectButton.clicked.connect(partial(toggle_connection,main_window))
    
def onPortChanged(main_window):
    print(main_window)
    if main_window.serial_thread:
        selectedPortName = main_window.comPorts.currentText()
        main_window.serial_thread.set_port_name(selectedPortName)

def toggle_connection(main_window):
    if not main_window.is_connected:
        start_connection(main_window)
    else:
        stop_connection(main_window)
        
def start_connection(main_window):
    selected_port = main_window.comPorts.currentText()
    if not selected_port:
        QMessageBox.warning(main_window, "Warning", "Please select a serial port.")
        return
    main_window.serial_thread = SerialThread()
    main_window.serial_thread.error_occurred.connect(main_window.handle_error)
    main_window.serial_thread.set_port_name(selected_port)
    main_window.serial_thread.start()
    main_window.is_connected = True
    main_window.comPorts.setEnabled(False)
    main_window.refreshButton.setEnabled(False)
    main_window.configureButton.setEnabled(True)
    main_window.startProcessButton.setEnabled(True)
    main_window.HVProgressBar.setEnabled(True)
    main_window.set_controls_enabled(True)
    main_window.connectButton.setText("Disconnect")
    main_window.setup_config()
        
    main_window.sendLineEdit.setEnabled(True)
    main_window.terminalTextEdit.setEnabled(True)
    main_window.clearButton.setEnabled(True)
    main_window.dumpButton.setEnabled(True)
    main_window.sendCommandButton.setEnabled(True)
    main_window.allRadioButton.setEnabled(True)
    main_window.offRadioButton.setEnabled(True)
    main_window.onlyErrorRadioButton.setEnabled(True)


def stop_connection(main_window):
    main_window.serial_thread.stop()
    main_window.serial_thread = None
    main_window.is_connected = False
    main_window.comPorts.setEnabled(True)
    main_window.refreshButton.setEnabled(True)
    main_window.configureButton.setEnabled(False)
    main_window.startProcessButton.setEnabled(False)
    main_window.connectButton.setEnabled(True)
    main_window.comPorts.setEnabled(True)
    main_window.refreshButton.setEnabled(True)
    main_window.HVProgressBar.setEnabled(False)
    main_window.set_controls_enabled(False)
    main_window.connectButton.setText("Connect")
        
    main_window.sendLineEdit.setEnabled(False)
    main_window.terminalTextEdit.setEnabled(False)
    main_window.clearButton.setEnabled(False)
    main_window.dumpButton.setEnabled(False)
    main_window.sendCommandButton.setEnabled(False)
    main_window.allRadioButton.setEnabled(False)
    main_window.offRadioButton.setEnabled(False)
    main_window.onlyErrorRadioButton.setEnabled(False)