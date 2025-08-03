# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mymusic.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.938, stop:0 rgba(0, 0, 0, 255), stop:0.960452 rgba(48, 3, 127, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_background = QLabel(self.centralwidget)
        self.button_background.setObjectName(u"button_background")
        self.button_background.setGeometry(QRect(0, 430, 700, 71))
        self.button_background.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"border:5px solid;\n"
"border-radius:10px;\n"
"border-color: rgb(42, 42, 42);")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(5, 45, 690, 380))
        self.listWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 20);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(455, 432, 239, 61))
        self.frame.setStyleSheet(u"background-color: transparent")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prevbtn = QPushButton(self.frame)
        self.prevbtn.setObjectName(u"prevbtn")
        self.prevbtn.setMinimumSize(QSize(51, 51))
        self.prevbtn.setBaseSize(QSize(51, 51))
        font = QFont()
        font.setPointSize(15)
        self.prevbtn.setFont(font)
        self.prevbtn.setStyleSheet(u"background-color: rgba(0, 0, 0, 180);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.prevbtn)

        self.playbtn = QPushButton(self.frame)
        self.playbtn.setObjectName(u"playbtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.playbtn.sizePolicy().hasHeightForWidth())
        self.playbtn.setSizePolicy(sizePolicy)
        self.playbtn.setMinimumSize(QSize(51, 51))
        self.playbtn.setBaseSize(QSize(51, 51))
        font1 = QFont()
        font1.setPointSize(13)
        self.playbtn.setFont(font1)
        self.playbtn.setStyleSheet(u"background-color: rgba(0, 0, 0, 180);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.playbtn)

        self.nextbtn = QPushButton(self.frame)
        self.nextbtn.setObjectName(u"nextbtn")
        self.nextbtn.setMinimumSize(QSize(51, 51))
        self.nextbtn.setFont(font)
        self.nextbtn.setStyleSheet(u"background-color: rgba(0, 0, 0, 180);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.nextbtn)

        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setGeometry(QRect(10, 430, 170, 71))
        self.frame1.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.horizontalLayout_2 = QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addbtn = QPushButton(self.frame1)
        self.addbtn.setObjectName(u"addbtn")
        self.addbtn.setMinimumSize(QSize(51, 51))
        self.addbtn.setBaseSize(QSize(51, 51))
        self.addbtn.setFont(font)
        self.addbtn.setStyleSheet(u"background-color: rgba(0, 0, 0, 180);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.addbtn)

        self.removebtn = QPushButton(self.frame1)
        self.removebtn.setObjectName(u"removebtn")
        self.removebtn.setMinimumSize(QSize(51, 51))
        self.removebtn.setBaseSize(QSize(51, 51))
        self.removebtn.setFont(font)
        self.removebtn.setStyleSheet(u"background-color: rgba(0, 0, 0, 180);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.removebtn)

        self.frame2 = QFrame(self.centralwidget)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setGeometry(QRect(5, 0, 690, 41))
        self.frame2.setStyleSheet(u"background-color: rgba(255, 255, 255, 20);")
        self.horizontalLayout_3 = QHBoxLayout(self.frame2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.yor_music_label = QLabel(self.frame2)
        self.yor_music_label.setObjectName(u"yor_music_label")
        self.yor_music_label.setMinimumSize(QSize(4, 30))
        self.yor_music_label.setStyleSheet(u"background-color: rgba(255, 0, 0, 100);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.yor_music_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.yor_music_label)

        self.Yandex_importbtn = QPushButton(self.frame2)
        self.Yandex_importbtn.setObjectName(u"Yandex_importbtn")
        self.Yandex_importbtn.setMinimumSize(QSize(0, 30))
        self.Yandex_importbtn.setBaseSize(QSize(22, 30))
        font2 = QFont()
        font2.setPointSize(9)
        self.Yandex_importbtn.setFont(font2)
        self.Yandex_importbtn.setStyleSheet(u"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:1, stop:0.0225989 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 0, 255));\n"
"border:2px;\n"
"border-color: rgb(255, 247, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Yandex_importbtn.setIconSize(QSize(20, 16))

        self.horizontalLayout_3.addWidget(self.Yandex_importbtn)

        self.updatebtn = QPushButton(self.centralwidget)
        self.updatebtn.setObjectName(u"updatebtn")
        self.updatebtn.setGeometry(QRect(650, 50, 41, 41))
        self.updatebtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);\n"
"icon-color: rgb(255,255,255)")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemReboot))
        self.updatebtn.setIcon(icon)
        self.updatebtn.setIconSize(QSize(18, 18))
        self.updatebtn.setAutoRepeat(True)
        self.updatebtn.setAutoRepeatDelay(500)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MyMusic", None))
        self.button_background.setText("")
        self.prevbtn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.playbtn.setText(QCoreApplication.translate("MainWindow", u"| |", None))
        self.nextbtn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.addbtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removebtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.yor_music_label.setText(QCoreApplication.translate("MainWindow", u"Your Music", None))
#if QT_CONFIG(tooltip)
        self.Yandex_importbtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Yandex_importbtn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Yandex_importbtn.setText(QCoreApplication.translate("MainWindow", u"Input from Yandex Music", None))
        self.updatebtn.setText("")
    # retranslateUi

