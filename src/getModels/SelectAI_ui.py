# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pax/REAL-Video-Enhancer/src/getModels/SelectAI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1155, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.InstallModelsFrame = QtWidgets.QFrame(self.centralwidget)
        self.InstallModelsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InstallModelsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InstallModelsFrame.setObjectName("InstallModelsFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.InstallModelsFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.InstallModelsFrame)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.InstallButton = QtWidgets.QPushButton(self.InstallModelsFrame)
        self.InstallButton.setObjectName("InstallButton")
        self.gridLayout.addWidget(self.InstallButton, 3, 0, 1, 1)
        self.installModelsProgressBar = QtWidgets.QProgressBar(self.InstallModelsFrame)
        self.installModelsProgressBar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.installModelsProgressBar.setProperty("value", 0)
        self.installModelsProgressBar.setTextVisible(False)
        self.installModelsProgressBar.setInvertedAppearance(False)
        self.installModelsProgressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.installModelsProgressBar.setObjectName("installModelsProgressBar")
        self.gridLayout.addWidget(self.installModelsProgressBar, 4, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.RealSRCheckBox = QtWidgets.QCheckBox(self.InstallModelsFrame)
        self.RealSRCheckBox.setEnabled(True)
        self.RealSRCheckBox.setObjectName("RealSRCheckBox")
        self.gridLayout_6.addWidget(self.RealSRCheckBox, 6, 0, 1, 1)
        self.RealCUGANCheckBox = QtWidgets.QCheckBox(self.InstallModelsFrame)
        self.RealCUGANCheckBox.setEnabled(True)
        self.RealCUGANCheckBox.setObjectName("RealCUGANCheckBox")
        self.gridLayout_6.addWidget(self.RealCUGANCheckBox, 1, 0, 1, 1)
        self.Waifu2xCheckBox = QtWidgets.QCheckBox(self.InstallModelsFrame)
        self.Waifu2xCheckBox.setObjectName("Waifu2xCheckBox")
        self.gridLayout_6.addWidget(self.Waifu2xCheckBox, 7, 0, 1, 1)
        self.RifeSettings = QtWidgets.QPushButton(self.InstallModelsFrame)
        self.RifeSettings.setObjectName("RifeSettings")
        self.gridLayout_6.addWidget(self.RifeSettings, 10, 1, 1, 1)
        self.RifeCheckBox = QtWidgets.QCheckBox(self.InstallModelsFrame)
        self.RifeCheckBox.setObjectName("RifeCheckBox")
        self.gridLayout_6.addWidget(self.RifeCheckBox, 10, 0, 1, 1)
        self.RealESRGANCheckBox = QtWidgets.QCheckBox(self.InstallModelsFrame)
        self.RealESRGANCheckBox.setObjectName("RealESRGANCheckBox")
        self.gridLayout_6.addWidget(self.RealESRGANCheckBox, 2, 0, 1, 1)
        self.CainCheckBox = QtWidgets.QCheckBox(self.InstallModelsFrame)
        self.CainCheckBox.setEnabled(True)
        self.CainCheckBox.setObjectName("CainCheckBox")
        self.gridLayout_6.addWidget(self.CainCheckBox, 14, 0, 1, 1)
        self.RifeVSCheckBox = QtWidgets.QCheckBox(self.InstallModelsFrame)
        self.RifeVSCheckBox.setEnabled(False)
        self.RifeVSCheckBox.setObjectName("RifeVSCheckBox")
        self.gridLayout_6.addWidget(self.RifeVSCheckBox, 11, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.InstallModelsFrame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "REAL Video Enhancer"))
        self.label_13.setText(_translate("MainWindow", "Models:"))
        self.InstallButton.setText(_translate("MainWindow", "Install"))
        self.RealSRCheckBox.setText(_translate("MainWindow", "RealSR (Upscale General)"))
        self.RealCUGANCheckBox.setText(_translate("MainWindow", "RealCUGAN (Upscale Animation)"))
        self.Waifu2xCheckBox.setText(_translate("MainWindow", "Waifu2X  (Upscale Animation)"))
        self.RifeSettings.setText(_translate("MainWindow", "Settings"))
        self.RifeCheckBox.setText(_translate("MainWindow", "RIFE (Interpolate General)"))
        self.RealESRGANCheckBox.setText(_translate("MainWindow", "RealESRGAN (Upscale Animation)"))
        self.CainCheckBox.setText(_translate("MainWindow", "IFRNET (Interpolate General)"))
        self.RifeVSCheckBox.setText(_translate("MainWindow", "VS-Rife (Interpolate General)"))
