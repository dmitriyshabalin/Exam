from tkinter import *
global slst
global hhh
global slst
slst = {'Россия':['Troick','Moscow','Ufa','Tomsk','Omsk','Sankt-Piterburg'],
        'Казахстан':["Астана","Алма-Ата"],
        "Франция":['Париж',"Леон","Марсель","Прованс"],
        "Англия":["Лондон","Ливерпуль","Манчестер"],
        "Китай":["Пекин","Шанхай","Циндао"]}
hhh = 0
def click(event):
    global hhh
    global slst
    hhh = 0
    for k in slst:
        g = slst[k]
        for i in g:
            i = str(k)+" - "+str(i)+'\n'
            text1.insert(1.0,i)
            hhh += 1
            text1.configure(height=hhh)
def rez(event):
    global slst
    h = []
    text1.delete(1.0,END)
    h.append(ent1.get())
    for k in h:
        j = 0
        for i in slst:
            g = slst[i]
            for y in g:
                if k == y:
                    ppp = str(k+' - '+i)
                    text1.insert(1.0,ppp)
                    j += 1
        if j == 0:
            win = Toplevel(root, relief=SUNKEN, bd=5, bg='blue')
            win.title('WoW')
            win.minsize(width=400, height=200)
            u = str('\nГорода '+str(k)+' нет, включить его в словарь?')
            lab=Label(win,font='Arial 18',text=u)
            lab.pack()
            butyes=Button(win,text='Да')
            butyes.pack()
            butno=Button(win,text='Нет')
            butno.pack()
            def nooo(event):
                win.destroy()
            butno.bind('<Button-1>',nooo)
            def yess(event):
                butyes.destroy()
                butno.destroy()
                lab.configure(text='Введите страну к которой он относится')
                butok=Button(win,text='Ок')
                ent2=Entry(win,width=30,bd=3)
                ent2.pack()
                stran = str(ent2.get())
                butok.pack()
                def okk(event):
                    global slst
                    u = 0
                    stran = str(ent2.get())
                    for i in slst:
                        if i == stran:
                            g = slst[i]
                            g.append(k)
                            slst[i] = g
                            u += 1
                    if u == 0:
                        kk = []
                        kk.append(k)
                        slst[stran] = kk
                    win.destroy()
                    rez(click)
                butok.bind('<Button-1>',okk)
            butyes.bind('<Button-1>',yess)



root = Tk()


fra = Frame(root,width=1000,height=500,bg='blue')
but1 = Button(fra,width=15,text='Вывести словарь')
text1 = Text(fra,width=50,height=hhh,bd=5)
but4 = Button(fra,width=15,text='Проверить город')
ent1 = Entry(fra,width=50,bg='#999',bd=3)



fra.pack()
ent1.pack()
but4.pack()
text1.pack()
but1.pack()

but4.bind('<Button-1>',rez)
but1.bind('<Button-1>',click)


root.mainloop()
