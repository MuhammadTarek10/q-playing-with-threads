import cv2
import numpy
from PySide6.QtCore import QThread, Signal


class Camera(QThread):
    frame = Signal(numpy.ndarray)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def run(self):
        self._active = True
        cap = cv2.VideoCapture(0)
        while True:
            ret, image = cap.read()
            if ret:
                self.frame.emit(cv2.flip(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 1))
            else:
                cap = cv2.VideoCapture(0)
                continue
            if self.isInterruptionRequested():
                break
        cap.release()

    def stop(self):
        self.requestInterruption()
        self.wait()