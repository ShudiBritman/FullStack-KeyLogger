class Encryption:
    def __init__(self, key="IDF"):
        self.my_key = key
        key = str(key)
        self.key = [ord(c) for c in key]
    def encrypt(self, data):
        data = str(data)
        return  "".join((chr(ord(c) ^ self.key[i % len(self.key)])) for i, c in enumerate(data))
    def decrypt(self, data):
        data = str(data)
        return self.encrypt(data)



