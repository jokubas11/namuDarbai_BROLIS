# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'programa.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 459)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.mygtGautiTemperatura = QtWidgets.QPushButton(self.centralwidget)
        self.mygtGautiTemperatura.setGeometry(QtCore.QRect(130, 30, 331, 31))
        self.mygtGautiTemperatura.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.mygtGautiTemperatura.setObjectName("mygtTemperatura")
        self.mygtGautiTemperatura.clicked.connect(self.gautiTemperatura)
        
        self.mygtGautiLaika = QtWidgets.QPushButton(self.centralwidget)
        self.mygtGautiLaika.setGeometry(QtCore.QRect(130, 90, 331, 31))
        self.mygtGautiLaika.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.mygtGautiLaika.setObjectName("mygtGautiLaika")
        self.mygtGautiLaika.clicked.connect(self.gautiLaika)
        
        self.mygtGautiVardaSerNr = QtWidgets.QPushButton(self.centralwidget)
        self.mygtGautiVardaSerNr.setGeometry(QtCore.QRect(130, 120, 331, 31))
        self.mygtGautiVardaSerNr.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.mygtGautiVardaSerNr.setObjectName("mygtGautiVarda")
        self.mygtGautiVardaSerNr.clicked.connect(self.gautiVardaSerNr)
        
        self.mygtGautiMygtuka = QtWidgets.QPushButton(self.centralwidget)
        self.mygtGautiMygtuka.setGeometry(QtCore.QRect(130, 60, 331, 31))
        self.mygtGautiMygtuka.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.mygtGautiMygtuka.setObjectName("mygtGautiMygtuka")
        self.mygtGautiMygtuka.clicked.connect(self.gautiMygtuka)
        
        self.infoLaukas = QtWidgets.QLabel(self.centralwidget)
        self.infoLaukas.setGeometry(QtCore.QRect(130, 170, 331, 51))
        self.infoLaukas.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.infoLaukas.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLaukas.setObjectName("infoLaukas")

        self.infoLaukas2 = QtWidgets.QLabel(self.centralwidget)
        self.infoLaukas2.setGeometry(QtCore.QRect(130, 350, 331, 51))
        self.infoLaukas2.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.infoLaukas2.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLaukas2.setObjectName("infoLaukas2")
        
        self.serNrTekstas = QtWidgets.QLineEdit(self.centralwidget)
        self.serNrTekstas.setGeometry(QtCore.QRect(70, 310, 191, 21))
        self.serNrTekstas.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.serNrTekstas.setObjectName("serNrTekstas")

        self.vardasTekstas = QtWidgets.QLineEdit(self.centralwidget)
        self.vardasTekstas.setGeometry(QtCore.QRect(70, 280, 191, 21))
        self.vardasTekstas.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.vardasTekstas.setText("")
        self.vardasTekstas.setObjectName("vardasTekstas")

        self.mygtNustatytiLaika = QtWidgets.QPushButton(self.centralwidget)
        self.mygtNustatytiLaika.setGeometry(QtCore.QRect(130, 230, 331, 31))
        self.mygtNustatytiLaika.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.mygtNustatytiLaika.setObjectName("mygtNustatytiLaika")
        self.mygtNustatytiLaika.clicked.connect(self.nustatytiLaika)

        self.mygtNustatytiVarda = QtWidgets.QPushButton(self.centralwidget)
        self.mygtNustatytiVarda.setGeometry(QtCore.QRect(280, 280, 271, 20))
        self.mygtNustatytiVarda.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.mygtNustatytiVarda.setObjectName("mygtNustatytiVarda")
        self.mygtNustatytiVarda.clicked.connect(self.nustatytiVarda)

        self.mygtNustatytiSerNr = QtWidgets.QPushButton(self.centralwidget)
        self.mygtNustatytiSerNr.setGeometry(QtCore.QRect(280, 310, 271, 21))
        self.mygtNustatytiSerNr.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.mygtNustatytiSerNr.setObjectName("mygtNustatytiSerNr")
        self.mygtNustatytiSerNr.clicked.connect(self.nustatytiSerNr)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mygtGautiTemperatura.setText(_translate("MainWindow", "Nuskaityti temperatūrą"))
        self.mygtGautiLaika.setText(_translate("MainWindow", "Nuskaityti laiką ir datą"))
        self.mygtGautiVardaSerNr.setText(_translate("MainWindow", "Nuskaityti prietaiso vardą ir serijinį numerį"))
        self.mygtGautiMygtuka.setText(_translate("MainWindow", "Nuskaityti mygtuko būseną"))
        self.infoLaukas.setText(_translate("MainWindow", ""))
        self.mygtNustatytiLaika.setText(_translate("MainWindow", "Nustatyti prietaisui kompiuterio laiką ir datą"))
        self.mygtNustatytiVarda.setText(_translate("MainWindow", "Nustatyti prietaiso vardą"))
        self.mygtNustatytiSerNr.setText(_translate("MainWindow", "Nustatyti prietaiso serijinį numerį"))
        self.infoLaukas2.setText(_translate("MainWindow", ""))

    def gautiTemperatura(self):
        self.infoLaukas2.setText("")

        char = 'u'
        serialPort.write(char.encode())

        self.infoLaukas.setText("temperatura yra 45 abarotai")
        
        

    def gautiMygtuka(self):
        self.infoLaukas2.setText("")

        char = 'd'
        serialPort.write(char.encode())

        self.infoLaukas.setText("mygtukas")

    def gautiVardaSerNr(self):
        self.infoLaukas2.setText("")

        char = 'a'
        serialPort.write(char.encode())

        self.infoLaukas.setText("vardas ser nr")

    def gautiLaika(self):
        self.infoLaukas2.setText("")

        char = 'b'
        serialPort.write(char.encode())

        self.infoLaukas.setText("laikas")

    def nustatytiLaika(self):
        self.infoLaukas.setText("")

        char = 'c'
        serialPort.write(char.encode())

        self.infoLaukas2.setText("nustatytas laikas")

    def nustatytiVarda(self):
        self.infoLaukas.setText("")

        tekstoLaukas = self.vardasTekstas.text()
        self.vardasTekstas.setText("")

        self.infoLaukas2.setText(tekstoLaukas)

    def nustatytiSerNr(self):
        self.infoLaukas.setText("")

        tekstoLaukas = self.serNrTekstas.text()
        self.serNrTekstas.setText("")

        self.infoLaukas2.setText(tekstoLaukas)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    serialPort = serial.Serial('/dev/serial/by-id/usb-mbed_Microcontroller_101000000000000000000002F7F2EE10-if01', 9600)
    
    MainWindow.show()
    sys.exit(app.exec_())