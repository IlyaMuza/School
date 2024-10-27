import time
import threading

def format_time_print(func):
    def wrapper(*args):
        res = float(func(*args))
        form_res = (f'{str(int(res // 3600)).zfill(2)}:{str(int(res % 60 // 60)).zfill(2)}:'
                      f'{str(int(res % 3600)).zfill(2)}.{int((res - int(res)) * 1000000)}')
        return form_res
    return wrapper


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for n in range(1,word_count + 1):
            f.write(f'Какое-то слово № {n}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name} с помощью потока {threading.current_thread()}')


@format_time_print
def str_time_delta(start, end):
    time_delta = str(end - start)
    return time_delta


time_start = time.time()
print(f'Текущий поток {threading.current_thread()}')
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time.time()
print(f'Время работы функций составило {str_time_delta(time_start, time_end)}')
thread1 = threading.Thread(target=write_words, args = (10, 'example5.txt', ))
thread2 = threading.Thread(target=write_words, args = (30, 'example6.txt', ))
thread3 = threading.Thread(target=write_words, args = (200, 'example7.txt', ))
thread4 = threading.Thread(target=write_words, args = (100, 'example8.txt', ))
time_start = time.time()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
time_end = time.time()
print(f'Время работы функций с использованием разных потоков составило {str_time_delta(time_start, time_end)}')


