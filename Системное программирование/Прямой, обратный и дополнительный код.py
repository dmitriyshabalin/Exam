#Прямой, обратный и дополнительный код

from tkinter import *

def pisk(event):

    x = ['x']
    t = 0

    while x is not int:
        try:
            x = ent1.get()
            x = int(x)
            break
        except ValueError:
            lb5 = Label(fra,text="Пожалуйста, введите число!",bg='#6C2DC7',fg='white',font='Arial 16')
            lol = " "
            lb6 = Label(fra,text=lol,bg='#6C2DC7',width=30)
            lb6.place(x=10,y=40)
            lb5.place(x=70,y=160)
            lb7 = Label(fra,text=" ",bg='#6C2DC7',fg='white',width=50)
            lb7.place(x=10,y=70)
            lb7 = Label(fra,text=" ",bg='#6C2DC7',fg='white',width=50)
            lb7.place(x=10,y=100)
            break
           
    while t == 0:
        if x >127:
            lb5 = Label(fra,text="Повторите ввод",bg='#6C2DC7',fg='white')
            lb5.place(x=255,y=32)
            break
        elif x<-127:
            lb5 = Label(fra,text="Повторите ввод",bg='#6C2DC7',fg='white')
            lb5.place(x=255,y=32)
            break
        else:
            if x >= 0:
                d = bin(x)
                if d != 8:
                    p=8-len(d[2:])
                    e=0
                    e=str(e)
                    d = d[2:]
                    d = e*p+d
                lol = " "
                lb6 = Label(fra,text=lol,bg='#6C2DC7',width=30)
                lb6.place(x=255,y=36)
                lb3 = Label(fra,text="Прямой, обратный и дополнительный код имеют вид:",bg='#6C2DC7',fg='white')
                lb3.place(x=10,y=40)
                lb4 = Label(fra,text=d,bg='#6C2DC7',fg='white')
                lb4.place(x=320,y=42)
                lb7 = Label(fra,text=" ",bg='#6C2DC7',fg='white',width=50)
                lb7.place(x=10,y=70)
                lb7 = Label(fra,text=" ",bg='#6C2DC7',fg='white',width=50)
                lb7.place(x=10,y=100)
                t = 1
                
            else:
                d = bin(x)
                if d != 8:
                    p=7-len(d[3:])
                    e=0
                    e=str(e)
                    d = d[3:]
                    d = e*p+d
                lol = " "
                lb6 = Label(fra,text=lol,bg='#6C2DC7',width=30)
                lb6.place(x=255,y=36)
                lol1 = " "
                lb6 = Label(fra,text=lol1,bg='#6C2DC7',width=40)
                lb6.place(x=10,y=40)
                lb3 = Label(fra,text="Прямой код имеет вид:",bg='#6C2DC7',fg='white')
                lb3.place(x=10,y=40)
                lb4 = Label(fra,text="1"+d,bg='#6C2DC7',fg='white')
                lb4.place(x=150,y=42)
                l = len(d)
                d = str(d)
                y = [1]
                for i in d:
                    if i == "1":
                        y.append(0)
                    else:
                        y.append(1)
                lb7 = Label(fra,text="Обратный код имеет вид:",bg='#6C2DC7',fg='white')
                lb7.place(x=10,y=70)
                kek = []
                for i in range(len(y)):
                    kek.append(y[i])
                lb8 = Label(fra,text=kek,bg='#6C2DC7',fg='white')
                lb8.place(x=160,y=72)
                lb7 = Label(fra,text="Дополнительный код имеет вид:",bg='#6C2DC7',fg='white')
                lb7.place(x=10,y=100)
                s = -1
                while s != -9:
                    if y[s] == 0:
                        y[s] = 1
                        s = s-1
                        break
                    else:
                        y[s] = 0
                        s = s-1
                tuk = []
                for k in range(len(y)):
                    tuk.append(y[k])
                lb8 = Label(fra,text=tuk,bg='#6C2DC7',fg='white')
                lb8.place(x=197,y=102)
                t=1
#Интерфейс


root = Tk()
root.title("Прямой, обратный и дополнительный код")
fra = Frame(root,width=455,height=200,bg='#6C2DC7')
fra.grid(row=0,column=0)

lb1 = Label(fra,text='Введите число из указонного диапозона:',bg='#6C2DC7',fg='white')
lb1.place(x=10,y=10)

lb2 = Label(fra,text="Диапазон: [-127:127]",bg='#6C2DC7',font='Arial 16')
lb2.place(x=100,y=135)
    
ent1 = Entry(fra,width=20)
ent1.place(x=250,y=12)
ent1.focus()

b1 = Button(fra,text='Перевести',bg='#FF7F50')
b1.place(x=380,y=10)
b1.bind("<Button-1>",pisk)

root.mainloop()
