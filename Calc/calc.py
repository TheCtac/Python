from PySide2 import QtWidgets
from calc_ui import Ui_MainWindow
import sys
import math

class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        self.show()
        self.res_ = None

        self.pushButton_1.clicked.connect(self.key_pressed)  # 1
        self.pushButton_2.clicked.connect(self.key_pressed)  # 2
        self.pushButton_3.clicked.connect(self.key_pressed)  # 3
        self.pushButton_4.clicked.connect(self.key_pressed)  # 4
        self.pushButton_5.clicked.connect(self.key_pressed)  # 5
        self.pushButton_6.clicked.connect(self.key_pressed)  # 6
        self.pushButton_7.clicked.connect(self.key_pressed)  # 7
        self.pushButton_8.clicked.connect(self.key_pressed)  # 8
        self.pushButton_9.clicked.connect(self.key_pressed)  # 9
        self.pushButton_0.clicked.connect(self.key_pressed)  # 0
        self.pushButton_pl.clicked.connect(self.key_pressed)  # +
        self.pushButton_mn.clicked.connect(self.key_pressed)  # -
        self.pushButton_dl.clicked.connect(self.key_pressed)  # /
        self.pushButton_mn_2.clicked.connect(self.key_pressed)  # *
        self.pushButton.clicked.connect(self.key_pressed)  # .
        self.pushButton_e.clicked.connect(self.result)  # =
    
    def key_pressed(self):
        button = self.sender()
        self.lineEdit.setText(self.lineEdit.text() + button.text())

    def result(self):
        input_ = self.lineEdit.text().strip()
        exec("self.res_ = " + input_)
        self.lineEdit.setText(str(self.res_))

if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Сздание инстанса класса
    calc = Calculator()
    # Запуск
    sys.exit(app.exec_())
