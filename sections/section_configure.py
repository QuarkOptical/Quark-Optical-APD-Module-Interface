def setup_configure_connections(main_window):
    main_window.minVoltageSlider.valueChanged.connect(lambda value: sliderChange(main_window, value, main_window.minVoltageSpinBox))
    main_window.maxVoltageSlider.valueChanged.connect(lambda value: sliderChange(main_window, value, main_window.maxVoltageSpinBox))
    main_window.minTempSlider.valueChanged.connect(lambda value: sliderChange(main_window, value, main_window.minTempSpinBox))
    main_window.maxTempSlider.valueChanged.connect(lambda value: sliderChange(main_window, value, main_window.maxTempSpinBox))
    main_window.minVoltageSpinBox.valueChanged.connect(lambda value: spinboxChange(main_window, value, main_window.minVoltageSlider))
    main_window.maxVoltageSpinBox.valueChanged.connect(lambda value: spinboxChange(main_window, value, main_window.maxVoltageSlider))
    main_window.minTempSpinBox.valueChanged.connect(lambda value: spinboxChange(main_window, value, main_window.minTempSlider))
    main_window.maxTempSpinBox.valueChanged.connect(lambda value: spinboxChange(main_window, value, main_window.maxTempSlider))

    main_window.startProcessButton.clicked.connect(lambda: toggle_process(main_window))
    main_window.configureButton.clicked.connect(lambda:send_configuration(main_window))
    
def sliderChange(main_window, value, spinbox):
    spinbox.setValue(value*main_window.scale)

def spinboxChange(main_window, value, slider):
    slider.setValue(int(value/main_window.scale))
    
def toggle_process(main_window):
    if not main_window.is_started:
        start_process(main_window)
    else:
        stop_process(main_window)
        
def start_process(main_window):
    main_window.gaugeWidget.gauge_status=0
    main_window.gaugeWidget.update()
    main_window.serial_thread.start_reading()
    main_window.serial_thread.data_received.connect(main_window.update_data)
        
    main_window.command_timer.start(100)
    main_window.is_started = True
    main_window.serial_thread.start_command()
    main_window.configureButton.setEnabled(False)
    main_window.HVProgressBar.setEnabled(True)
    main_window.connectButton.setEnabled(False)
    main_window.comPorts.setEnabled(False)
    main_window.refreshButton.setEnabled(False)
    main_window.set_controls(False)
    main_window.startProcessButton.setText("Stop Process")


def stop_process(main_window):
    main_window.gaugeWidget.gauge_status=1
    main_window.gaugeWidget.update()
    main_window.serial_thread.stop_reading()
    main_window.serial_thread.data_received.disconnect()
    main_window.command_timer.stop()
    main_window.is_started = False
    main_window.serial_thread.stop_command()
    main_window.HVProgressBar.setEnabled(False)
    main_window.configureButton.setEnabled(True)
    main_window.connectButton.setEnabled(True)
    main_window.comPorts.setEnabled(True)
    main_window.refreshButton.setEnabled(True)
    main_window.set_controls(True)
    main_window.startProcessButton.setText("Start Process")
    main_window.status="DISABLED"
    main_window.previous_status="DISABLED"
    main_window.aaaa.setStyleSheet("background-color: #A9A9A9;")
    
def send_configuration(main_window):
    if main_window.is_connected and main_window.serial_thread.port and main_window.serial_thread.port.is_open:
        command=f"w/CONFIGURE={main_window.minVoltageSpinBox.value()},{main_window.maxVoltageSpinBox.value()},{main_window.minTempSpinBox.value()},{main_window.maxTempSpinBox.value()}"
        main_window.serial_thread.port.write((command).encode())
        main_window.serial_thread.port.timeout = 1
        response = main_window.serial_thread.port.readline().decode().strip()
        if response:
            main_window.terminalTextEdit.append(response)
        else:
            main_window.serial_thread.error_occurred.emit("No response from the serial port.")