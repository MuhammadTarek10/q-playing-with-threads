import numpy
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow

from src.presentation.window1 import Ui_MainWindow as Window1
from src.presentation.window2 import Ui_MainWindow as Window2
from src.utils.camera_thread import Camera
from src.utils.number_thread import Number
from src.utils.thread_handler import ThreadHandler


class Window1App(QMainWindow, Window1):
    def __init__(self):
        super().__init__()
        self.camera = Camera()
        self.number = Number()
        self.threadHandler = ThreadHandler([self.camera, self.number])
        self.threadHandler.connect(self.camera.frame, self.updateFrame)
        self.threadHandler.connect(self.number.value, self.updateNumber)
        self.setupUi(self)
        self.StartButton.clicked.connect(self.start)
        self.StopCameraButton.clicked.connect(lambda: self.stop(0))
        self.StopNumberButton.clicked.connect(lambda: self.stop(1))
        self.Window2Button.clicked.connect(lambda: self.moveToWindow2())
        self.show()

    def updateFrame(self, frame: numpy.ndarray):
        frame = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        frame = frame.scaled(self.CameraLabel.size(), Qt.KeepAspectRatio)
        self.CameraLabel.setPixmap(QPixmap.fromImage(frame))

    def updateNumber(self, number: int):
        self.NumberLabel.setText(str(number))

    def start(self):
        self.threadHandler.startAll()

    def stop(self, thread: int):
        self.threadHandler.stop(thread)

    def moveToWindow2(self):
        self.threadHandler.stopAll()
        self.window2 = Window2App()
        self.window2.show()
        self.close()


class Window2App(QMainWindow, Window2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.camera = Camera()
        self.threadHandler = ThreadHandler([self.camera])
        self.cameraRunning = False;
        self.threadHandler.connect(self.camera.frame, self.updateFrame)
        self.ToggleCameraButton.clicked.connect(lambda: self.toggle())
        self.Window1Button.clicked.connect(lambda: self.moveToWindow1())
        self.show()

    def toggle(self):
        if self.cameraRunning:
            self.threadHandler.stopAll()
            self.cameraRunning = False
        else:
            self.threadHandler.startAll()
            self.cameraRunning = True

    def updateFrame(self, frame: numpy.ndarray):
        frame = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        frame = frame.scaled(self.CameraLabel.size(), Qt.KeepAspectRatio)
        self.CameraLabel.setPixmap(QPixmap.fromImage(frame))

    def moveToWindow1(self):
        self.threadHandler.stopAll()
        self.window1 = Window1App()
        self.window1.show()
        self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window1App()
    sys.exit(app.exec())