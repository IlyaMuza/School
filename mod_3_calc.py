import tkinter as tk

def get_values():
    if str(number1_entry.get())=='':
        number1_entry.insert(0,'0')
    if number2_entry.get() == '':
        number2_entry.insert(0,'0')
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(res):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def umnog():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def delen():
    num1, num2 = get_values()
    if num2 == 0:
        answer_entry.delete(0, 'end')
        answer_entry.insert(0, 'Деление на 0')
    else:
        res = num1 / num2
        insert_values(res)

window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False,False)
button_add = tk.Button(window, text="+", width=2, height=2, command=add)
button_add.place(x=100, y=200)
button_add = tk.Button(window, text="-", width=2, height=2, command=sub)
button_add.place(x=150, y=200)
button_add = tk.Button(window, text="*", width=2, height=2, command=umnog)
button_add.place(x=200, y=200)
button_add = tk.Button(window, text="/", width=2, height=2, command=delen)
button_add.place(x=250, y=200)
number1_entry = tk.Entry(window, width=30)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text="Введите первое число")
number1.place(x=100, y=50)
number2 = tk.Label(window, text="Введите второе число")
number2.place(x=100, y=125)
answer = tk.Label(window, text="Результат")
answer.place(x=100, y=275)
window.mainloop()