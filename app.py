import numpy
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow

from src.presentation.gui import Ui_MainWindow
from src.utils.camera_thread import Camera
from src.utils.number_thread import Number
from src.utils.thread_handler import ThreadHandler


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.camera = Camera()
        self.number = Number()
        self.thread_handler = ThreadHandler([self.camera, self.number])
        self.thread_handler.connect(self.camera.frame, self.updateFrame)
        self.thread_handler.connect(self.number.value, self.updateNumber)
        super().__init__()
        self.setupUi(self)
        self.StartButton.clicked.connect(self.start)
        self.StopCameraButton.clicked.connect(lambda: self.stop(0))
        self.StopNumberButton.clicked.connect(lambda: self.stop(1))
        self.show()

    def updateFrame(self, frame: numpy.ndarray):
        frame = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        frame = frame.scaled(self.CameraLabel.size(), Qt.KeepAspectRatio)
        self.CameraLabel.setPixmap(QPixmap.fromImage(frame))

    def updateNumber(self, number: int):
        self.NumberLabel.setText(str(number))

    def start(self):
        self.thread_handler.startAll()

    def stop(self, thread: int):
        self.thread_handler.stop(thread)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec())