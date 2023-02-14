# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import numpy
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QWidget)

import resources
from utils.camera_thread import Camera
from utils.number_thread import Number
from utils.thread_handler import ThreadHandler


class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.camera = Camera()
        self.number = Number()
        self.thread_handler = ThreadHandler([self.camera, self.number])
        self.thread_handler.connect(self.camera.frame, self.updateFrame)
        self.thread_handler.connect(self.number.value, self.updateNumber)

    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.NumberLabel = QLabel(self.centralwidget)
        self.NumberLabel.setObjectName(u"NumberLabel")
        self.NumberLabel.setGeometry(QRect(570, 270, 181, 111))
        font = QFont()
        font.setPointSize(36)
        self.NumberLabel.setFont(font)
        self.NumberLabel.setAlignment(Qt.AlignCenter)
        self.CameraLabel = QLabel(self.centralwidget)
        self.CameraLabel.setObjectName(u"CameraLabel")
        self.CameraLabel.setGeometry(QRect(10, 10, 471, 511))
        self.CameraLabel.setStyleSheet(u"border: 2px solid black;")
        self.ImageLabel = QLabel(self.centralwidget)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setGeometry(QRect(540, 40, 221, 161))
        self.ImageLabel.setPixmap(QPixmap(u":/images/car.jpeg"))
        self.ImageLabel.setScaledContents(True)
        self.StartButton = QPushButton(self.centralwidget, clicked=self.start)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(540, 370, 231, 51))
        self.StopNumberButton = QPushButton(self.centralwidget, clicked=lambda: self.stop(1))
        self.StopNumberButton.setObjectName(u"StopNumberButton")
        self.StopNumberButton.setGeometry(QRect(540, 480, 231, 51))
        self.StopCameraButton = QPushButton(self.centralwidget, clicked=lambda: self.stop(0))
        self.StopCameraButton.setObjectName(u"StopCameraButton")
        self.StopCameraButton.setGeometry(QRect(540, 420, 231, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def updateFrame(self, frame: numpy.ndarray):
        frame = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        frame = frame.scaled(self.CameraLabel.size(), Qt.KeepAspectRatio)
        self.CameraLabel.setPixmap(QPixmap.fromImage(frame))

    def updateNumber(self, number: int):
        self.NumberLabel.setText(str(number))

    def start(self):
        self.thread_handler.start()

    def stop(self, thread: int):
        self.thread_handler.stop(thread)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.NumberLabel.setText(QCoreApplication.translate("MainWindow", u"Number", None))
        self.CameraLabel.setText("")
        self.ImageLabel.setText("")
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Start All", None))
        self.StopNumberButton.setText(QCoreApplication.translate("MainWindow", u"Stop Number", None))
        self.StopCameraButton.setText(QCoreApplication.translate("MainWindow", u"Stop Camera", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
