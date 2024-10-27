import tkinter

from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os


def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл", filetypes=(('Text files', '.txt'),
                                                                                            ('All files', '*')))
    text['text'] = text['text'] + ' ' + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x150')
window.resizable(width=False, height=False)
text = tkinter.Label(window, text="Файл:", height=5, width=65, background='grey', foreground='red')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, text="Выберите файл", height=3, width=20, background='green',
                               foreground='purple', bg='silver', command=file_select)
button_select.grid(column=1, row=2, pady=5)
#window.configure(bg='silver')


window.mainloop()
