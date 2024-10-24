from random import choice
# 1 часть
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))
# 2 часть
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for elem in data_set:
                file.write(str(elem) + '\n')
        return None

    return write_everything

write = get_advanced_writer('example_9_4.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# 3 часть
class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        return choice(self.words)

first_ball = MysticBall('Да','Нет','Наверное')
print(first_ball())
print(first_ball())
print(first_ball())