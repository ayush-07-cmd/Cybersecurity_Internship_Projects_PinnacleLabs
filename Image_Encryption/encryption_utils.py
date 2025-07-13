# encryption_utils.py

from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as file:
        file.write(key)

def load_key(filename='secret.key'):
    with open(filename, 'rb') as file:
        return file.read()

def encrypt_image(image_path, encrypted_path, key):
    f = Fernet(key)
    with open(image_path, 'rb') as file:
        original = file.read()
    encrypted = f.encrypt(original)
    with open(encrypted_path, 'wb') as file:
        file.write(encrypted)

def decrypt_image(encrypted_path, output_path, key):
    f = Fernet(key)
    with open(encrypted_path, 'rb') as file:
        encrypted = file.read()
    decrypted = f.decrypt(encrypted)
    with open(output_path, 'wb') as file:
        file.write(decrypted)
