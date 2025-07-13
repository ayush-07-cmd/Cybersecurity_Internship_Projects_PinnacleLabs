from flask import Flask, render_template, request
from aes_des_rsa import *
import base64
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        algo = request.form['algorithm']
        mode = request.form['mode']

        try:
            # Logging timestamp
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"\n[{timestamp}] Algorithm: {algo} | Mode: {mode}\nInput: {text}\n"

            # AES Encryption/Decryption
            if algo == 'AES':
                if mode == 'encrypt':
                    key = get_random_bytes(16)
                    encrypted = aes_encrypt(text, key)
                    result = base64.b64encode(key + encrypted).decode()
                else:
                    raw = base64.b64decode(text)
                    key, data = raw[:16], raw[16:]
                    result = aes_decrypt(data, key)

            # DES Encryption/Decryption
            elif algo == 'DES':
                if mode == 'encrypt':
                    key = get_random_bytes(8)
                    encrypted = des_encrypt(text, key)
                    result = base64.b64encode(key + encrypted).decode()
                else:
                    raw = base64.b64decode(text)
                    key, data = raw[:8], raw[8:]
                    result = des_decrypt(data, key)

            # RSA Encryption/Decryption
            elif algo == 'RSA':
                if mode == 'encrypt':
                    encrypted = rsa_encrypt(text)
                    result = base64.b64encode(encrypted).decode()
                else:
                    data = base64.b64decode(text)
                    result = rsa_decrypt(data)

            # Save log to file
            log_entry += f"Output: {result}\n{'-'*60}"
            with open("history.txt", "a", encoding='utf-8') as f:
                f.write(log_entry)

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
