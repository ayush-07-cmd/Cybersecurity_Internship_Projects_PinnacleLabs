from flask import Flask, render_template, request
import re

app = Flask(__name__)

def analyze_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Make it at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
    else:
        suggestions.append("Include special characters.")

    common = ['password', '123456', 'admin', 'qwerty']
    if password.lower() in common:
        score = 1
        suggestions.append("Avoid using common passwords.")

    if score <= 3:
        strength = "Weak"
        color = "red"
    elif score <= 6:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, suggestions, color

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    suggestions = []
    color = "black"
    if request.method == 'POST':
        password = request.form['password']
        strength, suggestions, color = analyze_password(password)
    return render_template('index.html', strength=strength, suggestions=suggestions, color=color)

if __name__ == '__main__':
    app.run(debug=True)
