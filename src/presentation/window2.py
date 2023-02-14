
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
                               QPushButton, QSizePolicy, QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.CameraLabel = QLabel(self.centralwidget)
        self.CameraLabel.setObjectName(u"CameraLabel")
        self.CameraLabel.setGeometry(QRect(400, 30, 361, 481))
        self.CameraLabel.setStyleSheet(u"border: 2px solid;")
        self.ToggleCameraButton = QPushButton(self.centralwidget)
        self.ToggleCameraButton.setObjectName(u"ToggleCameraButton")
        self.ToggleCameraButton.setGeometry(QRect(50, 40, 281, 181))
        self.Window1Button = QPushButton(self.centralwidget)
        self.Window1Button.setObjectName(u"Window1Button")
        self.Window1Button.setGeometry(QRect(50, 270, 281, 181))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.CameraLabel.setText("")
        self.ToggleCameraButton.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
        self.Window1Button.setText(QCoreApplication.translate("MainWindow", u"Window1", None))
    # retranslateUi

