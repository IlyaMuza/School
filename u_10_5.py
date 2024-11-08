import multiprocessing
import time
from multiprocessing import Pool


def read_info(name):
    start_t = time.time()
    all_data = []  # Создавать локальный список all_data
    with open(name, 'r', encoding='utf-8') as f:  # Открывать файл name для чтения
        for line in f:
            if line == '':  # Считывать информацию построчно (readline), пока считанная строка не окажется пустой
                break
            all_data.append(line)  # добавлять каждую строку в список
    end_t = time.time()
    print('In function for file', name, 'Time result', end_t - start_t)
    print('Process working: ', multiprocessing.Process.name)

if __name__ == '__main__':
    file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']  # Создайте список названий файлов в соответствии с названиями файлов архива
    start_time = time.time()
    for n in file_list:  # Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
        read_info(n)
    end_time = time.time()
    print('Line process result ', end_time - start_time)
    print()

    start_time = time.time()
    print('Multi start')
    with Pool(processes=8) as p:  # Вызовите функцию read_info для каждого файла, используя многопроцессный подход
        p.map(read_info, file_list)
    end_time = time.time()
    print('Multi process result ', end_time - start_time)



