from flask import Flask,send_from_directory
import os

app = Flask(__name__,static_folder='static')

@app.route('/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(app.static_folder, filename)
