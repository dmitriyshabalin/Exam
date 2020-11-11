from random import randint
import turtle
import random
from tkinter import*
def tabl(event):
    act=turtle.Turtle()
    sss=100
    t=Text(root,width=30,height=14,bg='lightblue',font='Arial 20')
    t.pack()
    x=0
    y=0
    n=10
    v='пешеход повернул на восток'
    z='пешеход повернул на запад'
    u='пешеход повернул на юг'
    s='пешеход повернул на север'
    a=[randint(0,100) for i in range (n) ]
    xy=[]
    I=[]
    _colr=('Black','Red','Blue')
    turtle.reset()
    
    for i in a:
        act.color(random.choice(_colr))
        I.append(str(i))
        if i<25:
            x+=1
        elif i<50:
            x-=1
        elif i<75:
            y+=1
        else:
            y-=1
        xy.append(str(x)+';'+str(y))
        act.setx(x*sss)
        act.sety(y*sss)
        act.write(str(i))
        
    txtt = []
    if (abs(x)+abs(y))>2:
        t.insert(2.0,str(x)+'+'+str(y)+'='+str(x+y)+'\n')
        t.insert(3.0,'Пешеход вышел за два квартала \n')
    else:
        t.insert(2.0,str(x)+'+'+str(y)+'='+str(x+y)+'\n')
        t.insert(3.0,'Пешеход НЕ вышел за пределы 2х кварталов \n')
    for i in range(n):
        txtt.append(str(i+1)+' | '+str(I[i])+' | '+str(xy[i])+'\n')
    txtt.reverse()
    for rr in txtt:
        t.insert(1.0,rr)
    
root=Tk()
root.title('Задача о случайном блуждании')
b=Button(root, bg='lightblue', text='Показать решение задачи',font='20')

b.bind('<Button-1>',tabl)
b.pack()






