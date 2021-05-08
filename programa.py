from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time
from datetime import datetime

class Ui_MainWindow(object):
    
    """
    Tiesiog user interface, nustato vieta, mygtuku vardus ir prijungia
    juos prie tam skirtu funkciju
    """
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 459)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.istrintiAtminti = QtWidgets.QPushButton(self.centralwidget)
        self.istrintiAtminti.setGeometry(QtCore.QRect(130, 130, 331, 31))
        self.istrintiAtminti.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.istrintiAtminti.setObjectName("istrintiAtminti")
        self.istrintiAtminti.clicked.connect(self.trintiAtminti)

        self.mygtGautiTemperatura = QtWidgets.QPushButton(self.centralwidget)
        self.mygtGautiTemperatura.setGeometry(QtCore.QRect(130, 10, 331, 31))
        self.mygtGautiTemperatura.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.mygtGautiTemperatura.setObjectName("mygtTemperatura")
        self.mygtGautiTemperatura.clicked.connect(self.gautiTemperatura)
        
        self.mygtGautiLaika = QtWidgets.QPushButton(self.centralwidget)
        self.mygtGautiLaika.setGeometry(QtCore.QRect(130, 70, 331, 31))
        self.mygtGautiLaika.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.mygtGautiLaika.setObjectName("mygtGautiLaika")
        self.mygtGautiLaika.clicked.connect(self.gautiLaika)
        
        self.mygtGautiVardaSerNr = QtWidgets.QPushButton(self.centralwidget)
        self.mygtGautiVardaSerNr.setGeometry(QtCore.QRect(130, 100, 331, 31))
        self.mygtGautiVardaSerNr.setLocale(QtCore.QLocale(QtCore.QLocale.Lithuanian, QtCore.QLocale.Lithuania))
        self.mygtGautiVardaSerNr.setObjectName("mygtGautiVarda")
        self.mygtGautiVardaSerNr.clicked.connect(self.gautiVardaSerNr)
        
        self.mygtGautiMygtuka = QtWidgets.QPushButton(self.centralwidget)
        self.mygtGautiMygtuka.setGeometry(QtCore.QRect(130, 40, 331, 31))
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
        self.istrintiAtminti.setText(_translate("MainWindow", "Ištrinti atmintį"))
        self.mygtGautiLaika.setText(_translate("MainWindow", "Nuskaityti laiką ir datą"))
        self.mygtGautiVardaSerNr.setText(_translate("MainWindow", "Nuskaityti prietaiso vardą ir serijinį numerį"))
        self.mygtGautiMygtuka.setText(_translate("MainWindow", "Nuskaityti mygtuko būseną"))
        self.infoLaukas.setText(_translate("MainWindow", ""))
        self.mygtNustatytiLaika.setText(_translate("MainWindow", "Nustatyti prietaisui kompiuterio laiką ir datą"))
        self.mygtNustatytiVarda.setText(_translate("MainWindow", "Nustatyti prietaiso vardą"))
        self.mygtNustatytiSerNr.setText(_translate("MainWindow", "Nustatyti prietaiso serijinį numerį"))
        self.infoLaukas2.setText(_translate("MainWindow", ""))

    # Rasoma uzklausa skirta temperaturos nuskaitymui, po to apdorojamas atsakymas
    def gautiTemperatura(self):
        self.infoLaukas2.setText("")

        uzklausa = "a\n"
        atsakymas = self.siustiUzklausa(uzklausa)
        
        if atsakymas == 'a\n':
            self.infoLaukas.setText("Klaida matuojant temperaturą!")
        else:
            self.infoLaukas.setText("Temperatūra: " + atsakymas[1:])

    # Rasoma uzklausa skirta mygtuko busenai, po to apdorojamas atsakymas    
    def gautiMygtuka(self):
        self.infoLaukas2.setText("")

        uzklausa = 'b\n'
        atsakymas = self.siustiUzklausa(uzklausa)

        if atsakymas == 'b1\n':
            self.infoLaukas.setText("Mygtukas yra paspaustas")
        elif atsakymas == 'b2\n':
            self.infoLaukas.setText("Mygtukas nėra paspaustas")
        else:
            self.infoLaukas.setText("Nenumatyta klaida!")

    # Rasoma uzklausa skirta duomenu gavimui, po to apdorojamas atsakymas
    def gautiVardaSerNr(self):
        self.infoLaukas2.setText("")

        uzklausa = 'c\n'
        atsakymas = self.siustiUzklausa(uzklausa)

        if atsakymas == 'c\n':
            self.infoLaukas.setText("Prietaisas neturi nei vardo, nei serijinio numerio")
        elif atsakymas == 'x\n':
            self.infoLaukas.setText("Nenumatyta klaida")
        else:
            vardas = atsakymas[0:15]
            serijinisNr = atsakymas[16:32]

            if vardas.isspace():
                vardasStr = "Prietaisas neturi vardo"
            else:
                vardasStr = "Prietaiso vardas yra: " + vardas

            if serijinisNr.isspace():
                serijinisNrStr = "Prietaisas neturi serijinio numerio"
            else:
                serijinisNrStr = "Prietaiso serijinis numeris yra: " + serijinisNr
            
            self.infoLaukas.setText(vardasStr + '\n' + serijinisNrStr)

    # Rasoma uzklausa skirta laiko gavimui, po to apdorojamas atsakymas
    def gautiLaika(self):
        self.infoLaukas2.setText("")

        uzklausa = 'd\n'
        atsakymas = self.siustiUzklausa(uzklausa)

        if atsakymas == 'd-1\n':
            self.infoLaukas.setText("Prietaisas neturi nustatyto laiko")
        else:
            try:
                laikas = int(atsakymas[1:])
                laikasStr = datetime.utcfromtimestamp(laikas).strftime('%Y-%m-%d %H:%M:%S')
                self.infoLaukas.setText("Dabar yra: " + laikasStr)
            except:
                self.infoLaukas.setText("Nenumatyta klaida!")        

    # Rasoma uzklausa skirta laiko nustatymui, po to apdorojamas atsakymas
    def nustatytiLaika(self):
        self.infoLaukas.setText("")

        try:
            uzklausa = 'e' + str(round(time.clock_gettime(time.CLOCK_REALTIME) + 3600)) + '\n'
        except:
            uzklausa = 'k\n'
        atsakymas = self.siustiUzklausa(uzklausa)

        if atsakymas == 'e\n':
            self.infoLaukas2.setText("Naujas laikas nustatytas sėkmingai")
        else:
            self.infoLaukas.setText("Nenumatyta klaida!")

    # Rasoma uzklausa skirta vardo nustatymui, po to apdorojamas atsakymas    
    def nustatytiVarda(self):
        self.infoLaukas.setText("")

        try:
            tekstoLaukas = self.vardasTekstas.text()
            uzklausa = 'f' + str(tekstoLaukas) + '\n'
        except:
            uzklausa = 'k\n'
        atsakymas = self.siustiUzklausa(uzklausa)

        if atsakymas == 'f\n':
            self.infoLaukas2.setText("Naujas vardas nustatytas sėkmingai")
        else:
            self.infoLaukas2.setText("Nenumatyta klaida!")        

    # Rasoma uzklausa skirta serijinio nr nuskaitymui, po to apdorojamas atsakymas
    def nustatytiSerNr(self):
        self.infoLaukas.setText("")

        try:
            tekstoLaukas = self.serNrTekstas.text()
            uzklausa = 'g' + str(tekstoLaukas) + '\n'
        except:
            uzklausa = 'k\n'
        atsakymas = self.siustiUzklausa(uzklausa)

        if atsakymas == 'f\n':
            self.infoLaukas2.setText("Naujas serijinis numeris nustatytas sėkmingai")
        else:
            self.infoLaukas2.setText("Nenumatyta klaida!")       

    # Rasoma uzklausa skirta atminties trynimui, po to apdorojamas atsakymas
    def trintiAtminti(self):
        self.infoLaukas2.setText("")
        uzklausa = "h\n"
        atsakymas = self.siustiUzklausa(uzklausa)
        
        if atsakymas == "h\n":
            self.infoLaukas.setText("Atmintis ištrinta sėkmingai")
        else:
            self.infoLaukas2.setText("Nenumatyta klaida!")
        
    """
    Sioje funkcijoje mes nusiunciame uzklausa mbedui
    
    uzklausa turi nuo 2 iki 18 simboliu
    uzklausa[0] yra simbolis, kuris pasako mbedui i kuria funkcija kreiptis
    
    pavyzdziui, jeigu mbedas gauna uzklausa[0] = 'a', reiskia, kad kompiuteris
    paprase pamatuoti temperatura

    uzklausoms siusti naudojamas serial modulis
    """    
    def siustiUzklausa(self, uzklausa):

        galimaSiustiUzklausa = True

        # patikrina ar nustatant varda arba serijini nr, teksto laukas nera tuscias
        if (uzklausa[0] in ['f', 'g']):
            
            if (len(uzklausa) < 3):
                self.infoLaukas2.setText("Palikote tuščią lauką")
                galimaSiustiUzklausa = False

            elif (len(uzklausa) > 18):
                self.infoLaukas2.setText("Maksimalus simbolių kiekis - 16")
                galimaSiustiUzklausa = False

        # patikrina ar nebuvo kokios klaidos
        if (uzklausa[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
            galimaSiustiUzklausa = False
            self.infoLaukas2.setText("Nenumatyta klaida")

        #jeigu visi kriterijai buvo praeiti, uzkoduoti uzklausa i baitus ir siusti
        if (galimaSiustiUzklausa):    
            
            #raso iki endline simbolio
            serialPort.write(uzklausa.encode())            
            
            # atsakymas is mbedo, kuris ateis tokia pacia forma
            # skaito iki endline simbolio
            # uzdetas 5 sekundziu timeout, jeigu iki tol nebus atsakymo, bus klaida
            atsakymas = serialPort.readline()
            atsakymas = line.decode()
            return atsakymas
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    serialPort = serial.Serial('/dev/serial/by-id/usb-mbed_Microcontroller_101000000000000000000002F7F2EE10-if01', 9600, timeout = 5)
    
    MainWindow.show()
    sys.exit(app.exec_())
