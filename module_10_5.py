# "Многопроцессное программирование"
import multiprocessing
from multiprocessing import Pool
import threading
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            # считываем строку
            line = file.readline()
            all_data.append(line)
            # прерываем цикл, если строка пустая
            if not line:
                break
    # print(all_data)

# линейный вызов
filenames = [f'./file {number}.txt' for number in range(1, 5)]
# time_start = datetime.now()
# for file in filenames:
#     read_info(file)
#
# time_end = datetime.now()
# print(f' Линейный вызов: {time_end - time_start}')

# Линейный вызов: 0: 00:04.761274


if __name__ == '__main__':
    time_start = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info,filenames)

    time_end = datetime.now()
    print(f' Многопроцессный вызов: {time_end - time_start}')

#  Многопроцессный вызов: 0:00:02.171647
