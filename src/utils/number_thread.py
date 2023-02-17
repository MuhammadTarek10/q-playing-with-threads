from random import randint
from time import sleep

from PySide6.QtCore import QThread, Signal


class Number(QThread):
    value = Signal(str)
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def run(self):
        self._active = True
        while self._active:
            randomValue = randint(0, 100)
            self.value.emit(str(randomValue))
            sleep(1)
            
    
    def stop(self):
        self._active = False
        self.wait()