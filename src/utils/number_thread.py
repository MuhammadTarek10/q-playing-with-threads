from random import randint
from time import sleep

from PySide6.QtCore import QThread, Signal


class Number(QThread):
    value = Signal(str)
    def run(self):
        while True:
            randomValue = randint(0, 100)
            self.value.emit(str(randomValue))
            sleep(1)
    
    def stop(self):
        self.terminate()