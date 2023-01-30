import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import stylesheet as style
import time
from PIL import Image


class QMessageBoxX(QDialog):
    def __init__(
        self,
        icon=None,
        boldtext="",
        text="",
        ok=True,
        oktext="OK",
        cancel=False,
        canceltext="Cancel",
        stylesheet=style.basegui,
    ):
        super().__init__()
        # Setting Translucent and Frameless Window
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet(stylesheet)
        self.oldPos = self.pos()
        self.oldX = self.x()
        self.oldY = self.y()
        # Create screen resolution object
        # self.wx = App(False)
        # self.screenres = GetDisplaySize()

        self.iconType = icon
        # Setting Custom Background, Window Border and Shadow
        self.container = QWidget(self)
        self.container.setObjectName("messagebox_container")
        self.container.move(20, 20)
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setOffset(0, 0)
        self.shadow.setColor(QColor(0, 0, 0, 180))
        self.container.setGraphicsEffect(self.shadow)

        # Setting Font Family and Font Size
        self.font = QFont("Helvetica Neue", 14)
        self.font.setStyleStrategy(QFont.PreferAntialias)
        self.setFont(QFont(self.font))

        # Custom Title Bar
        self.titlebar = QLabel(self.container)
        self.titlebar.setObjectName("titlebar")
        self.titlebar.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.titlebar.move(0, 0)

        # Exit Button
        self.exit_button = QPushButton(self.titlebar)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setFixedSize(14, 14)
        self.exit_button.move(12, 8)
        self.exit_button.clicked.connect(self.close)

        # Minimize Button
        self.minimize_button = QPushButton(self.titlebar)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.setCursor(self.exit_button.cursor())
        self.minimize_button.setDisabled(True)
        self.minimize_button.setFixedSize(
            self.exit_button.width(), self.exit_button.height()
        )
        self.minimize_button.move(
            self.exit_button.x() + self.exit_button.width() + 10, self.exit_button.y()
        )
        self.minimize_button.clicked.connect(self.showMinimized)

        # Fullscreen Button
        self.fullscreen_button = QPushButton(self.titlebar)
        self.fullscreen_button.setDisabled(True)
        self.fullscreen_button.setObjectName("fullscreen_button")
        self.fullscreen_button.setCursor(self.exit_button.cursor())
        self.fullscreen_button.setFixedSize(
            self.exit_button.width(), self.exit_button.height()
        )
        self.fullscreen_button.move(
            self.minimize_button.x() + self.minimize_button.width() + 10,
            self.minimize_button.y(),
        )

        self.icon = QLabel(self.container)
        self.icon.move(30, self.titlebar.height() + 20)
        if self.iconType and self.iconType != "input":
            self.icon.setFixedSize(50, 50)
            if self.iconType == "warning":
                self.icon_pixmap = QPixmap("./image/gui/warning.png")
                self.icon_pixmap_scaled = self.icon_pixmap.scaled(
                    self.icon.width(),
                    self.icon.height(),
                    aspectRatioMode=Qt.IgnoreAspectRatio,
                    transformMode=Qt.SmoothTransformation,
                )
                self.icon.setPixmap(self.icon_pixmap_scaled)
            elif self.iconType == "information":
                self.icon_pixmap = QPixmap("./image/gui/information.png")
                self.icon_pixmap_scaled = self.icon_pixmap.scaled(
                    self.icon.width(),
                    self.icon.height(),
                    aspectRatioMode=Qt.IgnoreAspectRatio,
                    transformMode=Qt.SmoothTransformation,
                )
                self.icon.setPixmap(self.icon_pixmap_scaled)

            elif self.iconType == "question":
                self.icon_pixmap = QPixmap("./image/gui/question.png")
                self.icon_pixmap_scaled = self.icon_pixmap.scaled(
                    self.icon.width(),
                    self.icon.height(),
                    aspectRatioMode=Qt.IgnoreAspectRatio,
                    transformMode=Qt.SmoothTransformation,
                )
                self.icon.setPixmap(self.icon_pixmap_scaled)
                self.sd = QGraphicsDropShadowEffect()
                self.sd.setBlurRadius(15)
                self.sd.setOffset(0)
                self.icon.setGraphicsEffect(self.sd)
        else:
            self.icon.setFixedSize(0, 0)

        self.boldtext = QLabel(self.container)
        self.boldtext.setObjectName("messagebox_boldtext")
        self.boldtext.setFixedHeight(25)
        self.boldtext.move(self.icon.x() + self.icon.width() + 20, self.icon.y())
        self.boldtext.setText(boldtext)

        self.text = QLabel(self.container)
        self.text.setMaximumWidth(1200)
        self.text.setWordWrap(False)
        self.text.move(self.boldtext.x(), self.boldtext.y() + self.boldtext.height())
        self.text.setText(text)
        self.text.adjustSize()

        self.textbox = QLineEdit(self.container)
        self.textbox.setObjectName("messagebox_textbox")
        if self.iconType == "input":
            self.textbox.setFixedSize(200, 25)
            self.textbox.setVisible(True)
        else:
            self.textbox.setVisible(False)
            self.textbox.setFixedSize(0, 0)
        self.textbox.move(self.boldtext.x(), self.text.y() + self.text.height() + 10)

        self.cancel = QPushButton(self.container)
        self.cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel.setText(canceltext)
        self.cancel.clicked.connect(self.cancelButton)

        self.ok = QPushButton(self.container)
        self.ok.setObjectName("blue_button")
        self.ok.setCursor(self.cancel.cursor())
        self.ok.setVisible(ok)
        self.ok.setFixedSize(90, 20)
        self.ok.setText(oktext)
        self.ok.clicked.connect(self.okButton)

        self.container.setFixedWidth(
            max(
                self.boldtext.x() + self.boldtext.width() + self.icon.x(),
                self.text.x() + self.text.width() + self.icon.x(),
                self.textbox.x() + self.textbox.width() + self.icon.x(),
            )
        )
        self.titlebar.setFixedSize(self.container.width(), 30)
        if cancel:
            self.cancel.setFixedSize(90, 20)
            self.cancel.move(
                self.container.width() - self.cancel.width() - 30,
                self.textbox.y() + self.textbox.height() + 20,
            )
        else:
            self.cancel.setFixedSize(0, 20)
            self.cancel.move(
                self.container.width() - self.cancel.width() - 20,
                self.textbox.y() + self.textbox.height() + 20,
            )
        self.ok.move(self.cancel.x() - self.ok.width() - 5, self.cancel.y())
        self.container.setFixedHeight(self.ok.y() + self.ok.height() + 15)
        self.setFixedSize(self.container.width() + 40, self.container.height() + 40)

        self.effect = QGraphicsOpacityEffect(self)
        self.showAnimation = QPropertyAnimation(self.effect, b"opacity")
        self.showAnimation.setDuration(200)
        self.showAnimation.setStartValue(0)
        self.showAnimation.setEndValue(1)
        self.setGraphicsEffect(self.effect)
        self.showAnimation.start(QAbstractAnimation.DeleteWhenStopped)
        self.showAnimation.finished.connect(self.effect.deleteLater)

    def setupTextbox(self, placeholder="", text="", maxlength=None):
        self.textbox.setText(text)
        self.textbox.setPlaceholderText(placeholder)
        if maxlength:
            self.textbox.setMaxLength(maxlength)

    def getText(self):
        return self.textbox.text()

    def okButton(self):
        return self.done(1)

    def cancelButton(self):
        return self.done(0)


