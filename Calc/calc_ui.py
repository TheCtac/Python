from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(380, 515)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color : #fa0;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color : #DDD;\n"
"    color : #000; \n"
"    font-size : 18px;\n"
"    height : 40px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color : #EEE;\n"
"}\n"
"QLineEdit {\n"
"    font-size : 25px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 21, 341, 51))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 141, 341, 331))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_0 = QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")

        self.gridLayout.addWidget(self.pushButton_0, 3, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.pushButton_e = QPushButton(self.gridLayoutWidget)
        self.pushButton_e.setObjectName(u"pushButton_e")
        self.pushButton_e.setStyleSheet(u"QPushButton {\n"
"    background-color : #D11;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color : #F00;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_e, 3, 2, 1, 1)

        self.pushButton_0.raise_()
        self.pushButton_8.raise_()
        self.pushButton_5.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_9.raise_()
        self.pushButton.raise_()
        self.pushButton_e.raise_()
        self.pushButton_1.raise_()
        self.pushButton_2.raise_()
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 90, 341, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_pl = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_pl.setObjectName(u"pushButton_pl")
        self.pushButton_pl.setStyleSheet(u"QPushButton{\n"
"    background-color: #1c1;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: #0F0;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_pl)

        self.pushButton_mn = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_mn.setObjectName(u"pushButton_mn")
        self.pushButton_mn.setStyleSheet(u"QPushButton{\n"
"    background-color: #1c1;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: #0F0;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_mn)

        self.pushButton_dl = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_dl.setObjectName(u"pushButton_dl")
        self.pushButton_dl.setStyleSheet(u"QPushButton{\n"
"    background-color: #1c1;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: #0F0;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_dl)

        self.pushButton_mn_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_mn_2.setObjectName(u"pushButton_mn_2")
        self.pushButton_mn_2.setStyleSheet(u"QPushButton{\n"
"    background-color: #1c1;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: #0F0;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_mn_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 380, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Imput your data", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_e.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_pl.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_mn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_dl.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_mn_2.setText(QCoreApplication.translate("MainWindow", u"*", None))
    # retranslateUi

