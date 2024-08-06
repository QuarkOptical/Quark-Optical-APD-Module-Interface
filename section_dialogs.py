from add_config_dialog import PopupDialog
from about_dialog import AboutDialog 
import webbrowser

def setup_dialog_connection(main_window):
    main_window.infoButton.clicked.connect(lambda:show_info(main_window))
    main_window.userGuideButton.clicked.connect(show_guide)
    

def show_info(main_window):
    info = AboutDialog(parent=main_window)
    if info.exec():
        pass
    
def show_guide():
    url = "https://github.com/QuarkOptical/Quark-Optical-APD-Module-Interface/blob/main/User%20Guide.md"  # Replace with the URL you want to open
    webbrowser.open(url)
