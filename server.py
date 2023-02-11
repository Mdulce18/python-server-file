import os

from flask import Flask, request, abort, jsonify, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_DIRECTORY = "./files/"
DOWNLOAD_DIRECTORY = "./payloads/"

def create_directories(directories):
    for d in directories:
        if not os.path.exists(d):
            os.makedirs(d)

create_directories(["./files/","./payloads/"])
api = Flask(__name__)


@api.route("/payloads")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(DOWNLOAD_DIRECTORY):
        path = os.path.join(DOWNLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@api.route("/payloads/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(DOWNLOAD_DIRECTORY, path, as_attachment=True)


@api.route("/files_up", methods=["GET","POST"])
def post_file():
    if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(UPLOAD_DIRECTORY,secure_filename(f.filename)))
      return 'file uploaded successfully', 201

@api.route("/json", methods=["POST"])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    print(request.data)
    return 'JSON posted'

if __name__ == "__main__":
    api.run(host= '0.0.0.0',debug=False, port=4001)
