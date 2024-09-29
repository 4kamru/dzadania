#Задача "Записать и запомнить"
import os.path
from pprint import pprint
def custom_write(file_name, strings):
    # создаем файл, если его нет
    if not os.path.exists(file_name):
        file = open(file_name, 'w', encoding='utf-8')
        file.close()

    file = open(file_name,'a',encoding='utf-8')
    strings_positions = {}
    i=0
    for j in strings:
        i += 1
        # номер байта
        b_num = file.tell()
        file.write(f'{j}\n')
        strings_positions[(i,b_num)] = j

    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)