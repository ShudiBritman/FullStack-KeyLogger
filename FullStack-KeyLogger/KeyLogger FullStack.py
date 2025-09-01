class XorCipher()
    def __init__(self, key: str):
        self.key = [ord(c) for c in key]