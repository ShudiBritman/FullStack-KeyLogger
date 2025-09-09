class Encryption:
    def __init__(self, key="IDF"):
        self.my_key = key
        self.key = sum(ord(c) for c in str(key))

    def encrypt(self, data):
        data = str(data)
        return "".join(chr(ord(c) ^ self.key) for c in data)

    def decrypt(self, data):
        data = str(data)
        return self.encrypt(data)