class Encryption:
    def __init__(self, key: int):
        self.key = key
    def encrypt(self, data: str):
        return  "".join((chr(ord(c) ^ self.key)) for c in data)
    def decrypt(self, data: str):
        return self.encrypt(data)

my_cryption = Encryption(5)
encryption = my_cryption.encrypt("Hello world")
print(encryption)
encryption = my_cryption.decrypt(encryption)
print(encryption)

