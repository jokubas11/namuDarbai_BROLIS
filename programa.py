from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time
from datetime import datetime

class Ui_MainWindow(object):


    """
    initializing method related to object placement within the interface window
    """
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 459)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.buttonDeleteMemory = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDeleteMemory.setGeometry(QtCore.QRect(130, 130, 331, 31))
        self.buttonDeleteMemory.setObjectName("buttonDeleteMemory")
        self.buttonDeleteMemory.clicked.connect(self.deleteFlashMemory)

        self.buttonGetTemp = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetTemp.setGeometry(QtCore.QRect(130, 10, 331, 31))
        self.buttonGetTemp.setObjectName("buttonGetTemp")
        self.buttonGetTemp.clicked.connect(self.getTemperature)
        
        self.buttonGetTime = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetTime.setGeometry(QtCore.QRect(130, 70, 331, 31))
        self.buttonGetTime.setObjectName("buttonGetTime")
        self.buttonGetTime.clicked.connect(self.getCurrentTime)
        
        self.buttonGetNameSerial = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetNameSerial.setGeometry(QtCore.QRect(130, 100, 331, 31))
        self.buttonGetNameSerial.setObjectName("buttonGetName")
        self.buttonGetNameSerial.clicked.connect(self.getNameAndSerial)
        
        self.buttonGetButton = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetButton.setGeometry(QtCore.QRect(130, 40, 331, 31))
        self.buttonGetButton.setObjectName("buttonGetButton")
        self.buttonGetButton.clicked.connect(self.getButton)
        
        self.infoField = QtWidgets.QLabel(self.centralwidget)
        self.infoField.setGeometry(QtCore.QRect(130, 170, 331, 51))
        self.infoField.setAlignment(QtCore.Qt.AlignCenter)
        self.infoField.setObjectName("infoField")

        self.infoField2 = QtWidgets.QLabel(self.centralwidget)
        self.infoField2.setGeometry(QtCore.QRect(130, 350, 331, 51))
        self.infoField2.setAlignment(QtCore.Qt.AlignCenter)
        self.infoField2.setObjectName("infoField2")
        
        self.serialTextField = QtWidgets.QLineEdit(self.centralwidget)
        self.serialTextField.setGeometry(QtCore.QRect(70, 310, 191, 21))
        self.serialTextField.setText("")
        self.serialTextField.setObjectName("serialTextField")

        self.nameTextField = QtWidgets.QLineEdit(self.centralwidget)
        self.nameTextField.setGeometry(QtCore.QRect(70, 280, 191, 21))
        self.nameTextField.setText("")
        self.nameTextField.setObjectName("nameTextField")

        self.buttonSetTime = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSetTime.setGeometry(QtCore.QRect(130, 230, 331, 31))
        self.buttonSetTime.setObjectName("buttonSetTime")
        self.buttonSetTime.clicked.connect(self.setCurrentTime)

        self.buttonSetName = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSetName.setGeometry(QtCore.QRect(280, 280, 271, 20))
        self.buttonSetName.setObjectName("buttonSetName")
        self.buttonSetName.clicked.connect(self.setDeviceName)

        self.buttonSetSerial = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSetSerial.setGeometry(QtCore.QRect(280, 310, 271, 21))
        self.buttonSetSerial.setObjectName("buttonSetSerial")
        self.buttonSetSerial.clicked.connect(self.setSerialNo)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonGetTemp.setText(_translate("MainWindow", "Read Temperature"))
        self.buttonDeleteMemory.setText(_translate("MainWindow", "Delete Flash Memory"))
        self.buttonGetTime.setText(_translate("MainWindow", "Read Date and Time"))
        self.buttonGetNameSerial.setText(_translate("MainWindow", "Read Name and Serial Number"))
        self.buttonGetButton.setText(_translate("MainWindow", "Read Button Status"))
        self.infoField.setText(_translate("MainWindow", ""))
        self.buttonSetTime.setText(_translate("MainWindow", "Set PC's Time and Date to Device"))
        self.buttonSetName.setText(_translate("MainWindow", "Set Name For Device"))
        self.buttonSetSerial.setText(_translate("MainWindow", "Set Serial Number For Device"))
        self.infoField2.setText(_translate("MainWindow", ""))

    # Function writes request to be sent to get temperature, after that, processing the result
    def getTemperature(self):
        self.infoField2.setText("")

        request = "a\n"
        answer = self.sendRequest(request)
        
        if answer == 'a\n':
            self.infoField.setText("Error while measuring temperature")
        else:
            self.infoField.setText("Temperature: " + answer[1:])

    # Function writes request to be sent to get button status, after that, processing the result    
    def getButton(self):
        self.infoField2.setText("")

        request = 'b\n'
        answer = self.sendRequest(request)

        if answer == 'b1\n':
            self.infoField.setText("Button is pressed")
        elif answer == 'b2\n':
            self.infoField.setText("Button is not pressed")
        else:
            self.infoField.setText("Unforeseen error")

    # Function writes request to be sent to get name and serial number, after that, processing the result
    def getNameAndSerial(self):
        self.infoField2.setText("")

        request = 'c\n'
        answer = self.sendRequest(request)

        if answer == 'c\n':
            self.infoField.setText("Device doesn't have name, nor serial number")
        elif answer == 'x\n':
            self.infoField.setText("Unforeseen error")
        else:
            deviceName = answer[0:15]
            serialNumber = answer[16:32]

            if deviceName.isspace():
                deviceNameStr = "Device doesn't have name"
            else:
                deviceNameStr = "Device name: " + deviceName

            if serialNumber.isspace():
                serialNumberStr = "Device does not have serial number"
            else:
                serialNumberStr = "Serial number: " + serialNumber
            
            self.infoField.setText(deviceNameStr + '\n' + serialNumberStr)


    # Function writes request to be sent to get time, after that, processing the result
    def getCurrentTime(self):
        self.infoField2.setText("")

        request = 'd\n'
        answer = self.sendRequest(request)

        if answer == 'd-1\n':
            self.infoField.setText("Device does not have set time")
        else:
            try:
                timeRTC = int(answer[1:])
                timeString = datetime.utcfromtimestamp(timeRTC).strftime('%Y-%m-%d %H:%M:%S')
                self.infoField.setText("Time now: " + timeString)
            except:
                self.infoField.setText("Unforeseen error")        

    # Function writes request to be sent to set time, after that, processing the result
    def setCurrentTime(self):
        self.infoField.setText("")

        try:
            request = 'e' + str(round(time.clock_gettime(time.CLOCK_REALTIME) + 3600)) + '\n'
        except:
            request = 'k\n'
        answer = self.sendRequest(request)

        if answer == 'e\n':
            self.infoField2.setText("New time set")
        else:
            self.infoField2.setText("Unforeseen error")

    # Function writes request to be sent to set name, after that, processing the result 
    def setDeviceName(self):
        self.infoField.setText("")

        try:
            textField = self.nameTextField.text()
            request = 'f' + str(textField) + '\n'
        except:
            request = 'k\n'
        answer = self.sendRequest(request)

        if answer == 'f\n':
            self.infoField2.setText("Device name set successfully")
        else:
            self.infoField2.setText("Unforeseen error")        

    # Function writes request to be sent to set serial number, after that, processing the result
    def setSerialNo(self):
        self.infoField.setText("")

        try:
            textField = self.serialTextField.text()
            request = 'g' + str(textField) + '\n'
        except:
            request = 'k\n'
        answer = self.sendRequest(request)

        if answer == 'f\n':
            self.infoField2.setText("Serial number set successfully")
        else:
            self.infoField2.setText("Unforeseen error")       

    # Function writes request to be sent to delete flash memory, after that, processing the result
    def deleteFlashMemory(self):
        self.infoField2.setText("")
        request = "h\n"
        answer = self.sendRequest(request)
        
        if answer == "h\n":
            self.infoField.setText("Memory deleted succesfully")
        else:
            self.infoField.setText("Unforeseen error")
        
    """
    In this function, request is sent to mbed
    
    request has from 2 to 18 symbols
    request[0] tells mbed which function to go to
    
    for example, if mbed gets request[0] = 'a', means that PC asked to get temperature

    serial module is used for two-way communication
    """    
    def sendRequest(self, request):

        canSetRequest = True

        # Checks if the text field is not empty
        if (request[0] in ['f', 'g']):
            
            if (len(request) < 3):
                self.infoField2.setText("You have left empty field")
                canSetRequest = False

            elif (len(request) > 18):
                self.infoField2.setText("Max symbol amount - 16")
                canSetRequest = False

        # Checks if there were any other mistakes in request
        if (request[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
            canSetRequest = False
            self.infoField.setText("Unforeseen error")

        # If all criterias passed, send the request
        if (canSetRequest):    
            
            # writes until endline symbol
            serialPort.write(request.encode())
                        
            # answer from mbed will come back in the same format
            # there is 5 second time out, if timeout is reached, error returned
            answer = serialPort.readline()
            answer = answer.decode()
            return answer
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    serialPort = serial.Serial('/dev/serial/by-id/usb-mbed_Microcontroller_101000000000000000000002F7F2EE10-if01', 9600, timeout = 5)
    
    MainWindow.show()
    sys.exit(app.exec_())
