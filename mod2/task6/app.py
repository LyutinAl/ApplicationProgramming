from flask import Flask
import os


app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/preview/<size>/<path:rel_path>')
def preview(size, rel_path):
    abs_path = BASE_DIR + '/' + rel_path
    with open(abs_path, 'r') as file:
        result_text = file.read(int(size))
    return f'Size is: {size}\nAbs. path is: {abs_path} \\\\\\\\{result_text}'
