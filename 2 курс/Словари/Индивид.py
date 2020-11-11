#Индивидуальная по славарям
#Про дом
from tkinter import *
f = open('dom.txt','r')
sf = f.readlines()
d = {}
k = 0
for s in sf:
    if k%3 == 0:
        key = s[:-1]
        d[key] = []
    if k%3 == 1:
        d[key].append(s[:-1])
    if k%3 == 2:
        d[key].append(s[:s.find(' ')])
        d[key].append(s[s.find(' ')+1:-1])
    k += 1
f.close()
def Exit(event):
    root.destroy()
def Fammm(event):
    flg = 0
    for key in d:
        if ent1.get() in d[key]:
            flg = 1
            if d[key][-1] == '1':
                print(d[key][-1])
                lb2 = Label(fra,text='Есть доступ в интернет',font='Arial 18')
                lb2.place(x=10,y=35)
            else:
                lb3 = Label(fra,text='Доступ в интернет отсутствует',font='Arial 18')
                lb3.place(x=10,y=35)
    if flg == 0:
        lb4 = Label(fra,text='Нет данных',font='Arial 18')
        lb4.place(x=10,y=35)
def Kva(event):
    flg = 0
    for key in d:
        if ent2.get() in key:
            lb9 = Label(fra,text='Фамилия хозяина:',font='Arial 18')
            lb9.place(x=10,y=115)
            lb5 = Label(fra,text=d[key][0],font='Arial 18')
            lb5.place(x=215,y=115)
            flg = 1
    if flg == 0:
        lb6 = Label(fra,text='В квартире №'+ent2.get()+' никто не живёт',font='Arial 18')
        lb6.place(x=10,y=115)
def Vop(event):
    z = 0
    for key in d:
        if d[key][-1] == '1':
            z += 1
    lb6 = Label(fra,text=z,font='Arial 18')
    lb6.place(x=300,y=195)

#Интерфейс
root = Tk()
root.title("Дом № 9")
fra = Frame(root,width=400,height=300)
fra.grid(row=0,column=0)
lb1 = Label(fra,text='Введите фамилию:')
lb1.place(x=10,y=15)
ent1 = Entry(fra)
ent1.place(x=150,y=17)
ent1.focus()
bt1 = Button(fra,text='OK')
bt1.place(x=285,y=16)
bt1.bind("<Button-1>",Fammm)
lb7 = Label(fra,text='Введите № квартиры:')
lb7.place(x=10,y=70)
lb8 = Label(fra,text='Сколько квартир имеют выход в интернет')
lb8.place(x=10,y=200)
ent2 = Entry(fra)
ent2.place(x=150,y=72)
ent2.focus()
bt2 = Button(fra,text='OK')
bt2.place(x=285,y=67)
bt2.bind("<Button-1>",Kva)
bt3 = Button(fra,text='?')
bt3.place(x=249,y=197)
bt3.bind("<Button-1>",Vop)
bt4 = Button(fra,text='Выход')
bt4.place(x=350,y=250)
bt4.bind("<Button-1>",Exit)
root.mainloop()
