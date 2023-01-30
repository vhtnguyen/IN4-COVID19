import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import stylesheet as style
from UI import *
import json
import clientSocket as sk
import socket
import ProcDB as pdb
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


# define
Lg = None
clsk = sk.getsock()
ID = ""
IP = ""
APP = None
HUE = ""
SG = ""
HN = ""
TODAY = ""
CHART = ""


class MainUI(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        global ID, IP, clsk, HUE, SG, HN
        self.setWindowTitle("COVID-19 INFO HCMUS")
        self.resize(1000, 650)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(style.basegui)

        self.username = ID
        self.ipaddr = IP
        self.client = clsk
        self.hue = HUE
        self.sg = SG
        self.hn = HN

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
        )  # login input
        self.titlebar_shadow = QGraphicsDropShadowEffect()
        self.titlebar_shadow.setBlurRadius(10)
        self.titlebar_shadow.setOffset(0)
        self.titlebar.setGraphicsEffect(self.titlebar_shadow)
        # self.titlebar.setStyleSheet("background-color: green")

        # server ip tag
        self.svaddrtag = QLabel(self.titlebar)
        self.svaddrtag.setObjectName("svaddrtag")
        self.svaddrtag.setFixedSize(100, 20)
        self.svaddrtag.move(self.titlebar.width() - 160, 12)
        self.svaddrtag.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.svaddrtag.setText(self.ipaddr)
        self.svaddrtag.setStyleSheet(style.css)

        # switch sv button
        self.changesv_button = QPushButton(self.titlebar)
        self.changesv_button.setObjectName("changesv_button")
        self.changesv_button.setFixedSize(25, 22)
        self.changesv_button.move(self.svaddrtag.x() + 100, 11)
        self.changesv_button.setCursor(QCursor(Qt.PointingHandCursor))
        # self.swsv_button.setStyleSheet("background-color: green")
        # self.changesv_button.setStyleSheet(style.css)
        icon = QIcon()
        icon.addPixmap(QPixmap("./image/gui/logout_sv.png"))
        self.changesv_button.setIcon(icon)
        self.changesv_button.setIconSize(QSize(18, 18))

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

        # user icon
        self.user_button = QPushButton(self.titlebar)
        self.user_button.setObjectName("user_button")
        self.user_button.setFixedSize(25, 22)
        self.user_button.move(self.titlebar.width() / 2 - 40, 12)

        self.user_button.setCursor(QCursor(Qt.PointingHandCursor))
        # self.swsv_button.setStyleSheet("background-color: green")
        # self.changesv_button.setStyleSheet(style.css)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("./image/gui/profile_picture.png"))
        self.user_button.setIcon(icon2)
        self.user_button.setIconSize(self.user_button.size())

        # user tag
        self.user_tag = QLabel(self.titlebar)
        # self.user_tag.setObjectName("user_tag")
        self.user_tag.setFixedSize(150, 22)
        self.user_tag.move(self.user_button.x() + 20, 11)
        self.user_tag.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.user_tag.setStyleSheet("font-family: Open Sans SemiCondensed")
        self.user_tag.setText(f"Hello! @{self.username}")
        self.user_tag.setStyleSheet("font-weight: bold")
        # self.user_tag.setStyleSheet(style.css)

        # info_container
        self.main_container = QWidget(self.background)
        self.main_container.setObjectName("messagebox_container")
        self.main_container.setGeometry(
            QRect(
                0,
                self.titlebar.height() - 10,
                350,
                self.background.height() - self.titlebar.height() + 8.5,
            )
        )

        self.main_container.setGraphicsEffect(self.shadow)

        # search box
        self.searchbox = QLineEdit(self.main_container)
        self.searchbox.setObjectName("searchbox")
        self.searchbox.setMaxLength(22)
        self.searchbox.setPlaceholderText("Search...")
        # self.searchbox.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.searchbox.setFixedSize(300, 35)
        self.searchbox.move(20 + 5, 30)
        self.searchbox_shadow = QGraphicsDropShadowEffect()
        self.searchbox_shadow.setBlurRadius(15)
        self.searchbox_shadow.setOffset(0, 1)
        self.searchbox.setGraphicsEffect(self.searchbox_shadow)
        # self.searchbox.textChanged.connect(self.searchContacts)

        # Search Button
        self.search_button = QPushButton(self.main_container)
        self.search_button.setObjectName("search_button")
        self.search_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_button.setGeometry(
            QRect(
                self.searchbox.x() + self.searchbox.width() - 44,
                self.searchbox.y() + 4,
                40,
                28,
            )
        )
        # self.search_button_shadow = QGraphicsDropShadowEffect()
        # self.search_button_shadow.setBlurRadius(10)
        # self.search_button_shadow.setOffset(0, 1)
        # self.search_button.setGraphicsEffect(self.search_button_shadow)
        self.search_button.clicked.connect(self.search)

        # guide line
        self.guide_line = QPushButton(self.main_container)
        self.guide_line.setObjectName("forgotpw-register-login")
        self.guide_line.setFixedSize(200, 20)
        self.guide_line.setCursor(QCursor(Qt.PointingHandCursor))
        self.guide_line.move(self.searchbox.width() / 2 + 10, self.searchbox.y() + 40)
        self.guide_line.setText("search guide →")
        self.guide_line.setStyleSheet(style.css)
        self.guide_line.clicked.connect(self.search_guide)

        # draw horizontal line

        self.product_hline = QLabel(self.background)
        self.product_hline.setFrameShape(QFrame.HLine)
        self.product_hline.setFrameShadow(QFrame.Sunken)
        self.product_hline.move(20, self.searchbox.y() + 90)
        self.product_hline.resize(310, 10)
        self.product_hline_shadow = QGraphicsDropShadowEffect()
        self.product_hline_shadow.setBlurRadius(20)
        self.product_hline_shadow.setOffset(0, 2)
        self.product_hline.setGraphicsEffect(self.product_hline_shadow)

        # result box

        self.result_box = QWidget(self.main_container)
        self.result_box.setObjectName("result_box")
        self.result_box.setGeometry(QRect(25, self.product_hline.y() + 10, 300, 180))
        # 420
        self.result_box_shadow = QGraphicsDropShadowEffect()
        self.result_box_shadow.setBlurRadius(10)
        self.result_box_shadow.setOffset(0, 2)
        self.result_box.setGraphicsEffect(self.product_hline_shadow)

        # intro
        self.result_box_intro = QLabel(self.result_box)
        self.result_box_intro.setObjectName("intro_widget")
        self.result_box_intro.resize(self.result_box.size())
        self.result_box_intro.setText(
            """
            <span style="font-size: 30px; line-height: 30px; font-weight: bold">IN4-COVID19</span><br/>
            <span style="font-size: 20px; line-height: 20px;">The covid-19 tracker</span><br/>
            <span style="font-size: 15px; line-height: 15px;">By Stephen</span><br/>
            <span style="font-size: 12px; line-height: 12px;"><br>From K20 FIT@HCMUS with love ♥</span>
        """
        )
        self.result_box_intro.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)

        #
        self.result_searched = QLabel(self.result_box_intro)
        self.result_searched.setObjectName("result_box")
        self.result_searched.setGeometry(QRect(95, 40, 150, 100))
        self.result_searched.setStyleSheet("background-color: none")
        self.result_searched.setAlignment(Qt.AlignLeft)
        #
        self.today_box = QLabel(self.main_container)
        self.today_box.setObjectName("info_text")
        self.today_box.setGeometry(
            QRect(
                self.result_box.x(),
                self.result_box.y() + self.result_box.height() + 20,
                self.result_box.width(),
                230,
            )
        )
        self.today_box.setStyleSheet("background-color: #F5F5F5")

        # today title
        self.title_today = QLabel(self.today_box)
        self.title_today.setGeometry(
            QRect(
                10,
                15,
                150,
                30,
            )
        )
        self.title_today.setObjectName("info_title")
        self.title_today.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.title_today.setText("VIETNAM TODAY:")

        #
        self.product_hline2 = QLabel(self.today_box)
        self.product_hline2.setFrameShape(QFrame.HLine)
        self.product_hline2.setFrameShadow(QFrame.Sunken)
        self.product_hline2.move(self.title_today.x(), self.title_today.y() + 18)
        self.product_hline2.resize(130, 5)
        self.product_hline_shadow2 = QGraphicsDropShadowEffect()
        self.product_hline_shadow2.setBlurRadius(2)
        self.product_hline_shadow2.setOffset(0, 0)
        self.product_hline2.setGraphicsEffect(self.product_hline_shadow2)
        #

        #
        self.info_today = QLabel(self.today_box)
        self.info_today.setObjectName("info_text")
        self.info_today.setGeometry(QRect(65, self.product_hline2.y() + 10, 170, 170))
        self.info_today.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.info_today.setStyleSheet("font-size: 10pt")
        global TODAY
        self.info_today.setText(TODAY)
        # self.info_today.setStyleSheet("background-color: green")

        # info box

        self.chart_box = QWidget(self.background)
        self.chart_box.setObjectName("info_box")
        self.chart_box.setGeometry(
            QRect(
                self.main_container.width() + 25,
                self.titlebar.height() + 10,
                (self.background.width() - self.main_container.width() - 50),
                320,
            )
        )
        self.chart_box_shadow = QGraphicsDropShadowEffect()
        self.chart_box_shadow.setBlurRadius(10)
        self.chart_box_shadow.setOffset(0, 2)
        self.chart_box.setGraphicsEffect(self.chart_box_shadow)

        # chart box
        self.chart_lb = QLabel(self.chart_box)
        self.chart_lb.setObjectName("chart_container")
        self.chart_lb.setGeometry(QRect(10, 10, (self.chart_box.width() - 20), 300))
        # self.chart_container_shadow = QGraphicsDropShadowEffect()
        # self.chart_container_shadow.setBlurRadius(10)
        # self.chart_container_shadow.setOffset(0,2)
        # self.chart_container.setGraphicsEffect(self.chart_container_shadow)

        # info label

        self.info_lb = QLabel(self.background)
        self.info_lb.setObjectName("info_lb")
        self.info_lb.setGeometry(
            QRect(
                self.chart_box.x(),
                self.chart_box.y() + self.chart_box.height() + 20,
                self.chart_box.width(),
                205,
            )
        )
        # self.info1_box_shadow= QGraphicsDropShadowEffect()
        # self.info1_box_shadow.setBlurRadius(0)
        # self.info1_box_shadow.setOffset(0,1)
        # self.info1_box.setGraphicsEffect(self.info1_box_shadow)
        # print(self.info_box.width(),self.info_box.height())
        # 590 550
        self.info_title = QLabel(self.info_lb)
        self.info_title.setObjectName("info_title")
        self.info_title.setGeometry(QRect(0, 0, self.info_lb.width(), 40))
        self.info_title.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.info_title.setText("LASTEST UPDATED TODAY")
        # 560 205

        # draw horizontal line

        self.product_hline1 = QLabel(self.info_lb)
        self.product_hline1.setFrameShape(QFrame.HLine)
        self.product_hline1.setFrameShadow(QFrame.Sunken)
        self.product_hline1.move(180, self.info_title.y() + 30)
        self.product_hline1.resize(200, 10)
        self.product_hline_shadow1 = QGraphicsDropShadowEffect()
        self.product_hline_shadow1.setBlurRadius(20)
        self.product_hline_shadow1.setOffset(0, 2)
        self.product_hline1.setGraphicsEffect(self.product_hline_shadow1)

        # info 1

        self.info1 = QLabel(self.info_lb)
        self.info1.setObjectName("info_text")
        self.info1.setGeometry(QRect(50, self.info_title.height() + 15, 150, 150))
        self.info1.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.info1.setStyleSheet("font-size: 9pt")
        self.info1.setText(self.hn)

        # info 2
        self.info2 = QLabel(self.info_lb)
        self.info2.setObjectName("info_text")
        self.info2.setGeometry(
            QRect(self.info1.x() + self.info1.width() + 35, self.info1.y(), 150, 150)
        )
        self.info2.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.info2.setStyleSheet("font-size: 9pt")
        self.info2.setText(self.hue)
        # info 3
        self.info3 = QLabel(self.info_lb)
        self.info3.setObjectName("info_text")
        self.info3.setGeometry(
            QRect(self.info_lb.width() - 170 + 10, self.info1.y(), 150, 150)
        )
        self.info3.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.info3.setStyleSheet("font-size: 9pt")
        self.info3.setText(self.sg)
        self.oldPos = self.pos()

    def search_guide(self):
        print("info")
        self.message = QMessageBoxX(
            icon="information",
            boldtext="",
            text="HOW TO FIND YOUR PROVINCE/CITY INFORMATION.\nStep 1: Input your Province/City name in Search box.\nFor example:\nHà Nội→Hà Nội,Ha Noi,hnoi...\nBà Rịa Vũng Tàu→Bà Rịa Vũng Tàu,ba ria vung tau, brvt...\nStep 2: Click search button.\nDone!Now you can see the COVID-19 situation of your Province/City",
            ok=True,
            cancel=False,
        )
        self.message.exec()

    def updateUI(self):
        self.user_tag.setText(f"Hi {self.username} !")

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        # time.sleep(0.02)  # sleep for 20ms
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def closeDialog(self):
        sk.sendDisc(self.client)
        sys.exit()

    def search(self):
        nameprv = self.searchbox.text()
        if nameprv == "":
            self.message = QMessageBoxX(
                icon="warning",
                boldtext="Emty",
                text="Please input your Province/City in search box!",
                ok=True,
                cancel=False,
            )
            self.message.exec()
        else:
            res = sk.search(self.client, nameprv)

            self.result_box_intro.clear()
            self.result_searched.setStyleSheet("font-size: 15pt")
            self.result_searched.setStyleSheet("font-family: Open Sans SemiCondensed")
            self.result_searched.setStyleSheet("color:black")
            self.result_searched.setStyleSheet("font-weight: bold")
            self.result_searched.setText(res)
            self.searchbox.clear()


