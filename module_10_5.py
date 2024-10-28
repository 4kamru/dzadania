# "Многопроцессное программирование"
import multiprocessing
from multiprocessing import Pool
import threading
from datetime import datetime

def read_info(name):
    all_data = []
    time_start = datetime.now()
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            # считываем строку
            line = file.readline()
            all_data.append(line)
            # прерываем цикл, если строка пустая
            if not line:
                break
    time_end = datetime.now()
    print(time_end - time_start)
    # print(all_data)

# линейный вызов
filenames = [f'./file {number}.txt' for number in range(1, 5)]
# for file in filenames:
#     read_info(file)

# линейный вызов ************************************************
# 0:00:01.365350
# 0:00:01.343408
# 0:00:01.339388
# 0:00:00.136631

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        pool.map(read_info,filenames)

# многопроцессный вызов - пока что разница несущественна
# 0:00:00.145611
# 0:00:01.568806
# 0:00:01.596731
# 0:00:01.656572