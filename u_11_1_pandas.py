import pandas
import numpy
# Для Series доступно взятие элемента по индексу, срезы, поэлементные математические операции аналогично массивам numpy
s = pandas.Series(numpy.arange(5), index=["a", "b", "c", "d", "e"])
print("Выбор одного элемента")
print(s["a"])
print("Выбор нескольких элементов")
print(s[["a", "d"]])
print("Срез")
print(s[1:])
print("Поэлементное сложение")
print(s + s)
# Для Series можно применять фильтрацию данных по условию, записанному в качестве индекса
s = pandas.Series(numpy.arange(5), index=["a", "b", "c", "d", "e"])
print("Фильтрация")
print(s[s > 2])
# Объекты Series имеют атрибут name со значением имени набора данных, а также атрибут index.name с именем для индексов
s = pandas.Series(numpy.arange(5), index=["a", "b", "c", "d", "e"])
s.name = "Данные"
s.index.name = "Индекс"
print(s)

# Объект класса DataFrame работает с двумерными табличными данными. Создать DataFrame проще всего из словаря
students_marks_dict = {"student": ["Студент_1", "Студент_2", "Студент_3"],
                       "math": [5, 3, 4],
                       "physics": [4, 5, 5]}
students = pandas.DataFrame(students_marks_dict)
print(students)
# У объекта класса DataFrame есть индексы по строкам (index) и столбцам (columns)
print(students.index)
print(students.columns)
# Для индекса по строке по умолчанию задаётся числовое значение. Значения индекса можно заменить путём записи списка в атрибут index
students.index = ["A", "B", "C"]
print(students)
# Для доступа к записям таблицы по строковой метке используется атрибут loc. При использовании строковой метки доступна операция среза
print(students.loc["B":])

# Для записи данных из DataFrame в CSV-файл используется метод to_csv(file)
students.to_csv("primer_pandas.csv")
# Получить дата-сет из файлов
students_2 = pandas.read_csv("primer_pandas_2.csv")
print('Students_2 содержит')
print(students_2)
# Для получения первых n строк дата-сета используется метод head(n)
print(students_2.head(2))
# Для получения последних n строк используется метод tail(n)
print(students_2.tail(3))
# В качестве индекса можно использовать условия для фильтрации данных. Выберем пять первых результатов теста
# по математике для студентов, прошедших подготовительный курс
print(students_2[students_2["test preparation course"] == "completed"]["math score"].head())
# Выведем пять лучших результатов тестов по трём дисциплинам для предыдущей выборки с помощью сортировки
# методом sort_values(). Сортировка по умолчанию производится в порядке возрастания значений. Для сортировки
# по убыванию в именованный аргумент ascending передаётся значение False
with_course = students_2[students_2["test preparation course"] == "completed"]
print(with_course[["math score",
                   "reading score",
                   "writing score"]].sort_values(["math score",
                                                  "reading score",
                                                  "writing score"], ascending=False).head())