class LoginUI(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("COVID-19 INFO HCMUS")
        self.resize(1000, 650)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(style.css)
        global clsk
        self.client = clsk
        self.userid = ""
        self.pw = ""

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

        # self.background.setStyleSheet("background-color: red")

        # titlebar
        self.titlebar = QWidget(self)
        self.titlebar.setObjectName("titlebar")
        self.titlebar.setGeometry(
            QRect(self.background.x(), self.background.y(), self.background.width(), 40)
        )  # login input
        self.titlebar_shadow = QGraphicsDropShadowEffect()
        self.titlebar_shadow.setBlurRadius(10)
        self.titlebar_shadow.setOffset(0)
        self.titlebar.setGraphicsEffect(self.titlebar_shadow)
        self.titlebar.setStyleSheet(style.basegui)
        # self.titlebar.setStyleSheet("background-color: green")

        # server ip tag
        self.svaddrtag = QLabel(self.titlebar)
        self.svaddrtag.setObjectName("svaddrtag")
        self.svaddrtag.setFixedSize(100, 20)
        self.svaddrtag.move(self.titlebar.width() - 160, 12)
        self.svaddrtag.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.svaddrtag.setText("192.168.0.1")
        self.svaddrtag.setStyleSheet(style.css)

        # switch sv button
        self.changesv_button = QPushButton(self.titlebar)
        self.changesv_button.setObjectName("changesv_button")
        self.changesv_button.setFixedSize(25, 22)
        self.changesv_button.move(self.svaddrtag.x() + 100, 11)
        self.changesv_button.setCursor(QCursor(Qt.PointingHandCursor))
        # self.swsv_button.setStyleSheet("background-color: green")
        # self.changesv_button.setStyleSheet(style.css)
        icon = QIcon()
        icon.addPixmap(QPixmap("./image/gui/logout_sv.png"))
        self.changesv_button.setIcon(icon)
        self.changesv_button.setIconSize(QSize(18, 18))

        # system button
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
        self.logo_box.setGeometry(QRect(0, self.titlebar.height(), 350, 275))

        # to check the logo_box pos
        # self.logo_box.setStyleSheet("background-color: blue")

        # logo label pic
        self.logo_label = QLabel(self.logo_box)
        self.logo_label.setObjectName("logo_label")
        self.logo_label.setScaledContents(True)
        self.logo_label.setPixmap(QPixmap("./image/gui/logo.png"))
        self.logo_label.resize(300, 150)

        # self.exit_button.setFixedSize(16, 16)
        self.logo_label.move(
            (self.logo_box.width() - self.logo_label.width()) / 2,
            (self.logo_box.height() - self.logo_label.height()) / 2,
        )

        # ads tittle
        self.ads_title = QLabel(self.background)
        self.ads_title.setObjectName("ads_title")
        self.ads_title.setFixedSize(
            self.background.width() - self.logo_box.width() - 80, 40
        )
        self.ads_title.move(self.logo_box.width() + 47, self.titlebar.height() + 18)
        self.ads_title_shadow = QGraphicsDropShadowEffect()
        self.ads_title_shadow.setBlurRadius(10)
        self.ads_title_shadow.setOffset(0)
        self.ads_title.setGraphicsEffect(self.ads_title_shadow)
        self.ads_title.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.ads_title.setText("4 STEPS TO WEAR FACE MARK THE RIGHT WAY.")
        # self.ads_title.setStyleSheet("background-color: purple")

        # login image
        self.product_image = QLabel(self.background)
        self.product_image.setObjectName("product_image")
        self.product_image.setFixedSize(
            self.background.width() - self.logo_box.width() - 80,
            self.background.height() - 140,
        )
        self.product_image.move(self.logo_box.width() + 47, 115)
        self.product_image_shadow = QGraphicsDropShadowEffect()
        self.product_image_shadow.setBlurRadius(10)
        self.product_image_shadow.setOffset(0)
        self.product_image.setGraphicsEffect(self.product_image_shadow)

        # boder vertical line

        self.product_vline = QLabel(self.background)
        self.product_vline.setObjectName("product_vline")
        self.product_vline.setFrameShape(QFrame.VLine)
        self.product_vline.setFrameShadow(QFrame.Sunken)
        self.product_vline.move(350, self.titlebar.height())
        self.product_vline.resize(
            20, self.background.height() - self.titlebar.height() - 15
        )
        self.product_vline_shadow = QGraphicsDropShadowEffect()
        self.product_vline_shadow.setBlurRadius(5)
        self.product_vline_shadow.setOffset(0)
        self.product_vline.setGraphicsEffect(self.product_vline_shadow)

        # Login widget
        self.login_box = QWidget(self.background)
        self.login_box.setObjectName("login_box")
        self.login_box.setFixedSize(
            self.logo_box.width(), self.background.height() - self.logo_box.height()
        )
        self.login_box.move(0, self.logo_box.height() - 30)
        # self.login_box.setStyleSheet("background-color: yellow")

        # main label login
        self.main_label = QLabel(self.login_box)
        self.main_label.setObjectName("main_label")
        self.main_label.setGeometry(QRect(0, 10, self.login_box.width(), 40))
        self.main_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.main_label.setText("W E L C O M E!")
        # self.main_label.setStyleSheet("background-color: pink")

        self.username = QLineEdit(self.login_box)
        self.username.setMaxLength(22)
        self.username.setFocus()
        self.username.setFixedSize(250, 40)
        self.username.move(
            (self.main_label.width() - self.username.width()) / 2,
            self.main_label.y() + 50,
        )
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit(self.login_box)
        self.password.setMaxLength(14)
        self.password.setFixedSize(self.username.size())
        self.password.move(
            self.username.x(), self.username.y() + self.username.height() + 10
        )
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.setStyleSheet(self.username.styleSheet())

        self.login_button = QPushButton(self.login_box)
        self.login_button.setObjectName("main_button")
        self.login_button.setDefault(True)
        self.login_button.setFixedSize(150, 30)
        self.login_button.move(
            (self.main_label.width() - self.login_button.width()) / 2,
            self.password.y() + self.password.height() + 20,
        )
        self.login_button.setText("Login")
        self.login_button.setFont(QFont("Arial Bold", 16))
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_button_shadow = QGraphicsDropShadowEffect()
        self.login_button_shadow.setBlurRadius(15)
        self.login_button_shadow.setOffset(0)
        self.login_button.setGraphicsEffect(self.login_button_shadow)
        self.login_button.clicked.connect(self.login)

        # forgot password ?
        self.forgotpw = QPushButton(self.login_box)
        self.forgotpw.setObjectName("forgotpw-register-login")
        self.forgotpw.setFixedSize(200, 25)
        self.forgotpw.move(
            (self.main_label.width() - self.forgotpw.width()) / 2,
            self.login_button.y() + self.login_button.height() + 25,
        )
        self.forgotpw.setText("Forgot password?")
        self.forgotpw.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgotpw.clicked.connect(self.forgotpwDialog)

        # register new account
        self.register = QPushButton(self.login_box)
        self.register.setObjectName(self.forgotpw.objectName())
        self.register.setFixedSize(200, 25)
        self.register.setCursor(self.forgotpw.cursor())
        self.register.move(
            (self.main_label.width() - self.register.width()) / 2,
            self.forgotpw.y() + self.forgotpw.height() + 7,
        )
        self.register.setText("Create new account")
        self.register.clicked.connect(self.registerDialog)

        # Registering widget
        self.register_box = QWidget(self.background)
        self.register_box.setObjectName("register_box")
        self.register_box.setFixedSize(self.login_box.size())
        # self.register_box.setFixedSize(self.login_box.width(), self.login_box.height())
        self.register_box.move(self.login_box.pos())

        self.register_label = QLabel(self.register_box)
        self.register_label.setObjectName("main_label")
        self.register_label.setAlignment(self.main_label.alignment())
        self.register_label.setFixedSize(self.main_label.size())
        self.register_label.move(self.main_label.pos())
        self.register_label.setText("Register: Step 1")

        self.register_fullname = QLineEdit(self.register_box)
        self.register_fullname.setPlaceholderText("Full Name")
        self.register_fullname.setMaxLength(22)
        self.register_fullname.setGeometry(
            self.username.x(),
            self.username.y(),
            self.username.width(),
            self.username.height(),
        )

        self.register_username = QLineEdit(self.register_box)
        self.register_username.setPlaceholderText("Username")
        self.register_username.setValidator(
            QRegExpValidator(QRegExp("^[a-zA-Z0-9_]{6,14}$"))
        )
        self.register_username.setGeometry(
            self.register_fullname.x(),
            self.register_fullname.y() + self.register_fullname.height() + 10,
            self.register_fullname.width(),
            self.register_fullname.height(),
        )

        self.register_nextstep = QPushButton(self.register_box)
        self.register_nextstep.setObjectName("main_button")
        self.register_nextstep.setCursor(self.login_button.cursor())
        self.register_nextstep.setText("Next step")
        self.register_nextstep.setFixedSize(self.login_button.size())
        self.register_nextstep.move(
            self.login_button.x(),
            self.register_username.y() + self.register_username.height() + 20,
        )
        self.register_ns_shadow = QGraphicsDropShadowEffect()
        self.register_ns_shadow.setBlurRadius(self.login_button_shadow.blurRadius())
        self.register_ns_shadow.setOffset(self.login_button_shadow.offset())
        self.register_nextstep.setGraphicsEffect(self.register_ns_shadow)

        # nhay qua trang tiep theo
        self.register_nextstep.clicked.connect(self.registerNextStep)

        self.register_login_button = QPushButton(self.register_box)
        self.register_login_button.setObjectName(self.forgotpw.objectName())
        self.register_login_button.setCursor(self.forgotpw.cursor())
        self.register_login_button.setText("← Already have an account?")
        self.register_login_button.setFixedSize(200, self.forgotpw.height())
        self.register_login_button.move(
            5, self.login_box.height() - self.register_login_button.height() - 10
        )
        self.register_login_button.clicked.connect(self.loginDialog)

        # Registering widget 2
        self.register_box2 = QWidget(self.background)
        self.register_box2.setObjectName("register_box")
        self.register_box2.setFixedSize(self.login_box.width(), self.login_box.height())
        self.register_box2.move(self.login_box.pos())

        self.register_label2 = QLabel(self.register_box2)
        self.register_label2.setObjectName("main_label")
        self.register_label2.setAlignment(self.main_label.alignment())
        self.register_label2.setFixedSize(self.main_label.size())
        self.register_label2.move(0, 10)
        self.register_label2.setText("Register: Step 2")

        self.register_password = QLineEdit(self.register_box2)
        self.register_password.setPlaceholderText("Password")
        self.register_password.setEchoMode(QLineEdit.Password)
        self.register_password.setValidator(
            QRegExpValidator(QRegExp("^[a-zA-Z0-9_]{6,14}$"))
        )
        self.register_password.setGeometry(
            QRect(
                self.register_fullname.x(),
                self.username.y(),
                self.register_fullname.width(),
                self.register_fullname.height(),
            )
        )

        self.register_password_cf = QLineEdit(self.register_box2)
        self.register_password_cf.setPlaceholderText("Confirm password")
        self.register_password_cf.setEchoMode(QLineEdit.Password)
        self.register_password_cf.setValidator(
            QRegExpValidator(QRegExp("^[a-zA-Z0-9_]{6,14}$"))
        )
        self.register_password_cf.setGeometry(
            QRect(
                self.register_fullname.x(),
                self.register_password.y() + self.register_password.height() + 10,
                self.register_fullname.width(),
                self.register_fullname.height(),
            )
        )

        self.register_pin = QLineEdit(self.register_box2)
        self.register_pin.setPlaceholderText("PIN")
        self.register_pin.setEchoMode(QLineEdit.Password)
        self.register_pin.setValidator(QRegExpValidator(QRegExp("^[0-9]{4,4}$")))
        self.register_pin.setGeometry(
            QRect(
                self.register_fullname.x(),
                self.register_password_cf.y() + self.register_password_cf.height() + 10,
                self.register_fullname.width(),
                self.register_fullname.height(),
            )
        )

        self.register_button = QPushButton(self.register_box2)
        self.register_button.setObjectName("main_button")
        self.register_button.setCursor(self.login_button.cursor())
        self.register_button.setText("Register")
        self.register_button.setFixedSize(self.login_button.size())
        self.register_button.move(
            self.login_button.x(),
            self.register_pin.y() + self.register_pin.height() + 20,
        )
        self.register_btn_shadow = QGraphicsDropShadowEffect()
        self.register_btn_shadow.setBlurRadius(self.login_button_shadow.blurRadius())
        self.register_btn_shadow.setOffset(self.login_button_shadow.offset())
        self.register_button.setGraphicsEffect(self.register_btn_shadow)
        self.register_button.clicked.connect(self.registerFinalStep)

        self.register_login_button2 = QPushButton(self.register_box2)
        self.register_login_button2.setObjectName(self.forgotpw.objectName())
        self.register_login_button2.setCursor(self.forgotpw.cursor())
        self.register_login_button2.setText("← Already have an account?")
        self.register_login_button2.setFixedHeight(self.forgotpw.height())
        self.register_login_button2.move(
            15, self.login_box.height() - self.register_login_button.height() - 10
        )
        self.register_login_button2.clicked.connect(self.loginDialog)

        self.register_backstep = QPushButton(self.register_box2)
        self.register_backstep.setObjectName(self.forgotpw.objectName())
        self.register_backstep.setCursor(self.forgotpw.cursor())
        self.register_backstep.setText("← Back to step 1")
        self.register_backstep.setFixedHeight(self.forgotpw.height())
        self.register_backstep.move(
            self.register_login_button2.x(),
            self.register_login_button2.y() - self.register_backstep.height(),
        )
        self.register_backstep.clicked.connect(self.backStep)

        # Forgot password widget
        self.forgotpw_box = QWidget(self.background)
        self.forgotpw_box.setObjectName("forgotpw_box")
        self.forgotpw_box.setFixedSize(self.login_box.size())
        self.forgotpw_box.move(self.login_box.pos())

        self.forgotpw_label = QLabel(self.forgotpw_box)
        self.forgotpw_label.setObjectName("main_label")
        self.forgotpw_label.setAlignment(self.main_label.alignment())
        self.forgotpw_label.setFixedSize(self.main_label.size())
        self.forgotpw_label.move(0, 10)
        self.forgotpw_label.setText("Reset password")

        self.forgotpw_username = QLineEdit(self.forgotpw_box)
        self.forgotpw_username.setPlaceholderText("Username")
        self.forgotpw_username.setGeometry(
            QRect(
                self.username.x(),
                self.forgotpw_label.y() + self.forgotpw_label.height() + 10,
                self.username.width(),
                self.username.height(),
            )
        )
        self.forgotpw_username.setValidator(
            QRegExpValidator(QRegExp("^[a-zA-Z0-9_]{6,14}$"))
        )

        self.forgotpw_pin = QLineEdit(self.forgotpw_box)
        self.forgotpw_pin.setPlaceholderText("PIN")
        self.forgotpw_pin.setEchoMode(QLineEdit.Password)
        self.forgotpw_pin.setGeometry(
            QRect(
                self.username.x(),
                self.forgotpw_username.y() + self.forgotpw_username.height() + 10,
                self.username.width(),
                self.username.height(),
            )
        )
        self.forgotpw_pin.setValidator(QRegExpValidator(QRegExp("^[0-9_]{4,4}$")))

        self.forgotpw_newpw = QLineEdit(self.forgotpw_box)
        self.forgotpw_newpw.setPlaceholderText("New password")
        self.forgotpw_newpw.setEchoMode(QLineEdit.Password)
        self.forgotpw_newpw.setFixedSize(self.forgotpw_username.size())
        self.forgotpw_newpw.move(
            self.forgotpw_username.x(),
            self.forgotpw_pin.y() + self.forgotpw_pin.height() + 10,
        )
        self.forgotpw_newpw.setValidator(
            QRegExpValidator(QRegExp("^[a-zA-Z0-9_]{6,14}$"))
        )

        self.forgotpw_newpw_cf = QLineEdit(self.forgotpw_box)
        self.forgotpw_newpw_cf.setPlaceholderText("Confirm password")
        self.forgotpw_newpw_cf.setEchoMode(QLineEdit.Password)
        self.forgotpw_newpw_cf.setFixedSize(self.forgotpw_username.size())
        self.forgotpw_newpw_cf.move(
            self.username.x(),
            self.forgotpw_newpw.y() + self.forgotpw_newpw.height() + 10,
        )
        self.forgotpw_newpw_cf.setValidator(
            QRegExpValidator(QRegExp("^[a-zA-Z0-9_]{6,14}$"))
        )

        self.forgotpw_reset = QPushButton(self.forgotpw_box)
        self.forgotpw_reset.setObjectName("main_button")
        self.forgotpw_reset.setCursor(self.login_button.cursor())
        self.forgotpw_reset.setText("Reset")
        self.forgotpw_reset.setFixedSize(self.login_button.size())
        self.forgotpw_reset.move(
            self.login_button.x(),
            self.forgotpw_newpw_cf.y() + self.forgotpw_newpw_cf.height() + 20,
        )
        self.forgotpw_reset_shadow = QGraphicsDropShadowEffect()
        self.forgotpw_reset_shadow.setBlurRadius(self.login_button_shadow.blurRadius())
        self.forgotpw_reset_shadow.setOffset(self.login_button_shadow.offset())
        self.forgotpw_reset.setGraphicsEffect(self.forgotpw_reset_shadow)
        self.forgotpw_reset.clicked.connect(self.forgetPassword)

        self.forgotpw_login = QPushButton(self.forgotpw_box)
        self.forgotpw_login.setObjectName("forgotpw-register-login")
        self.forgotpw_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgotpw_login.setText("← Login")
        self.forgotpw_login.setFixedSize(90, self.forgotpw.height())
        self.forgotpw_login.move(
            5, self.login_box.height() - self.register_login_button.height() - 10
        )
        self.forgotpw_login.clicked.connect(self.loginDialog)

        self.oldPos = self.pos()
        self.login_box.raise_()
        self.product_image.raise_()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        # time.sleep(0.02)  # sleep for 20ms
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def closeDialog(self):
        sk.sendDisc(self.client)
        sys.exit()

    def loginDialog(self):
        self.login_button.setDefault(True)
        self.register_button.setDefault(False)
        self.forgotpw_reset.setDefault(False)
        self.register_fullname.clear()
        self.register_username.clear()
        self.register_password.clear()
        self.register_pin.clear()
        self.forgotpw_username.clear()
        self.forgotpw_newpw.clear()
        self.forgotpw_newpw_cf.clear()
        self.forgotpw_pin.clear()
        self.login_box.raise_()
        self.product_image.raise_()

    def registerDialog(self):
        self.login_button.setDefault(False)
        self.register_button.setDefault(True)
        self.forgotpw_reset.setDefault(False)
        self.username.clear()
        self.password.clear()
        self.forgotpw_username.clear()
        self.forgotpw_newpw.clear()
        self.forgotpw_newpw_cf.clear()
        self.forgotpw_pin.clear()
        self.register_box.raise_()
        self.product_image.raise_()

    def forgotpwDialog(self):
        self.login_button.setDefault(False)
        self.register_button.setDefault(False)
        self.forgotpw_reset.setDefault(True)
        self.username.clear()
        self.password.clear()
        self.register_username.clear()
        self.register_password.clear()
        self.register_password_cf.clear()
        self.register_pin.clear()
        self.forgotpw_box.raise_()
        self.product_image.raise_()

    def backStep(self):
        self.register_box.raise_()
        self.product_image.raise_()

    def login(self):
        self.userid = self.username.text()
        self.pw = self.password.text()
        userid = self.userid
        pw = self.pw
        print(f"{self.userid} request login")
        sk.send_msg(self.client, "login")
        sk.recv_msg(self.client)
        sk.send_msg(self.client, userid)
        sk.recv_msg(self.client)
        sk.send_msg(self.client, pw)
        sk.recv_msg(self.client)
        result = sk.recv_msg(self.client)
        sk.send_msg(self.client, "ok")
        print(result)
        if result == "wrong pw":
            print("wrong")
            self.message = QMessageBoxX(
                icon="warning",
                boldtext="Wrong password!",
                text="Your password seems to be wrong. Please try again!",
                ok=True,
                cancel=False,
            )
            self.message.exec()
            self.password.clear()
        # If password is right, then login successfully
        elif result == "login ok":
            print("login successfully")
            global ID, HUE, SG, HN, CHART, TODAY
            ID = self.userid
            HUE = sk.hue(self.client)
            SG = sk.saigon(self.client)
            HN = sk.hanoi(self.client)
            CHART = sk.get7days(self.client)
            TODAY = sk.getToday(self.client)
            pdb.draw7daysChart(CHART)
            self.message = QMessageBoxX(
                icon="information",
                boldtext="Login successfully",
                text="You have logged in successfully as @{0}".format(self.userid),
                ok=True,
                cancel=False,
            )
            self.message.exec()
            global APP
            APP = MainUI()
            APP.show()
            self.close()
        elif result == "user not found":
            print("not found")
            self.message = QMessageBoxX(
                icon="warning",
                boldtext="User doesn't exist",
                text="This username doesn't exist. Please check again!",
                ok=True,
                cancel=False,
            )
            self.message.exec()
            self.password.clear()

    def registerNextStep(self):
        if len(self.register_fullname.text()) < 4:
            warning = QMessageBoxX(
                icon="warning",
                boldtext="Too short full name",
                text="Full name must contain at least 4 characters.",
            )
            warning.exec()
        elif len(self.register_username.text()) < 6:
            warning = QMessageBoxX(
                icon="warning",
                boldtext="Too short username",
                text="Username must contain at least 6 characters.",
            )
            warning.exec()
        else:
            sk.send_msg(self.client, "signup")
            sk.recv_msg(self.client)
            sk.send_msg(self.client, self.register_fullname.text())
            sk.recv_msg(self.client)
            sk.send_msg(self.client, self.register_username.text())
            sk.recv_msg(self.client)
            self.register_box2.raise_()
            self.product_image.raise_()

    def registerFinalStep(self, result):
        if len(self.register_password.text()) < 6:
            warning = QMessageBoxX(
                icon="warning",
                boldtext="Too short password",
                text="Password must contain at least 6 characters.",
            )
            warning.exec()
        elif self.register_password_cf.text() != self.register_password.text():
            warning = QMessageBoxX(
                icon="warning",
                boldtext="Wrong confirmation password",
                text="The confirmation password you have entered is wrong. Please check again.",
            )
        elif len(self.register_pin.text()) < 4:
            warning = QMessageBoxX(
                icon="warning",
                boldtext=" Too short PIN",
                text="PIN must contain at least 4 numbers",
            )
            warning.exec()
        else:
            sk.send_msg(self.client, self.register_password.text())
            sk.recv_msg(self.client)

            sk.send_msg(self.client, self.register_pin.text())
            sk.recv_msg(self.client)

            sk.send_msg(self.client, "ok")
            result = sk.recv_msg(self.client)
            # input ok
            if result == "username exist":
                self.register_fullname.clear()
                self.register_username.clear()
                self.register_password.clear()
                self.register_password_cf.clear()
                self.register_pin.clear()
                self.warning = QMessageBoxX(
                    icon="warning",
                    boldtext="Existed username",
                    text="This username has been used. Please choose another username.",
                )
                self.warning.exec()
            # If inputed username doesn't exist, write all registered data
            elif result == "usename accept":
                # send register to sv
                self.information = QMessageBoxX(
                    icon="information",
                    boldtext="Registered successfully",
                    text="Your account [{0}] has been created successfully!".format(
                        self.register_username.text()
                    ),
                )
                self.information.exec()
                self.loginDialog()

    def forgetPassword(self):
        newpw = self.forgotpw_newpw.text()
        newpwcf = self.forgotpw_newpw_cf.text()
        if newpw != newpwcf:
            self.warning = QMessageBoxX(
                icon="warning",
                boldtext="Wrong confirm password",
                text="Confirm password is incorrect. Please check again.",
            )
            self.forgotpw_newpw.clear()
            self.forgotpw_newpw_cf.clear()
            self.warning.exec()
        else:
            sk.send_msg(self.client, "forgot password")
            sk.recv_msg(self.client)
            sk.send_msg(self.client, self.forgotpw_username.text())
            sk.recv_msg(self.client)
            sk.send_msg(self.client, self.forgotpw_pin.text())
            sk.recv_msg(self.client)
            sk.send_msg(self.client, newpw)
            sk.recv_msg(self.client)
            sk.send_msg(self.client, "ok")
            result = sk.recv_msg(self.client)
            if result == "password changed":
                self.information = QMessageBoxX(
                    icon="information",
                    boldtext="Password was changed ",
                    text="Your account password @{0} has been changed successfully!".format(
                        self.forgotpw_username.text()
                    ),
                )
                self.forgotpw_username.clear()
                self.forgotpw_pin.clear()
                self.forgotpw_newpw.clear()
                self.forgotpw_newpw_cf.clear()
                self.information.exec()
                self.loginDialog()
            elif result == "incorrect":
                self.warning = QMessageBoxX(
                    icon="warning",
                    boldtext="Wrong PIN",
                    text="This PIN is incorrect. Please check again.",
                )
                self.forgotpw_pin.clear()
                self.warning.exec()
            elif result == "user not exist":
                self.warning = QMessageBoxX(
                    icon="warning",
                    boldtext="Not existed username",
                    text="This username hasn't existed.",
                )
                self.forgotpw_username.clear()
                self.forgotpw_pin.clear()
                self.forgotpw_newpw.clear()
                self.forgotpw_newpw_cf.clear()
                self.warning.exec()
                self.forgotpwDialog()


class getStartUI(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        global clsk
        self.setWindowTitle("COVID-19 INFO HCMUS")
        self.resize(400, 550)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(style.css)
        self.hostip = ""
        self.client = clsk
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
        # self.connnectsv_box.setStyleSheet("background-color: blue")

        # # Login widget
        # self.login_box = QWidget(self.background)
        # self.login_box.setObjectName("login_box")
        # self.login_box.setFixedSize(self.logo_box.width(),self.background.height()-self.logo_box.height())
        # self.login_box.move(0,self.logo_box.height()-30)
        # #self.login_box.setStyleSheet("background-color: blue")

        # main label login
        self.main_label = QLabel(self.connnectsv_box)
        self.main_label.setObjectName("main_label")
        self.main_label.setGeometry(QRect(0, 10, self.background.width(), 40))
        self.main_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.main_label.setText("CONNECT TO SERVER")
        # self.main_label.setStyleSheet("background-color: blue")

        self.inputip = QLineEdit(self.connnectsv_box)
        self.inputip.setMaxLength(22)
        self.inputip.setFocus()
        self.inputip.setFixedSize(250, 40)
        self.inputip.move(
            (self.main_label.width() - self.inputip.width()) / 2,
            self.main_label.y() + 50,
        )
        self.inputip.setPlaceholderText("IP host server")

        self.connect_button = QPushButton(self.connnectsv_box)
        self.connect_button.setObjectName("main_button1")
        self.connect_button.setDefault(True)
        self.connect_button.setFixedSize(150, 30)
        self.connect_button.move(
            (self.main_label.width() - self.connect_button.width()) / 2,
            self.inputip.y() + self.inputip.height() + 20,
        )
        self.connect_button.setText("Connect")
        self.connect_button.setFont(QFont("Arial Bold", 16))
        self.connect_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.connect_button_shadow = QGraphicsDropShadowEffect()
        self.connect_button_shadow.setBlurRadius(15)
        self.connect_button_shadow.setOffset(0)
        self.connect_button.setGraphicsEffect(self.connect_button_shadow)

        # bam nut connect

        self.connect_button.clicked.connect(self.connect)

        # more info
        self.more_info = QPushButton(self.connnectsv_box)
        self.more_info.setObjectName("more_info")
        self.more_info.setFixedSize(200, 25)
        self.more_info.move(
            (self.main_label.width() - self.more_info.width()),
            self.connect_button.y() + 110,
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
        sk.send_msg(self.client, "logout")
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

    def connect(self):
        try:
            addr = self.inputip.text().split(":")
            self.hostip = addr[0]
            if len(addr) == 2:
                self.port = int(addr[1])
            else:
                self.port = 8888
            self.addr = (self.hostip, self.port)
            global clsk
            if sk.client_conn(clsk, self.addr):
                print("connect successfully")
                self.message = QMessageBoxX(
                    icon="information",
                    boldtext="Connect successfully",
                    text=f"You have connected to host server at IP address: {self.hostip} PORT: {self.port}",
                    ok=True,
                    cancel=False,
                )
                self.message.exec()
                global Lg, IP
                IP = self.hostip
                Lg = LoginUI()
                Lg.show()
                self.close()
            else:
                print("can't connect")
                self.message = QMessageBoxX(
                    icon="warning",
                    boldtext="Connect fail!",
                    text=f"Can not connect to server at IP address: {self.hostip} PORT: {self.port}",
                    ok=True,
                    cancel=False,
                )
                self.message.exec()
                self.inputip.clear()
        except:
            print("can't connect")
            self.message = QMessageBoxX(
                icon="warning",
                boldtext="Connect fail!",
                text=f"Can not connect to server at IP address: {self.hostip} PORT: {self.port}",
                ok=True,
                cancel=False,
            )
            self.message.exec()
            self.inputip.clear()


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

    gstart = getStartUI()
    gstart.show()
    sys.exit(app.exec())
