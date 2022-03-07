import os
import urllib.request
import json
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from datamanipulator import read_csv

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.environ.get("UPLOAD_FOLDER"), filename))
        probs, topics, representative_docs, frequency, topic_info = read_csv(os.path.join(os.environ.get("UPLOAD_FOLDER"), filename))
        print(topics)
        print(representative_docs)
        return topics, 200

        
    else:
        resp = jsonify(
            {'message': 'Only CSV is a allowed file type'})
        resp.status_code = 400
        return resp


if __name__ == "__main__":
    app.run()
