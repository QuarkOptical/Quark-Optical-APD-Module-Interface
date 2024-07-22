def setup_terminal_connections(main_window):
    main_window.dumpButton.clicked.connect(lambda:send_dump(main_window))
    main_window.sendCommandButton.clicked.connect(lambda:send_data(main_window))
    main_window.sendLineEdit.returnPressed.connect(lambda:send_data(main_window))
    main_window.clearButton.clicked.connect(main_window.terminalTextEdit.clear)
    main_window.buttongroup.buttonToggled.connect(lambda button: setLedMode(main_window, button))
    

def send_dump(main_window):
    main_window.serial_thread.port.write("r/DUMP".encode())
    received=main_window.serial_thread.port.read(200).decode().strip()
    main_window.terminalTextEdit.append(received)
    
def send_data(main_window):
    if main_window.sendLineEdit.text()=='/help' or main_window.sendLineEdit.text()== '/h':
        help_text="""
                Commands:<br>
                w/CURRENT_VOLTAGE=(number) - Sets desired voltage to number.<br>
                w/MODE=(number) - Sets operating mode to number.<br>
                w/MIN_TEMP=(number) - Sets minimum temperature threshold to number.<br>
                w/MAX_TEMP=(number) - Sets maximum temperature threshold to number.<br>
                w/MIN_HV=(number) - Sets minimum high voltage threshold to number.<br>
                w/MAX_HV=(number) - Sets maximum high voltage threshold to number.<br>
                w/LED_MODE=(number) - Sets LED mode to number.<br><br>
                
                r/MIN_TEMP - Displays minimum temperature threshold.<br>
                r/MAX_TEMP - Displays maximum temperature threshold.<br>
                r/MIN_HV - Displays minimum high voltage threshold.<br>
                r/MAX_HV - Displays maximum high voltage threshold.<br>
                r/CURRENT_VOLTAGE - Displays output voltage value from system.<br>
                r/CURRENT_TEMP - Displays  current temperature.<br>
                r/DEVICE_MODE - Displays operating mode.<br>
                r/DEVICE_STATUS - Displays system status.<br>
                r/LED_MODE - Displays LED mode.<br>
                r/MANUFACTURER_ID - Displays manufacturer ID.<br>
                r/DUMP - Displays system information dump.<br><br>
        
                /clear - Clears  terminal.<br>"""
        main_window.terminalTextEdit.append(help_text)
        
    elif main_window.sendLineEdit.text() in ["clear","/clear","cls"]:
        main_window.terminalTextEdit.clear()
    elif main_window.is_connected:
        data = main_window.sendLineEdit.text()
        if data=="r/DUMP":
            main_window.serial_thread.port.write(data.encode())
            received=main_window.serial_thread.port.read(200).decode().strip()
        else:
            main_window.serial_thread.port.write(data.encode())
            received=main_window.serial_thread.port.readline().decode().strip()
        main_window.terminalTextEdit.append(received)

    main_window.sendLineEdit.setEnabled(False)
    main_window.sendCommandButton.setEnabled(False)
    main_window.terminal_timer.start()

def setLedMode(main_window,button):
    if button.isChecked():
        if button==main_window.allRadioButton:
            send_only_data(main_window,"w/LED_MODE=0")
        elif button==main_window.onlyErrorRadioButton:
            send_only_data(main_window,"w/LED_MODE=1")
        elif button==main_window.offRadioButton:
            send_only_data(main_window,"w/LED_MODE=2")
            
def send_only_data(main_window,data):
    main_window.serial_thread.port.write(data.encode())
    received=main_window.serial_thread.port.readline().decode().strip()
    main_window.terminalTextEdit.append(received)