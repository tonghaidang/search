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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VLD - search"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ALL"))
        self.comboBox.setItemText(1, _translate("MainWindow", " Fubáo"))
        self.comboBox.setItemText(2, _translate("MainWindow", " Febáo"))
        self.comboBox.setItemText(3, _translate("MainWindow", "••Sun••"))
        self.comboBox.setItemText(4, _translate("MainWindow", "¬Sâu"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Meow"))
        self.comboBox.setItemText(6, _translate("MainWindow", "JeiiCy"))
        self.comboBox.setItemText(7, _translate("MainWindow", "GiaY"))
        self.comboBox.setItemText(8, _translate("MainWindow", "GiaThuann"))
        self.comboBox.setItemText(9, _translate("MainWindow", "M A R S"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.radioButton.setText(_translate("MainWindow", "Phòng chờ"))
        self.radioButton_2.setText(_translate("MainWindow", "Tán gẫu"))

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
                    True: [self.fubao_pc, self.febao_pc, self.sun_pc, self.sau_pc, self.jeiicy_pc, self.giay_pc, self.giathuan_pc],
                    False: lambda: self.errorLabel.setText("Chỉ hoạt động với Phòng chờ")
                },
                " Fubáo": {
                    True: self.fubao_pc,
                    False: self.fubao_tg
                },
                " Febáo": {
                    True: self.febao_pc,
                    False: self.febao_tg
                },
                "••Sun••": {
                    True: self.sun_pc,
                    False: self.sun_tg
                },
                "¬Sâu": {
                    True: self.sau_pc,
                    False: self.sau_tg
                },
                "Meow": {
                    True: self.meow_pc,
                    False: self.meow_tg
                },
                "JeiiCy": {
                    True: self.jeiicy_pc,
                    False: self.jeiicy_tg
                },
                "GiaY": {
                    True: self.giay_pc,
                    False: self.giay_tg
                },
                "GiaThuann": {
                    True: self.giathuan_pc,
                    False: self.giathuan_tg
                },
                "M A R S": {
                    True: lambda: self.errorLabel.setText("Chỉ hoạt động với Tán gẫu"),
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
    def fubao_pc(self):
        time.sleep(2)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write("\u00A0")
        pyautogui.press('F')
        pyautogui.press('u')
        pyautogui.press('b')
        pyautogui.press('a')
        pyautogui.press('s')
        pyautogui.press('o')
        keyboard.write("\u00A0")
        pyautogui.press('enter')
    
    def fubao_tg(self):
        time.sleep(2)
        keyboard.write("\u00A0")
        pyautogui.press('F')
        pyautogui.press('u')
        pyautogui.press('b')
        pyautogui.press('a')
        pyautogui.press('s')
        pyautogui.press('o')
        keyboard.write("\u00A0")

    def febao_pc(self):
        time.sleep(2)
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
        time.sleep(2)
        keyboard.write("\u00A0")
        pyautogui.press('F')
        pyautogui.press('e')
        pyautogui.press('b')
        pyautogui.press('a')
        pyautogui.press('s')
        pyautogui.press('o')
        keyboard.write("\u00A0")

    def sun_pc(self):
        time.sleep(2)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write("\u2022")
        keyboard.write("\u2022")
        pyautogui.press('S')
        pyautogui.press('u')
        pyautogui.press('n')
        keyboard.write("\u2022")
        keyboard.write("\u2022")
        pyautogui.press('enter')

    def sun_tg(self):
        time.sleep(2)
        keyboard.write("\u2022")
        keyboard.write("\u2022")
        pyautogui.press('S')
        pyautogui.press('u')
        pyautogui.press('n')
        keyboard.write("\u2022")
        keyboard.write("\u2022")

    def jeiicy_pc(self):
        time.sleep(2)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write('JeiiCy')
        pyautogui.press('enter')

    def jeiicy_tg(self):
        time.sleep(2)
        keyboard.write('JeiiCy')

    def giay_pc(self):
        time.sleep(2)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write('GiaY')
        pyautogui.press('enter')

    def giay_tg(self):
        time.sleep(2)
        keyboard.write('GiaY')

    def giathuan_pc(self):
        time.sleep(2)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write('GiaThuann')
        pyautogui.press('enter')

    def giathuan_tg(self):
        time.sleep(2)
        keyboard.write('GiaThuann')

    def mars(self):
        time.sleep(2)
        keyboard.write('kechatao113')

    def sau_pc(self):
        time.sleep(2)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write("\u00AC")
        keyboard.write('S')
        keyboard.press('a')
        keyboard.press('a')
        keyboard.press('u')
        keyboard.press('enter')

    def sau_tg(self):
        time.sleep(2)
        keyboard.write("\u00AC")
        keyboard.write('S')
        keyboard.press('a')
        keyboard.press('a')
        keyboard.press('u')

    def meow_pc(self):
        time.sleep(2)
        keyboard.press('/')
        keyboard.press('a')
        keyboard.press('i')
        keyboard.press_and_release("space")
        keyboard.write('Wilder')
        keyboard.write('\u00A0')
        keyboard.write('Meow')
        keyboard.press('enter')

    def meow_tg(self):
        time.sleep(2)
        keyboard.write('Wilder')
        keyboard.write('\u00A0')
        keyboard.write('Meow')

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
