# Form implementation generated from reading ui file 'd:\QT WORKSPACE\deneme1\Quark-Optical-APD-Module-Interface\ui\dialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 250)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 312, 180))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 0, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.minVoltageLabel_ = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minVoltageLabel_.sizePolicy().hasHeightForWidth())
        self.minVoltageLabel_.setSizePolicy(sizePolicy)
        self.minVoltageLabel_.setObjectName("minVoltageLabel_")
        self.verticalLayout_3.addWidget(self.minVoltageLabel_)
        self.maxVoltageLabel_ = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxVoltageLabel_.sizePolicy().hasHeightForWidth())
        self.maxVoltageLabel_.setSizePolicy(sizePolicy)
        self.maxVoltageLabel_.setObjectName("maxVoltageLabel_")
        self.verticalLayout_3.addWidget(self.maxVoltageLabel_)
        self.maxTempLabel_ = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxTempLabel_.sizePolicy().hasHeightForWidth())
        self.maxTempLabel_.setSizePolicy(sizePolicy)
        self.maxTempLabel_.setObjectName("maxTempLabel_")
        self.verticalLayout_3.addWidget(self.maxTempLabel_)
        self.minTempLabel_ = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minTempLabel_.sizePolicy().hasHeightForWidth())
        self.minTempLabel_.setSizePolicy(sizePolicy)
        self.minTempLabel_.setObjectName("minTempLabel_")
        self.verticalLayout_3.addWidget(self.minTempLabel_)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.minVoltageSlider_ = QtWidgets.QSlider(parent=self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        self.minVoltageSlider_.setFont(font)
        self.minVoltageSlider_.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.minVoltageSlider_.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.minVoltageSlider_.setObjectName("minVoltageSlider_")
        self.verticalLayout_2.addWidget(self.minVoltageSlider_)
        self.maxVoltageSlider_ = QtWidgets.QSlider(parent=self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        self.maxVoltageSlider_.setFont(font)
        self.maxVoltageSlider_.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.maxVoltageSlider_.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.maxVoltageSlider_.setObjectName("maxVoltageSlider_")
        self.verticalLayout_2.addWidget(self.maxVoltageSlider_)
        self.minTempSlider_ = QtWidgets.QSlider(parent=self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        self.minTempSlider_.setFont(font)
        self.minTempSlider_.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.minTempSlider_.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.minTempSlider_.setObjectName("minTempSlider_")
        self.verticalLayout_2.addWidget(self.minTempSlider_)
        self.maxTempSlider_ = QtWidgets.QSlider(parent=self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        self.maxTempSlider_.setFont(font)
        self.maxTempSlider_.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.maxTempSlider_.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.maxTempSlider_.setObjectName("maxTempSlider_")
        self.verticalLayout_2.addWidget(self.maxTempSlider_)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.minVoltageSpinBox_ = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_5)
        self.minVoltageSpinBox_.setObjectName("minVoltageSpinBox_")
        self.verticalLayout_4.addWidget(self.minVoltageSpinBox_)
        self.maxVoltageSpinBox_ = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_5)
        self.maxVoltageSpinBox_.setObjectName("maxVoltageSpinBox_")
        self.verticalLayout_4.addWidget(self.maxVoltageSpinBox_)
        self.minTempSpinBox_ = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_5)
        self.minTempSpinBox_.setObjectName("minTempSpinBox_")
        self.verticalLayout_4.addWidget(self.minTempSpinBox_)
        self.maxTempSpinBox_ = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_5)
        self.maxTempSpinBox_.setObjectName("maxTempSpinBox_")
        self.verticalLayout_4.addWidget(self.maxTempSpinBox_)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 4)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(200, 200, 121, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.saveButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_3.addWidget(self.saveButton)
        self.cancelButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Product Name"))
        self.minVoltageLabel_.setText(_translate("Dialog", "Min High Voltage"))
        self.maxVoltageLabel_.setText(_translate("Dialog", "Max High Voltage"))
        self.maxTempLabel_.setText(_translate("Dialog", "Min Temperature"))
        self.minTempLabel_.setText(_translate("Dialog", "Max Temperature"))
        self.saveButton.setText(_translate("Dialog", "Kaydet"))
        self.cancelButton.setText(_translate("Dialog", "Çıkış"))