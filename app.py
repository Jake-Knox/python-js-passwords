from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password/<int:length>')
def generate_password_route(length):
    password = generate_password(length)
    return jsonify(password=password)

if __name__ == '__main__':
    app.run()