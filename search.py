from PyQt6 import QtCore, QtGui, QtWidgets
import pygetwindow as gw
import keyboard
import pyautogui
import time



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 133)
        MainWindow.setMinimumSize(QtCore.QSize(320, 133))
        MainWindow.setMaximumSize(QtCore.QSize(320, 133))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(180, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.errorLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(70, 100, 210, 25))
        self.errorLabel.setObjectName("errorLabel")
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.search)
        self.comboBox.currentIndexChanged.connect(self.handleComboBoxChange)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VLD - search"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ALL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "viejo pesca"))
        self.comboBox.setItemText(2, _translate("MainWindow", "pez dorado"))
        self.comboBox.setItemText(3, _translate("MainWindow", " Aibáo "))
        self.comboBox.setItemText(4, _translate("MainWindow", " Febáo "))
        self.comboBox.setItemText(5, _translate("MainWindow", "rouu"))
        self.comboBox.setItemText(6, _translate("MainWindow", "M A R S"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.radioButton.setText(_translate("MainWindow", "Phòng chờ"))
        self.radioButton.setChecked(True)
        self.radioButton_2.setText(_translate("MainWindow", "Tán gẫu"))
        self.radioButton_2.setDisabled(True)

    def handleComboBoxChange(self, index):
        selected_item = self.comboBox.itemText(index)

        if selected_item == "ALL":
            self.radioButton.setChecked(True)
            self.radioButton.setDisabled(False)
            self.radioButton_2.setDisabled(True)
        elif selected_item == "M A R S":
            self.radioButton.setDisabled(True)
            self.radioButton_2.setChecked(True)
            self.radioButton_2.setDisabled(False)
        else:
            self.radioButton.setChecked(True)
            self.radioButton.setDisabled(False)
            self.radioButton_2.setDisabled(False)

    def search(self):
        self.errorLabel.setText("")
        windows_name = "audition"
        windows = gw.getAllTitles()
        active_windows = [window for window in windows if windows_name in window.lower()]
        if active_windows:
            app_window = gw.getWindowsWithTitle(active_windows[0])[0]
            app_window.activate()
            MainWindow.move(1473, 141)
            action_dict = {
                "ALL": {
                    True: [self.viejo_pc, self.pez_pc, self.aibao_pc, self.febao_pc, self.rouu_pc],
                },
                "viejo pesca": {
                    True: self.viejo_pc,
                    False: self.viejo_tg
                },
                "pez dorado": {
                    True: self.pez_pc,
                    False: self.pez_tg
                },
                " Aibáo ": {
                    True: self.aibao_pc,
                    False: self.aibao_tg
                },
                " Febáo ": {
                    True: self.febao_pc,
                    False: self.febao_tg
                },
                "rouu": {
                    True: self.rouu_pc,
                    False: self.rouu_tg
                },
                "M A R S": {
                    False: self.mars
                }
            }
            
            combo_text = self.comboBox.currentText()
            radio_checked = self.radioButton.isChecked()
            
            if combo_text in action_dict:
                if radio_checked in action_dict[combo_text]:
                    action = action_dict[combo_text][radio_checked]
                    if isinstance(action, list):
                        for func in action:
                            app_window.activate()
                            func()
                    else:
                        app_window.activate()
                        action()
                else:
                    self.errorLabel.setText("Chọn Tán gẫu hoặc Phòng chờ")
        else:
            self.errorLabel.setText("Không tìm thấy Audition")
    def viejo_pc(self):
        time.sleep(1)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write('viejo')
        keyboard.write("\u00A0")
        keyboard.write('pesca')
        pyautogui.press('enter')

    def viejo_tg(self):
        time.sleep(1)
        keyboard.write('viejo')
        keyboard.write("\u00A0")
        keyboard.write('pesca')

    def pez_pc(self):
        time.sleep(1)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write('pez')
        keyboard.write("\u00A0")
        keyboard.write('dorado')
        pyautogui.press('enter')

    def pez_tg(self):
        time.sleep(1)
        keyboard.write('pez')
        keyboard.write("\u00A0")
        keyboard.write('dorado')

    def aibao_pc(self):
        time.sleep(1)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write("\u00A0")
        pyautogui.press('A')
        pyautogui.press('i')
        pyautogui.press('b')
        pyautogui.press('a')
        pyautogui.press('s')
        pyautogui.press('o')
        keyboard.write("\u00A0")
        pyautogui.press('enter')
    
    def aibao_tg(self):
        time.sleep(1)
        keyboard.write("\u00A0")
        pyautogui.press('A')
        pyautogui.press('i')
        pyautogui.press('b')
        pyautogui.press('a')
        pyautogui.press('s')
        pyautogui.press('o')
        keyboard.write("\u00A0")

    def febao_pc(self):
        time.sleep(1)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write("\u00A0")
        pyautogui.press('F')
        pyautogui.press('e')
        pyautogui.press('b')
        pyautogui.press('a')
        pyautogui.press('s')
        pyautogui.press('o')
        keyboard.write("\u00A0")
        pyautogui.press('enter')

    def febao_tg(self):
        time.sleep(1)
        keyboard.write("\u00A0")
        pyautogui.press('F')
        pyautogui.press('e')
        pyautogui.press('b')
        pyautogui.press('a')
        pyautogui.press('s')
        pyautogui.press('o')
        keyboard.write("\u00A0")

    def rouu_pc(self):
        time.sleep(1)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write('rouu')
        pyautogui.press('enter')

    def rouu_tg(self):
        time.sleep(1)
        keyboard.write('rouu')

    def mars(self):
        time.sleep(1)
        keyboard.write('kechatao113')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
