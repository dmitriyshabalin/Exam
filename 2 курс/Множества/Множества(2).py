#!Пересечения
from tkinter import *
def Exit(event):
    root.destroy()
def Sech(event):
    x = ent1.get().split(' ')
    y = ent2.get().split(' ')
    x = set(x)
    y = set(y)
    q = x&y
    q.discard(' ')
    lb3 = Label(fra,text=q,bg='Aqua')
    lb3.place(x=150,y=70)
#Интерфейс
root = Tk()
root.title("Поиск одинаковых чисел")
fra = Frame(root,width=370,height=150,bg='Aqua')
fra.grid(row=0,column=0)
lb1 = Label(fra,text='Введите первый список:',bg='Aqua')
lb1.place(x=10,y=10)
ent1 = Entry(fra,width=20)
ent1.place(x=150,y=10)
ent1.focus()
lb2 = Label(fra,text='Введите второй список:',bg='Aqua')
lb2.place(x=11,y=40)
ent2 = Entry(fra,width=20)
ent2.place(x=150,y=40)
lb4 = Label(fra,text='Пересечения:',bg='Aqua')
lb4.place(x=25,y=70)
b1 = Button(fra,text='Найти',bg='Lightyellow')
b1.place(x=300,y=21)
b1.bind("<Button-1>",Sech)
b2 = Button(fra,text='Выход',bg='Lightyellow')
b2.place(x=160,y=100)
b2.bind("<Button-1>",Exit)


root.mainloop()
