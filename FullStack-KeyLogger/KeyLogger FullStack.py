class Encryption:
    def __init__(self, key: str):
        self.key = str(key)
        self.key = [ord(c) for c in self.key]
    def encrypt(self, data: str):
        return  "".join((chr(ord(c) ^ self.key[i % len(self.key)])) for i, c in enumerate(data))
    def decrypt(self, data: str):
        return self.encrypt(data)




