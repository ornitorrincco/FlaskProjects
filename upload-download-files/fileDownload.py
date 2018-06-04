from flask import Flask,send_from_directory
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__,static_folder='static')

@app.route('/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(app.static_folder, filename)
