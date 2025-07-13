# app.py

from flask import Flask, render_template, request, send_file
import os
from encryption_utils import generate_key, save_key, load_key, encrypt_image, decrypt_image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    image = request.files['image']
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    encrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], 'encrypted_' + image.filename)
    
    image.save(image_path)
    key = generate_key()
    save_key(key)
    encrypt_image(image_path, encrypted_path, key)
    
    return send_file(encrypted_path, as_attachment=True)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    image = request.files['image']
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    decrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], 'decrypted_' + image.filename)
    
    image.save(image_path)
    key = load_key()
    decrypt_image(image_path, decrypted_path, key)

    return send_file(decrypted_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
