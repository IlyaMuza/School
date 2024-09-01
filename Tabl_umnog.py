import tkinter as tk
import random

def primer_generate():
    a = random.randrange(2,10)
    b = random.randrange(2,10)
    primer = str(a) + ' X ' + str(b) + ' = '
    return a, b, primer

# def get_values():
#     if str(number1_entry.get())=='':
#         number1_entry.insert(0,'0')
#     if number2_entry.get() == '':
#         number2_entry.insert(0,'0')
#     num1 = int(number1_entry.get())
#     num2 = int(number2_entry.get())
#     return num1, num2
#
# def insert_values(res):
#     answer_entry.delete(0, 'end')
#     answer_entry.insert(0, res)

def starting():
    global count_primer, a, b, primer, number_prav
    count_primer += 1
    number1 = tk.Label(window, text='                  ')
    number1.place(x=100, y=10)
#    number1.destroy()
    number2 = tk.Label(window, text='                  ')
    number2.place(x=100, y=35)
    number3 = tk.Label(window, text='                  ')
    number3.place(x=100, y=60)
    number4 = tk.Label(window, text='                  ')
    number4.place(x=100, y=85)
    number5 = tk.Label(window, text='                  ')
    number5.place(x=100, y=110)
    number6 = tk.Label(window, text='                  ')
    number6.place(x=100, y=135)
    number7 = tk.Label(window, text='                  ')
    number7.place(x=100, y=160)
    number8 = tk.Label(window, text='                  ')
    number8.place(x=100, y=185)
    number9 = tk.Label(window, text='                  ')
    number9.place(x=100, y=210)
    number10 = tk.Label(window, text='                  ')
    number10.place(x=100, y=235)
    a, b, primer = primer_generate()
    if count_primer == 1:
        number1 = tk.Label(window, text=primer)
        number1.place(x=100, y=10)
        count_primer = 1
        number_prav = 0

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def label_v_primer(primer):
    global count_primer
    count_primer += 1
    if count_primer == 1:
        number1 = tk.Label(window, text=primer)
        number1.place(x=100, y=10)
    if count_primer == 2:
        number2 = tk.Label(window, text=primer)
        number2.place(x=100, y=35)
    if count_primer == 3:
        number3 = tk.Label(window, text=primer)
        number3.place(x=100, y=60)
    if count_primer == 4:
        number4 = tk.Label(window, text=primer)
        number4.place(x=100, y=85)
    if count_primer == 5:
        number5 = tk.Label(window, text=primer)
        number5.place(x=100, y=110)
    if count_primer == 6:
        number6 = tk.Label(window, text=primer)
        number6.place(x=100, y=135)
    if count_primer == 7:
        number7 = tk.Label(window, text=primer)
        number7.place(x=100, y=160)
    if count_primer == 8:
        number8 = tk.Label(window, text=primer)
        number8.place(x=100, y=185)
    if count_primer == 9:
        number9 = tk.Label(window, text=primer)
        number9.place(x=100, y=210)
    if count_primer == 10:
        number10 = tk.Label(window, text=primer)
        number10.place(x=100, y=235)

def proverka_otveta():
    global number_prav, count_primer, a, b, primer, res
    res = a * b
    if int(answer_entry.get()) == res:
        number_prav += 1
    str_number_prav = 'Правильных ответов ' + str(number_prav) + ' из 10'
    number11 = tk.Label(window, text=str_number_prav)
    number11.place(x=185, y=10)
    if int(answer_entry.get()) == res and count_primer == 1:
        number1 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        number1.place(x=100, y=10)
    elif count_primer == 1:
        number1 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        number1.place(x=100, y=10)
    if int(answer_entry.get()) == res and count_primer == 2:
        number2 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        number2.place(x=100, y=35)
    elif count_primer == 2:
        number2 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        number2.place(x=100, y=35)
    if int(answer_entry.get()) == res and count_primer == 3:
        number3 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        number3.place(x=100, y=60)
    elif count_primer == 3:
        number3 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        number3.place(x=100, y=60)
    if int(answer_entry.get()) == res and count_primer == 4:
        number4 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        number4.place(x=100, y=85)
    elif count_primer == 4:
        number4 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        number4.place(x=100, y=85)
    if int(answer_entry.get()) == res and count_primer == 5:
        number5 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        number5.place(x=100, y=110)
    elif count_primer == 5:
        number5 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        number5.place(x=100, y=110)
    if int(answer_entry.get()) == res and count_primer == 6:
        number6 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        number6.place(x=100, y=135)
    elif count_primer == 6:
        number6 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        number6.place(x=100, y=135)
    if int(answer_entry.get()) == res and count_primer == 7:
        number7 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        number7.place(x=100, y=160)
    elif count_primer == 7:
        number7 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        number7.place(x=100, y=160)
    if int(answer_entry.get()) == res and count_primer == 8:
        number8 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        number8.place(x=100, y=185)
    elif count_primer == 8:
        number8 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        number8.place(x=100, y=185)
    if int(answer_entry.get()) == res and count_primer == 9:
        number9 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        number9.place(x=100, y=210)
    elif count_primer == 9:
        number9 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        number9.place(x=100, y=210)
    if int(answer_entry.get()) == res and count_primer == 10:
        number10 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        number10.place(x=100, y=235)
    elif count_primer == 10:
        number10 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        number10.place(x=100, y=235)


def otvet():
    global count_primer, a, b, primer
    proverka_otveta()
    if count_primer >= 10:
        pass
    else:
        a, b, primer = primer_generate()
        label_v_primer(primer)
    answer_entry.delete(0, 'end')


window = tk.Tk()
window.title('Таблица умножения')
window.geometry("350x350")
window.resizable(False,False)
button_add = tk.Button(window, text="Запуск", width=6, height=2, command=starting)
button_add.place(x=90, y=260)
button_add = tk.Button(window, text="Стоп", width=6, height=2, command=sub)
button_add.place(x=150, y=260)
button_add = tk.Button(window, text="Принять", width=6, height=2, command=otvet)
button_add.place(x=210, y=260)
# button_add = tk.Button(window, text="/", width=2, height=2, command=delen)
# button_add.place(x=250, y=200)
# number1_entry = tk.Entry(window, width=30)
# number1_entry.place(x=100, y=75)
# number2_entry = tk.Entry(window, width=28)
# number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=325)
# number1 = tk.Label(window, text="")
# number1.place(x=100, y=50)
# number2 = tk.Label(window, text="")
# number2.place(x=100, y=75)
# number3 = tk.Label(window, text="")
# number3.place(x=100, y=100)
# number4 = tk.Label(window, text="")
# number4.place(x=100, y=125)
# number5 = tk.Label(window, text="")
# number5.place(x=100, y=150)
# number6 = tk.Label(window, text="")
# number6.place(x=100, y=175)
# number7 = tk.Label(window, text="")
# number7.place(x=100, y=200)
# number8 = tk.Label(window, text="")
# number8.place(x=100, y=225)
# number9 = tk.Label(window, text="")
# number9.place(x=100, y=250)
# number10 = tk.Label(window, text="")
# number10.place(x=100, y=275)
answer = tk.Label(window, text="Введите ответ")
answer.place(x=100, y=300)

number_prav = 0
count_primer = 0
a = 1
b = 1
primer = 'Пример не сгенерирован'
res = 0
# a, b, primer = primer_generate()
# number1(text=primer)



window.mainloop()