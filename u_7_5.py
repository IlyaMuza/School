import os, time

print('текущая директория ', os.getcwd())
if os.path.exists('sec'):
    os.chdir('sec')
else:
    os.mkdir('sec')
    os.chdir('sec')
#os.makedirs(r'third\forth')
print('Список всего listdir ', os.listdir())
os.chdir(r'C:\Users\User\PycharmProjects\pythonProject')
for i in os.walk('.'):
    print('walk: ', i)

file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print('Files: ', file)
print('Direktory: ', dirs)
print(os.stat(file[3]).st_size)
print(os.stat(file[3]))
#os.system('pip install random2')
print('=-=-=-=-' * 20)

# Начало Домашнего задания
directory = r'C:\Windows\Help'
print(f'Поиск файлов в директории {directory}'.center(183, '~'))
for root, dirs, files in os.walk(directory):
    for fi in files:
        file_path = os.path.join(os.path.abspath('.'),root[2:],fi)
        file_time = os.path.getmtime(os.path.join(root,fi))
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        print(f'Обнаружен файл: {fi}'.ljust(30, ' '), f'Путь: {file_path}'.ljust(45, ' '),
              f'Размер: {file_size} байт'.ljust(20, ' '),
              f'Время изменения: {formatted_time}'.ljust(35, ' '),
              f'Родительская директория: {os.path.dirname(file_path)}')

