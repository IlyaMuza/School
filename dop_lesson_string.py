# Напишите программу, которая принимает строку от пользователя и выводит на экран первые 3 символа строки.
# Если строка короче 3 символов, выведите всю строку.
#a=input()
#print(a[0:3])

# Напишите программу, которая принимает строку от пользователя и выводит на экран последние 3 символа строки.
# Если строка короче 3 символов, выведите всю строку
#a=input()
#print(a[-3:])

# Напишите программу, которая принимает строку от пользователя и выводит на экран символы с шагом 2 начиная со второго
# символа и до предпоследнего символа. Если строка короче 3 символов, выведите всю строку.
#a=input()
#if len(a) < 3: print(a)
#a=a[0:len(a)-1]
#print(a[1::2])

# Написать программу, которая принимает на вход строку и выводит первую и последнюю букву строки, а также все символы
# между ними в обратном порядке.
#a=input()
#b=a[::-1]
#b=b[1:len(b)-1]
#print(a[0] + a[-1] + b)

# Напишите программу на Python, чтобы получить строку из первых 2 и последних 2 символов из заданной строки.
# Если длина строки меньше 2, верните вместо пустой строки.
# Пример строки: «w3resource»
# Ожидаемый результат: 'w3ce'
# Пример строки: 'w3'
# Ожидаемый результат: 'w3w3'
# Пример строки: 'w'
# Ожидаемый результат: пустая строка
#a = input()
#if len(a) < 2: print('пустая строка')
#if len(a) >= 2: print(a[0:2] + a[-2:])

# Напишите программу на Python, чтобы получить строку из заданной строки, в которой все вхождения ее первого символа
# были заменены на '$', кроме самого первого символа.
# Пример строки: «abc», «xyz»
# Ожидаемый результат: 'xyc abz'
# Решение по примеру:
#a = input()
#mesto_probela = a.find(' ')
#b = a[0:mesto_probela-1]
#c = a[mesto_probela+1:-1]
#resultat = c + a[mesto_probela-1] + ' ' + b + a[-1]
#print(resultat)
# Решение по условиям задачи, как я это понял
#b = a[0] + a.replace(a[0],'$')
#b = b[0] + b[2:]
#print(b)

# Напишите программу на Python, чтобы заменить данную строку новой строкой, в которой были изменены первый
# и последний символы.
#a = input()
#b = a[1:-1]
#b = input('На что заменить первый символ? ')[0] + b + input('На что заменить последний символ? ')[0]
#print(b)

# Напишите скрипт Python, который принимает ввод от пользователя и отображает его обратно в верхнем и нижнем регистре
a = input()
b = list(a)
b.clear()
for i in range(0, len(a)):
    if a[i].isupper():
        b.append(a[i].lower())
    if a[i].islower():
        b.append(a[i].upper())
    a = a[0:i] + str(b[i]) + a[i+1:]
print(a)