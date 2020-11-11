#Город под подошвой
from tkinter import *
with open ('Slovari.txt','r') as f: #открываем файл
    d = f.readline()
    d = eval(d)
def Exit(event): #выход из программы
    root.destroy()
def Pisk(event): #поиск страны по городу
    q = ent1.get()
    z = 0
    for k in d:
        g = d[k]
        if q in g:
            lb2 = Label(fra,text=k)
            lb2.place(x=15,y=35)
            z = 1            
    if z == 0:
        lb3 = Label(fra,text='Города нет в словаре')
        lb3.place(x=230,y=10)
        lb4 = Label(fra,text='Добавить?')
        lb4.place(x=240,y=50)
        b1 = Button(fra,text='Да',bg='Pink')
        b1.place(x=310,y=47)
        b1.bind("<Button-1>",Dob)
        b5 = Button(fra,text='Нет',bg='Pink')
        b5.place(x=340,y=47)
        b5.bind("<Button-1>",Exit)
def Dob(event): #добавление новой страны
    q = ent1.get()
    z = 0
    lb5 = Label(fra,text='В какой стране город '+q+':')
    lb5.place(x=10,y=100)
    ent2.place(x=11,y=130)
    ent2.focus()
    b3 = Button(fra,text='ОК',bg='Pink')
    b3.place(x=140,y=130)
    b3.bind("<Button-1>",Ook)
def Ook(event):
    z = 0
    q = ent1.get()
    key = ent2.get()
    for k in d:
        if k == key:
            d[key].append(q)
            lb6 = Label(fra,text=k)
            lb6.place(x=15,y=35)
            z = 1
            with open('Slovari.txt','w') as f: #запись в файл
                f.write(str(d))
    if z == 0:
        ww = []
        ww.append(q)
        d[key] = ww
        lb7 = Label(fra,text=key)
        lb7.place(x=15,y=35)
        with open('Slovari.txt','w') as f:
            f.write(str(d))
#Интерфейс
root = Tk()
root.title("Страны и города")
fra = Frame(root,width=400,height=300,bg='Aqua')
fra.grid(row=0,column=0)
lb1 = Label(fra,text='Введите город:',bg='Aqua')
lb1.place(x=10,y=10)
ent1 = Entry(fra,width=20)
ent1.place(x=100,y=12)
ent1.focus()
ent2 = Entry(fra,width=20)
b2 = Button(fra,text='Поиск',bg='Pink')
b2.place(x=135,y=35)
b2.bind("<Button-1>",Pisk)
b4 = Button(fra,text='Выход',bg='Pink')
b4.place(x=330,y=250)
b4.bind("<Button-1>",Exit)


root.mainloop()
