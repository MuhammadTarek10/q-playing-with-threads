from types import FunctionType

from PySide6.QtCore import Signal


class ThreadHandler:
    def __init__(self, threads: list) -> None:
        self.threads = threads

    def startAll(self):
        for thread in self.threads:
            thread.start()

    def start(self, thread: int):
        self.threads[thread].start()

    def connect(self, threadSignal: Signal, func: FunctionType):
        threadSignal.connect(func)

    def stopAll(self):
        for thread in self.threads:
            thread.stop()

    def stop(self, thread: int):
        self.threads[thread].stop()