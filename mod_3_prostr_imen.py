calls = 0


def count_calls():  # Функция count_calls подсчитывающая вызовы остальных функций
    global calls
    calls += 1


def string_info(string):  # Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки,
    # строку в верхнем регистре, строку в нижнем регистре
    cortege = (len(string), string.upper(), string.lower())
    count_calls()
    return cortege


def is_contains(string, spisok):   # Функция is_contains принимает два аргумента: строку и список, и возвращает True,
    count_calls()                  # если строка находится в этом списке, False - если отсутствует. Регистром строки
    string = string.lower()        # при проверке пренебречь: UrbaN ~ URBAN
    for i in range(0, len(spisok)):
        spisok[i] = spisok[i].lower()
    return string in spisok


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
