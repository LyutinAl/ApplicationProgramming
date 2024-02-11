from flask import Flask
from datetime import datetime
# import sys

# weekdays = [('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'),
#             ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
#             {1: 'Понедельник',
#              2: 'Вторник',
#              3: 'Среда',
#              4: 'Четверг',
#              5: 'Пятница',
#              6: 'Суббота',
#              7: 'Воскресенье'}]
# for type_ in weekdays:
#     print(f'For type: {type(type_)}, size is {sys.getsizeof(type_)}')

weekdays = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')

app = Flask(__name__)


@app.route('/hello_world/<name>')
def hello(name):
    weekday = datetime.today().weekday()
    return f'Hello, {name}. Хорошей {weekdays[weekday]}!'
