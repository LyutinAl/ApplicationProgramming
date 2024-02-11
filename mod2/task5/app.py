from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:subpath>')
def hello(subpath:str):
    numbers = subpath.split('/')
    try:
        max_number = max(int(number) for number in numbers)
    except ValueError:
        return 'Получен неверный URL, укажите URL в виде \'/max_number/[0-9.*]/[0-9.*]...\''
    return f'Максимальное число: {max_number}'
