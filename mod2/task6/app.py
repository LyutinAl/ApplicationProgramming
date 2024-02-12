from flask import Flask
import os


app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/preview/<size>/<path:rel_path>')
def preview(size, rel_path):
    abs_path = os.path.abspath(os.path.join(BASE_DIR, rel_path))
    try:
        with open(abs_path, 'r') as file:
            result_text = file.read(size)
    except FileNotFoundError:
        return 'Ошибка при открытии, файл не найден', 403
    except Exception as e:
        return f'Ошибка при открытии файла: {e}', 400

    return (f'<b>{abs_path}</b> {len(result_text)}<br>'
            f'{result_text}')
