# Домашнее задание по теме "Файлы в операционной системе".
import os
import time

print('Current dir:', os.getcwd())

directory_name = "."
for root, dirs, files in os.walk(directory_name, True, None, False):
    for file in files:
        filepath = os.path.join(directory_name, file)
        filetime = os.path.getmtime(f"{root}\{file}")
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(f'{root}\{file}')
        parent_dir = os.path.dirname(f'{root}\{file}')
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
