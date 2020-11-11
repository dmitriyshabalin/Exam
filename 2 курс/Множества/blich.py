#!Среднее арифмитическое
from tkinter import *
from random import randint
def Exit(event):
    root.destroy()
def Viva(event):
    lb1 = Label(fra, text=A, bg="Aqua")
    lb1.place(x=130,y=10)
def Sum(event):
    s = 0
    for j in A:
        s += j
    s = s/20
    r=round(s,2)
    lb2 = Label(fra, text=r, bg="Aqua")
    lb2.place(x=130,y=50)
A = set()
while len(A) < 20:
    A.add(randint(-10,30))

#Интерфейс
root = Tk()
root.title("Среднее арифметическое")
fra = Frame(root, width=500, height=150, bg="Aqua")
fra.grid(row=0,column=0)
b1 = Button(fra, text="Вывод множества", bg="Lightyellow")
b1.place(x=10,y=10)
b1.bind("<Button-1>", Viva)
b2 = Button(fra, text="Найти", bg="Lightyellow")
b2.place(x=37,y=50)
b2.bind("<Button-1>", Sum)
b3 = Button(fra, text="Выход",bg="Lightyellow")
b3.place(x=37,y=100)
b3.bind("<Button-1>", Exit)


root.mainloop()
