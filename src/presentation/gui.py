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

import src.presentation.resources


class Ui_MainWindow(object):
    
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
        self.StartButton = QPushButton(self.centralwidget)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(540, 370, 231, 51))
        self.StopNumberButton = QPushButton(self.centralwidget)
        self.StopNumberButton.setObjectName(u"StopNumberButton")
        self.StopNumberButton.setGeometry(QRect(540, 480, 231, 51))
        self.StopCameraButton = QPushButton(self.centralwidget)
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