class QDialogX(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        # Setting Translucent and Frameless Window
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.oldPos = self.pos()
        self.oldX = self.x()
        self.oldY = self.y()

        # Setting Custom Background, Window Border and Shadow
        self.container = QWidget(self)
        self.container.setObjectName("container")
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setOffset(0, 0)
        self.shadow.setColor(QColor(0, 0, 0, 180))
        self.container.setGraphicsEffect(self.shadow)

        # Custom Title Bar
        self.titlebar = QLabel(self.container)
        self.titlebar.setObjectName("titlebar")
        self.titlebar.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.titlebar.setFixedSize(self.container.width(), 30)
        self.titlebar.move(0, 0)

        # Exit Button
        self.exit_button = QPushButton(self.titlebar)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setFixedSize(14, 14)
        self.exit_button.move(12, 8)
        self.exit_button.clicked.connect(self.close)

        # Minimize Button
        self.minimize_button = QPushButton(self.titlebar)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.setCursor(self.exit_button.cursor())
        self.minimize_button.setDisabled(True)
        self.minimize_button.setFixedSize(
            self.exit_button.width(), self.exit_button.height()
        )
        self.minimize_button.move(
            self.exit_button.x() + self.exit_button.width() + 10, self.exit_button.y()
        )
        self.minimize_button.clicked.connect(self.showMinimized)

        # Fullscreen Button
        self.fullscreen_button = QPushButton(self.titlebar)
        self.fullscreen_button.setDisabled(True)
        self.fullscreen_button.setObjectName("fullscreen_button")
        self.fullscreen_button.setCursor(self.exit_button.cursor())
        self.fullscreen_button.setFixedSize(
            self.exit_button.width(), self.exit_button.height()
        )
        self.fullscreen_button.move(
            self.minimize_button.x() + self.minimize_button.width() + 10,
            self.minimize_button.y(),
        )

    # Mouse Press Event
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        self.oldX = event.globalX()
        self.oldY = event.globalY()

    # Custom Window Moving Event
    def mouseMoveEvent(self, event):
        # time.sleep(0.02)  # sleep for 20ms
        delta = QPoint(event.globalPos() - self.oldPos)
        if (
            self.oldX >= self.x() + self.container.x() + self.titlebar.x()
            and self.oldX
            <= self.x() + self.container.x() + self.titlebar.x() + self.titlebar.width()
            and self.oldY >= self.y() + self.container.y() + self.titlebar.y()
            and self.oldY
            <= self.y()
            + self.container.y()
            + self.titlebar.y()
            + self.titlebar.height()
        ):
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
            self.oldX = event.globalX()
            self.oldY = event.globalY()
