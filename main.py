from tkinter import *
import tkinter as tk

from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import numpy as np

root = Tk()

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 500
h = h - 225
root.geometry('1000x470+{}+{}'.format(w, h))
root.title("Метод експертної оцінки")

showinfo(
        title='Оберіть файл з матрицею',
        message='Будь ласка, оберіть файл з матрицею!'
    )

filetypes = (
    ('text files', '*.txt'),
    ('All files', '*.*')
)

filename = fd.askopenfilename(
    title='Відкрити файл',
    initialdir='/',
    filetypes=filetypes)

class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=10, font=('Arial', 10))
                self.e.grid(row=i, column=j, padx=10, pady=10)
                self.e.insert(END, lst[i][j])

lst = np.loadtxt(filename, dtype='U', encoding='utf-8', delimiter=',')

total_rows = len(lst)
total_columns = len(lst[0])
t = Table(root)

def count():

    lst = np.loadtxt(filename, dtype='U', encoding='utf-8', delimiter=',')

    foreigner = round(float(lst[1][2]) * float(lst[1][3]) + float(lst[2][2]) * float(lst[2][3]) + float(lst[3][2]) * float(lst[3][3]) + float(lst[4][2]) * float(lst[4][3]) + float(lst[5][2]) * float(lst[5][3]), 2)

    eagles = round(float(lst[1][2]) * float(lst[1][4]) + float(lst[2][2]) * float(lst[2][4]) + float(lst[3][2]) * float(lst[3][4]) + float(lst[4][2]) * float(lst[4][4]) + float(lst[5][2]) * float(lst[5][4]), 2)

    fleetwood_mac = round(float(lst[1][2]) * float(lst[1][5]) + float(lst[2][2]) * float(lst[2][5]) + float(lst[3][2]) * float(lst[3][5]) + float(lst[4][2]) * float(lst[4][5]) + float(lst[5][2]) * float(lst[5][5]), 2)

    heart = round(float(lst[1][2]) * float(lst[1][6]) + float(lst[2][2]) * float(lst[2][6]) + float(lst[3][2]) * float(lst[3][6]) + float(lst[4][2]) * float(lst[4][6]) + float(lst[5][2]) * float(lst[5][6]), 2)

    queen = round(float(lst[1][2]) * float(lst[1][7]) + float(lst[2][2]) * float(lst[2][7]) + float(lst[3][2]) * float(lst[3][7]) + float(lst[4][2]) * float(lst[4][7]) + float(lst[5][2]) * float(lst[5][7]), 2)

    pink_floyd = round(float(lst[1][2]) * float(lst[1][8]) + float(lst[2][2]) * float(lst[2][8]) + float(lst[3][2]) * float(lst[3][8]) + float(lst[4][2]) * float(lst[4][8]) + float(lst[5][2]) * float(lst[5][8]), 2)

    best_70_80s_rock_band = {foreigner: lst[0, 3], eagles: lst[0, 4], fleetwood_mac: lst[0, 5], heart: lst[0, 6], queen: lst[0, 7], pink_floyd: lst[0, 8]}
    best_70_80s_rock_band = best_70_80s_rock_band.get(max(best_70_80s_rock_band))

    text1.delete("1.0", END)
    text1.insert("1.0", best_70_80s_rock_band)
    text1.insert("1.0", '\n\nОтже, найкращий рок-гурт 70-80-тих: ')
    text1.insert("1.0", pink_floyd)
    text1.insert("1.0", ': ')
    text1.insert("1.0", lst[0, 8])
    text1.insert("1.0", '\n')
    text1.insert("1.0", queen)
    text1.insert("1.0", ': ')
    text1.insert("1.0", lst[0, 7])
    text1.insert("1.0", '\n')
    text1.insert("1.0", heart)
    text1.insert("1.0", ': ')
    text1.insert("1.0", lst[0, 6])
    text1.insert("1.0", '\n')
    text1.insert("1.0", fleetwood_mac)
    text1.insert("1.0", ': ')
    text1.insert("1.0", lst[0, 5])
    text1.insert("1.0", '\n')
    text1.insert("1.0", eagles)
    text1.insert("1.0", ': ')
    text1.insert("1.0", lst[0, 4])
    text1.insert("1.0", '\n')
    text1.insert("1.0", foreigner)
    text1.insert("1.0", ': ')
    text1.insert("1.0", lst[0,3])
    text1.insert("1.0", 'Визначення експертної оцінки кожного гурту: \n\n')

labelframe = LabelFrame(root, text="Розв'язок", width=980, height=210)
labelframe.place(x=10, y=240)

text1 = tk.Text(width=120, height=11)
text1.place(x=15, y=260)

b1 = tk.Button(text="Обчислити", command=count).place(x=885, y=105)

root.mainloop()