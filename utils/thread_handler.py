from types import FunctionType

from PySide6.QtCore import Signal


class ThreadHandler:
    def __init__(self, threads: list) -> None:
        self.threads = threads

    def start(self):
        for thread in self.threads:
            thread.start()

    def connect(self, threadSignal: Signal, func: FunctionType):
        threadSignal.connect(func)

    def stopAll(self):
        for thread in self.threads:
            thread.stop()

    def stop(self, thread):
        self.threads[thread].stop()