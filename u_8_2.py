def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы - {i}')
    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        p_s = personal_sum(numbers)
        srdn_arif = p_s[0] / (len(numbers) - p_s[1])
    except ZeroDivisionError:
        print('В numbers записана пустая последовательность')
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    if srdn_arif == 0:
        return 0
    return srdn_arif

print(f'Результат 1: {calculate_average("1,2,3")}')
print(f'Результат 2: {calculate_average([1,"Строка",3,"Echo"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42,12,35,46])}')
print(f'Результат 5: {calculate_average([])}')