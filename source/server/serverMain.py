import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# import openpyxl as xl
import stylesheet as style
import json
from UI import *
import serverSocket as sv

from threading import *
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


class serverUI(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("COVID-19 INFO HCMUS")
        self.resize(400, 550)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(style.css)
        self.server = sv.getSV()
        self.status = sv.SV.svInfo(self.server)
        self.add_list = sv.SV.addrInfo(self.server)
        sv.SV.takeUI(self.server, self)

        self.background = QWidget(self)
        self.background.setObjectName("background")
        self.background.setGeometry(
            QRect(20, 20, self.width() - 40, self.height() - 40)
        )
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setOffset(0, 0)
        self.shadow.setColor(QColor(0, 0, 0, 180))
        self.background.setGraphicsEffect(self.shadow)

        # self.background.setStyleSheet("background-color: green")

        # titlebar
        self.titlebar = QWidget(self)
        self.titlebar.setObjectName("titlebar")
        self.titlebar.setGeometry(
            QRect(self.background.x(), self.background.y(), self.background.width(), 40)
        )
        self.titlebar_shadow = QGraphicsDropShadowEffect()
        self.titlebar_shadow.setBlurRadius(10)
        self.titlebar_shadow.setOffset(0)
        self.titlebar.setGraphicsEffect(self.titlebar_shadow)
        self.titlebar.setStyleSheet(style.basegui)
        # self.titlebar.setStyleSheet("background-color: green")

        self.exit_button = QPushButton(self.titlebar)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setFixedSize(16, 16)
        self.exit_button.move(17, 12)
        self.exit_button.clicked.connect(self.closeDialog)

        self.minimize_button = QPushButton(self.titlebar)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.setCursor(self.exit_button.cursor())
        self.minimize_button.setFixedSize(16, 16)
        self.minimize_button.move(
            self.exit_button.x() + self.exit_button.width() + 10, self.exit_button.y()
        )
        self.minimize_button.clicked.connect(self.showMinimized)

        self.fullscreen_button = QPushButton(self.titlebar)
        self.fullscreen_button.setObjectName("fullscreen_button")
        self.fullscreen_button.setCursor(self.exit_button.cursor())
        self.fullscreen_button.setFixedSize(16, 16)
        self.fullscreen_button.move(
            self.minimize_button.x() + self.minimize_button.width() + 10,
            self.minimize_button.y(),
        )

        # hcmus logo widget
        self.logo_box = QWidget(self.background)
        self.logo_box.setObjectName("logo_box")
        self.logo_box.setGeometry(QRect(0, self.titlebar.height(), self.width(), 80))

        # to check the logo_box pos
        # self.logo_box.setStyleSheet("background-color: red")

        # logo label pic
        self.logo_label = QLabel(self.logo_box)
        self.logo_label.setObjectName("logo_label")
        self.logo_label.setScaledContents(True)
        self.logo_label.setPixmap(QPixmap("./image/gui/logo.png"))
        self.logo_label.resize(150, 75)  # not change
        # self.exit_button.setFixedSize(16, 16)
        self.logo_label.move(
            self.logo_box.width() / 2 - self.logo_label.width() / 2 - 15, 5
        )
        # self.logo_label.setStyleSheet("background-color: blue")

        # connect server widget
        self.connnectsv_box = QWidget(self.background)
        self.connnectsv_box.setObjectName("connnectsv_box")
        self.connnectsv_box.setFixedSize(
            self.width(), self.background.height() - self.logo_box.height()
        )
        self.connnectsv_box.move(0, self.logo_box.height())
        # self.connnectsv_box.setStyleSheet("background-color: blue")

        # info_box widget
        self.info_box = QLabel(self.background)
        self.info_box.setObjectName("info_box")
        self.info_box.setFixedSize(self.background.width() - 40, 300)
        self.info_box.move(20, self.logo_box.y() + self.logo_box.height())
        self.info_box.setStyleSheet("background-color: black")

        #
        self.stt_box = QLabel(self.info_box)
        self.stt_box.setObjectName("info_box")
        self.stt_box.setFixedSize(self.background.width() - 50, 100)
        self.stt_box.move(20, 0)
        self.stt_box.setText(self.status)
        self.stt_box.setStyleSheet("color: #07CAF9")
        #
        self.addr_box = QLabel(self.info_box)
        self.addr_box.setObjectName("info_box")
        self.addr_box.setFixedSize(self.background.width() - 50, 200)
        self.addr_box.move(20, self.stt_box.height())
        # self.addr_box.setStyleSheet("background-color: pink")
        self.addr_box.setStyleSheet("color: #149414")
        self.addr_box.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.addr_box.setText(self.add_list)

        self.update_button = QPushButton(self.background)
        self.update_button.setObjectName("main_button")
        self.update_button.setDefault(True)
        self.update_button.setFixedSize(120, 30)
        self.update_button.move(38, self.info_box.y() + self.info_box.height() + 15)
        self.update_button.setText("Update server")
        self.update_button.setFont(QFont("Arial Bold", 16))
        self.update_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_button_shadow = QGraphicsDropShadowEffect()
        self.update_button_shadow.setBlurRadius(15)
        self.update_button_shadow.setOffset(0)
        self.update_button.setGraphicsEffect(self.update_button_shadow)
        self.update_button.clicked.connect(self.updateNow)

        self.disc_button = QPushButton(self.background)
        self.disc_button.setObjectName("main_button")
        self.disc_button.setDefault(True)
        self.disc_button.setFixedSize(120, 30)
        self.disc_button.move(
            self.update_button.width() + self.update_button.x() + 40,
            self.update_button.y(),
        )
        self.disc_button.setText("Disconnect all")
        self.disc_button.setFont(QFont("Arial Bold", 16))
        self.disc_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.disc_button_shadow = QGraphicsDropShadowEffect()
        self.disc_button_shadow.setBlurRadius(15)
        self.disc_button_shadow.setOffset(0)
        self.disc_button.setGraphicsEffect(self.disc_button_shadow)
        self.disc_button.clicked.connect(self.disc_all)

        self.oldPos = self.pos()

    def updateNow(self):
        sv.SV.updateSV(self.server)

    def disc_all(self):
        sv.SV.disconnect_SV(self.server)
        sv.SV.updateUI(self.server)

    def shutDownSV(self):
        sv.SV.shutdown_SV(self.server)

    def updateUI(self):
        self.stt_box.setText(self.status)
        self.addr_box.setText(self.add_list)

    def checkSD(self):
        return self.checkShutdow

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        # time.sleep(0.02)  # sleep for 20ms
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def closeDialog(self):
        self.close()
        self.shutDownSV()


class getStartUI(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("COVID-19 INFO HCMUS")
        self.resize(400, 550)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(style.css)
        self.background = QWidget(self)
        self.background.setObjectName("background")
        self.background.setGeometry(
            QRect(20, 20, self.width() - 40, self.height() - 40)
        )
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setOffset(0, 0)
        self.shadow.setColor(QColor(0, 0, 0, 180))
        self.background.setGraphicsEffect(self.shadow)

        # self.background.setStyleSheet("background-color: green")

        # titlebar
        self.titlebar = QWidget(self)
        self.titlebar.setObjectName("titlebar")
        self.titlebar.setGeometry(
            QRect(self.background.x(), self.background.y(), self.background.width(), 40)
        )
        self.titlebar_shadow = QGraphicsDropShadowEffect()
        self.titlebar_shadow.setBlurRadius(10)
        self.titlebar_shadow.setOffset(0)
        self.titlebar.setGraphicsEffect(self.titlebar_shadow)
        self.titlebar.setStyleSheet(style.basegui)
        # self.titlebar.setStyleSheet("background-color: green")

        self.exit_button = QPushButton(self.titlebar)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setFixedSize(16, 16)
        self.exit_button.move(17, 12)
        self.exit_button.clicked.connect(self.closeDialog)

        self.minimize_button = QPushButton(self.titlebar)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.setCursor(self.exit_button.cursor())
        self.minimize_button.setFixedSize(16, 16)
        self.minimize_button.move(
            self.exit_button.x() + self.exit_button.width() + 10, self.exit_button.y()
        )
        self.minimize_button.clicked.connect(self.showMinimized)

        self.fullscreen_button = QPushButton(self.titlebar)
        self.fullscreen_button.setObjectName("fullscreen_button")
        self.fullscreen_button.setCursor(self.exit_button.cursor())
        self.fullscreen_button.setFixedSize(16, 16)
        self.fullscreen_button.move(
            self.minimize_button.x() + self.minimize_button.width() + 10,
            self.minimize_button.y(),
        )

        # hcmus logo widget
        self.logo_box = QWidget(self.background)
        self.logo_box.setObjectName("logo_box")
        self.logo_box.setGeometry(QRect(0, self.titlebar.height(), self.width(), 200))

        # to check the logo_box pos
        # self.logo_box.setStyleSheet("background-color: red")

        # logo label pic
        self.logo_label = QLabel(self.logo_box)
        self.logo_label.setObjectName("logo_label")
        self.logo_label.setScaledContents(True)
        self.logo_label.setPixmap(QPixmap("./image/gui/logo.png"))
        self.logo_label.resize(300, 150)  # not change
        # self.exit_button.setFixedSize(16, 16)
        self.logo_label.move(33, 10)

        # connect server widget
        self.connnectsv_box = QWidget(self.background)
        self.connnectsv_box.setObjectName("connnectsv_box")
        self.connnectsv_box.setFixedSize(
            self.width(), self.background.height() - self.logo_box.height()
        )
        self.connnectsv_box.move(0, self.logo_box.height())

        # main label login
        self.main_label = QLabel(self.connnectsv_box)
        self.main_label.setObjectName("main_label")
        self.main_label.setGeometry(QRect(0, 10, self.background.width(), 40))
        self.main_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.main_label.setText("LOGIN SERVER")
        # self.main_label.setStyleSheet("background-color: blue")

        self.inputid = QLineEdit(self.connnectsv_box)
        self.inputid.setMaxLength(22)
        self.inputid.setFocus()
        self.inputid.setFixedSize(250, 40)
        self.inputid.move(
            (self.main_label.width() - self.inputid.width()) / 2,
            self.main_label.y() + 50,
        )
        self.inputid.setPlaceholderText("Username")

        #
        self.inputpw = QLineEdit(self.connnectsv_box)
        self.inputpw.setMaxLength(22)
        self.inputpw.setFixedSize(250, 40)
        self.inputpw.move(self.inputid.x(), self.inputid.y() + 50)
        self.inputpw.setPlaceholderText("Password")
        self.inputpw.setEchoMode(QLineEdit.Password)

        self.connect_button = QPushButton(self.connnectsv_box)
        self.connect_button.setObjectName("main_button")
        self.connect_button.setDefault(True)
        self.connect_button.setFixedSize(150, 30)
        self.connect_button.move(
            (self.main_label.width() - self.connect_button.width()) / 2,
            self.inputpw.y() + self.inputpw.height() + 20,
        )
        self.connect_button.setText("Login")
        self.connect_button.setFont(QFont("Arial Bold", 16))
        self.connect_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.connect_button_shadow = QGraphicsDropShadowEffect()
        self.connect_button_shadow.setBlurRadius(15)
        self.connect_button_shadow.setOffset(0)
        self.connect_button.setGraphicsEffect(self.connect_button_shadow)

        # bam nut connect

        self.connect_button.clicked.connect(self.login)

        # more info
        self.more_info = QPushButton(self.connnectsv_box)
        self.more_info.setObjectName("more_info")
        self.more_info.setFixedSize(200, 25)
        self.more_info.move(
            (self.main_label.width() - self.more_info.width()),
            self.connect_button.y() + 70,
        )
        self.more_info.setText("More infomation 🠚")
        self.more_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.more_info.clicked.connect(self.showInfo)

        self.oldPos = self.pos()
        self.connnectsv_box.raise_()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        # time.sleep(0.02)  # sleep for 20ms
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def closeDialog(self):
        self.close()
        sys.exit()

    def showInfo(self):
        print("info")
        self.message = QMessageBoxX(
            icon="information",
            boldtext="",
            text="IN4 COVID-19 is an application use to tracking Covid-19 infomation in Viet Nam.\nIt's a project in subject Computer network at HCMUS.",
            ok=True,
            cancel=False,
        )
        self.message.exec()

    def login(self):
        try:
            adminDict = open("adminData.json")
            data = json.load(adminDict)
            adminDict.close()
            self.data = data[self.inputid.text()]
            self.password_data = self.data["password"]
            # If password is wrong
            if self.password_data != self.inputpw.text():
                print("wrong")
                self.message = QMessageBoxX(
                    icon="warning",
                    boldtext="Wrong password!",
                    text="Your password seems to be wrong. Please try again!",
                    ok=True,
                    cancel=False,
                )

                self.message.exec()
                self.inputpw.clear()
            # If password is right, then login successfully
            else:
                print("login server ok")
                fullname = self.data["fullname"]
                self.message = QMessageBoxX(
                    icon="information",
                    boldtext="Login successfully",
                    text="You have logged in successfully as {0}".format(fullname),
                    ok=True,
                    cancel=False,
                )
                self.message.exec()
                mainsvui = serverUI()
                mainsvui.show()
                sv.main()
                self.close()

        except KeyError:
            print("not found")
            self.message = QMessageBoxX(
                icon="warning",
                boldtext="ID doesn't exist",
                text="This ID doesn't exist. Please check again!",
                ok=True,
                cancel=False,
            )
            self.message.exec()
            self.inputpw.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("./image/fonts/SanFranciscoDisplay-Regular.otf")
    QFontDatabase.addApplicationFont("./image/fonts/SanFranciscoDisplay-Bold.otf")
    QFontDatabase.addApplicationFont("./image/fonts/SanFranciscoDisplay-Medium.otf")
    QFontDatabase.addApplicationFont("./image/fonts/SanFranciscoDisplay-Thin.otf")

    QFontDatabase.addApplicationFont("./image/fonts/junegull.ttf")
    QFontDatabase.addApplicationFont("./image/fonts/Moose-zp01.ttf")
    QFontDatabase.addApplicationFont("./image/fonts/OpenSans_Condensed-Bold.ttf")
    QFontDatabase.addApplicationFont("./image/fonts/OpenSans.ttf")
    gstart = getStartUI(None)
    gstart.show()
    sys.exit(app.exec())
