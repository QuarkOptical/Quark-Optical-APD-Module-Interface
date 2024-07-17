from PyQt6.QtWidgets import QDialog
from PyQt6 import uic
import os

class PopupDialog(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        uic.loadUi('ui/dialog.ui', self)
        self.scale=0.01
        
        self.minVoltageSlider_.setRange(10000,20000)
        self.maxVoltageSlider_.setRange(10000,20000)
        
        self.minTempSlider_.setRange(0,5000)
        self.maxTempSlider_.setRange(0,5000)
        

        self.minVoltageSpinBox_.setRange(0,200)
        self.maxVoltageSpinBox_.setRange(0,200)
        self.minTempSpinBox_.setRange(0,50)
        self.maxTempSpinBox_.setRange(0,50)
        
        self.saveButton.clicked.connect(self.on_save)
        self.cancelButton.clicked.connect(self.on_close)
        
        self.minVoltageSlider_.valueChanged.connect(lambda value: self.sliderChange(value, self.minVoltageSpinBox_))
        self.maxVoltageSlider_.valueChanged.connect(lambda value: self.sliderChange(value, self.maxVoltageSpinBox_))
        self.minTempSlider_.valueChanged.connect(lambda value: self.sliderChange(value, self.minTempSpinBox_))
        self.maxTempSlider_.valueChanged.connect(lambda value: self.sliderChange(value, self.maxTempSpinBox_))
        
        
        self.minVoltageSpinBox_.valueChanged.connect(lambda value: self.spinboxChange(value,self.minVoltageSlider_))
        self.maxVoltageSpinBox_.valueChanged.connect(lambda value: self.spinboxChange(value,self.maxVoltageSlider_))
        self.minTempSpinBox_.valueChanged.connect(lambda value: self.spinboxChange(value,self.minTempSlider_))
        self.maxTempSpinBox_.valueChanged.connect(lambda value: self.spinboxChange(value,self.maxTempSlider_))
        
        
    
    def on_save(self):
        with open("Product Calibrations/"+(self.lineEdit.text()+".txt"),'w')as file:
            file.write(f"{self.minVoltageSpinBox_.value()}\n")
            file.write(f"{self.maxVoltageSpinBox_.value()}\n")
            file.write(f"{self.minTempSpinBox_.value()}\n")
            file.write(f"{self.maxTempSpinBox_.value()}\n")
         
        self.accept()
        self.parent().listeDosyaAdlari()
    
    def on_close(self):
        self.reject()
    
    def sliderChange(self,value,spinbox):
        spinbox.setValue(value*self.scale)
        
    
    def spinboxChange(self,value,slider):
        slider.setValue(int(value/self.scale))