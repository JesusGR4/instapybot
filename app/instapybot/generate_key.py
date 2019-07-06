from cryptography.fernet import Fernet
import os

path = "./generated_key.key"
if not os.path.isfile(path):
    key = Fernet.generate_key()
    file = open(path, 'wb')
    file.write(key)
    file.close()
