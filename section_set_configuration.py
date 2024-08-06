from add_config_dialog import PopupDialog
from PyQt6.QtWidgets import QMessageBox,QFileDialog
import os
import shutil
def setup_set_configuration_connection(main_window):
    main_window.addConfigButton.clicked.connect(lambda:show_popup(main_window))
    main_window.configsComboBox.currentIndexChanged.connect(lambda index: onComboBoxIndexChanged(main_window, index))
    main_window.addToolButton.clicked.connect(lambda:upload_data(main_window))
    
def show_popup(main_window):
    dialog = PopupDialog(parent=main_window)
    dialog.setWindowTitle("Add Configuration Manually")
    if dialog.exec():
        pass
    
def onComboBoxIndexChanged(main_window, index):
    file="Product Calibrations/"+main_window.configsComboBox.itemText(index)
    try:
        with open(file, 'r') as dosya:
            lines = dosya.readlines()

            min_hv = float(lines[0].strip()) if len(lines) > 0 else None
            max_hv = float(lines[1].strip()) if len(lines) > 1 else None
            min_temp = float(lines[2].strip()) if len(lines) > 2 else None
            max_temp = float(lines[3].strip()) if len(lines) > 3 else None
            main_window.minVoltageSlider.setValue(int(min_hv/main_window.scale))
            main_window.maxVoltageSlider.setValue(int(max_hv/main_window.scale))
            main_window.minTempSlider.setValue(int(min_temp/main_window.scale))
            main_window.maxTempSlider.setValue(int(max_temp/main_window.scale))

    except FileNotFoundError:
        QMessageBox.warning(main_window, "Warning", f"{file} not found.")
        
def upload_data(main_window):
    file_dialog = QFileDialog(main_window)
    file_dialog.setWindowTitle("Dosya Seç")
    file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    file_dialog.setNameFilter("Text files (*.txt)")

    if file_dialog.exec():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            file_path = selected_files[0]
            target_directory = "Product Calibrations"
            try:
                os.makedirs(target_directory, exist_ok=True)
                shutil.copy(file_path, target_directory)                
            except Exception as e:
                QMessageBox.warning(main_window,"Error" ,f"File copy error:{str(e)}")
                
            main_window.list_files()
    
