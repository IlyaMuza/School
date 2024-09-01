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
    global count_primer, a, b, primer, number_prav, lbl1,lbl2,lbl3,lbl4,lbl5,lbl6,lbl7,lbl8,lbl9,lbl10, lbl11
    count_primer = 1
    lbl1 = tk.Label(window, text='                  ')
    lbl1.place(x=100, y=10)
    lbl2 = tk.Label(window, text='                  ')
    lbl2.place(x=100, y=35)
    lbl3 = tk.Label(window, text='                  ')
    lbl3.place(x=100, y=60)
    lbl4 = tk.Label(window, text='                  ')
    lbl4.place(x=100, y=85)
    lbl5 = tk.Label(window, text='                  ')
    lbl5.place(x=100, y=110)
    lbl6 = tk.Label(window, text='                  ')
    lbl6.place(x=100, y=135)
    lbl7 = tk.Label(window, text='                  ')
    lbl7.place(x=100, y=160)
    lbl8 = tk.Label(window, text='                  ')
    lbl8.place(x=100, y=185)
    lbl9 = tk.Label(window, text='                  ')
    lbl9.place(x=100, y=210)
    lbl10 = tk.Label(window, text='                  ')
    lbl10.place(x=100, y=235)
    lbl11 = tk.Label(window, text='                                                       ')
    lbl11.place(x=185, y=10)
    # lbl1.destroy()
    # lbl2.destroy()
    # lbl3.destroy()
    # lbl4.destroy()
    # lbl5.destroy()
    # lbl6.destroy()
    # lbl7.destroy()
    # lbl8.destroy()
    # lbl9.destroy()
    # lbl10.destroy()
    # lbl11.destroy()
    a, b, primer = primer_generate()
    if count_primer == 1:
        lbl1 = tk.Label(window, text=primer)
        lbl1.place(x=100, y=10)
        number_prav = 0


def label_v_primer(primer):
    global count_primer, lbl1,lbl2,lbl3,lbl4,lbl5,lbl6,lbl7,lbl8,lbl9,lbl10
    count_primer += 1
    if count_primer == 1:
        lbl1 = tk.Label(window, text=primer)
        lbl1.place(x=100, y=10)
    if count_primer == 2:
        lbl2 = tk.Label(window, text=primer)
        lbl2.place(x=100, y=35)
    if count_primer == 3:
        lbl3 = tk.Label(window, text=primer)
        lbl3.place(x=100, y=60)
    if count_primer == 4:
        lbl4 = tk.Label(window, text=primer)
        lbl4.place(x=100, y=85)
    if count_primer == 5:
        lbl5 = tk.Label(window, text=primer)
        lbl5.place(x=100, y=110)
    if count_primer == 6:
        lbl6 = tk.Label(window, text=primer)
        lbl6.place(x=100, y=135)
    if count_primer == 7:
        lbl7 = tk.Label(window, text=primer)
        lbl7.place(x=100, y=160)
    if count_primer == 8:
        lbl8 = tk.Label(window, text=primer)
        lbl8.place(x=100, y=185)
    if count_primer == 9:
        lbl9 = tk.Label(window, text=primer)
        lbl9.place(x=100, y=210)
    if count_primer == 10:
        lbl10 = tk.Label(window, text=primer)
        lbl10.place(x=100, y=235)

def proverka_otveta():
    global number_prav, count_primer, a, b, primer, res, lbl1,lbl2,lbl3,lbl4,lbl5,lbl6,lbl7,lbl8,lbl9,lbl10, lbl11
    res = a * b
    if int(answer_entry.get()) == res:
        number_prav += 1
    str_number_prav = 'Правильных ответов ' + str(number_prav) + ' из 10'
    lbl11 = tk.Label(window, text=str_number_prav)
    lbl11.place(x=185, y=10)
    if int(answer_entry.get()) == res and count_primer == 1:
        lbl1 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        lbl1.place(x=100, y=10)
    elif count_primer == 1:
        lbl1 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        lbl1.place(x=100, y=10)
    if int(answer_entry.get()) == res and count_primer == 2:
        lbl2 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        lbl2.place(x=100, y=35)
    elif count_primer == 2:
        lbl2 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        lbl2.place(x=100, y=35)
    if int(answer_entry.get()) == res and count_primer == 3:
        lbl3 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        lbl3.place(x=100, y=60)
    elif count_primer == 3:
        lbl3 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        lbl3.place(x=100, y=60)
    if int(answer_entry.get()) == res and count_primer == 4:
        lbl4 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        lbl4.place(x=100, y=85)
    elif count_primer == 4:
        lbl4 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        lbl4.place(x=100, y=85)
    if int(answer_entry.get()) == res and count_primer == 5:
        lbl5 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        lbl5.place(x=100, y=110)
    elif count_primer == 5:
        lbl5 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        lbl5.place(x=100, y=110)
    if int(answer_entry.get()) == res and count_primer == 6:
        lbl6 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        lbl6.place(x=100, y=135)
    elif count_primer == 6:
        lbl6 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        lbl6.place(x=100, y=135)
    if int(answer_entry.get()) == res and count_primer == 7:
        lbl7 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        lbl7.place(x=100, y=160)
    elif count_primer == 7:
        lbl7 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        lbl7.place(x=100, y=160)
    if int(answer_entry.get()) == res and count_primer == 8:
        lbl8 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        lbl8.place(x=100, y=185)
    elif count_primer == 8:
        lbl8 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        lbl8.place(x=100, y=185)
    if int(answer_entry.get()) == res and count_primer == 9:
        lbl9 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        lbl9.place(x=100, y=210)
    elif count_primer == 9:
        lbl9 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        lbl9.place(x=100, y=210)
    if int(answer_entry.get()) == res and count_primer == 10:
        lbl10 = tk.Label(window, text=primer + str(answer_entry.get()), background='green')
        lbl10.place(x=100, y=235)
    elif count_primer == 10:
        lbl10 = tk.Label(window, text=primer + str(answer_entry.get()), background='red')
        lbl10.place(x=100, y=235)


def otvet():
    global count_primer, a, b, primer
    if count_primer > 10:
        pass
    proverka_otveta()
    a, b, primer = primer_generate()
    label_v_primer(primer)
    answer_entry.delete(0, 'end')


window = tk.Tk()
window.title('Таблица умножения')
window.geometry("350x350")
window.resizable(False,False)
button_add = tk.Button(window, text="Запуск", width=10, height=2, command=starting)
button_add.place(x=90, y=260)
# button_add = tk.Button(window, text="Стоп", width=6, height=2, command=sub)
# button_add.place(x=150, y=260)
button_add = tk.Button(window, text="Принять", width=10, height=2, command=otvet)
button_add.place(x=200, y=260)
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