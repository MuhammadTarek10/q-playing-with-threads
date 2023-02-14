import cv2
import numpy
from PySide6.QtCore import QThread, Signal


class Camera(QThread):
    frame = Signal(numpy.ndarray)
    def run(self):
        self._active = True
        cap = cv2.VideoCapture(0)
        while self._active:
            ret, image = cap.read()
            if ret:
                self.frame.emit(cv2.flip(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 1))
            else:
                cap = cv2.VideoCapture(0)
                continue
        cap.release()

    def stop(self):
        self._active = False
        self.terminate()