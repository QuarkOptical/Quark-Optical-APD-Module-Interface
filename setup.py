import sys
from cx_Freeze import setup, Executable

includefiles=["ui","assets","Product Calibrations"]
build_exe_options = {
    "packages": ["os", "re", "shutil", "PyQt6.QtWidgets", "PyQt6.QtGui", "PyQt6.QtCore", "PyQt6.QtSerialPort", "pyqtgraph", "webbrowser"],
    "includes": ["serial_thread", "info_dialog", "about_dialog","GaugeWidget", "CustomProgressBar","seri_port_okuyucu"],
    "include_files": includefiles,
    "excludes": []
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Tells the build script to hide the console.

executables = [
    Executable(
        "main.py", 
        base=base, 
        target_name="APD Module Interface.exe", 
        icon="sirket.ico"  # Add icon path if available
    )
]

setup(
    name="APD Module",
    version="0.1",
    description="Quark Optical APD Module Interface",
    options={"build_exe": build_exe_options},
    executables=executables
)
