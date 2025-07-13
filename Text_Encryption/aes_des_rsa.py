from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import rsa

# AES
def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.iv + cipher.encrypt(pad(data.encode(), AES.block_size))

def aes_decrypt(enc_data, key):
    iv = enc_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc_data[16:]), AES.block_size).decode()

# DES
def des_encrypt(data, key):
    cipher = DES.new(key, DES.MODE_CBC)
    return cipher.iv + cipher.encrypt(pad(data.encode(), DES.block_size))

def des_decrypt(enc_data, key):
    iv = enc_data[:8]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc_data[8:]), DES.block_size).decode()

# RSA
(pubkey, privkey) = rsa.newkeys(512)

def rsa_encrypt(data):
    return rsa.encrypt(data.encode(), pubkey)

def rsa_decrypt(enc_data):
    return rsa.decrypt(enc_data, privkey).decode()
