from random import *
from math import*
from  tkinter import *
def P(event):    
    n=int(ent.get())
    ri=[round(random(),3) for  i in  range(n)]
    print(ri) #случайные числа ri  
    x=[]
    yi=[]
    a=1
    b=5
    for i in ri :
        xi=(i*(b-a))+a #нахождение xi
        y = (6*xi-(xi**2)-5)**2 #нахождение yi
        x.append(round(xi,3))
        yi.append(round(y,3))
    #print("yi=",yi)
    #решение интеграла
    #I = ((3*b)**2-((b**3)/3)-5*b)-((3*a)**2-((a**3)/3)-5*a)
    I = 34.133
    I1=(b-a)*(sum(yi))/n #нахождение I*
    ABS=fabs(I-I1) #нахождение abs
    #const
    gamma=0.95
    t=1.96
    pl=0.1
    Dx=((b-a)**2)/12 #нахождение D[X]
    n=((t**2)*Dx)/(pl**2)
    tx=('I='+str(round(I,3))+'\nI*='+str(round(I1,3))+'\nABS ='+str(round(ABS,3))+'\nn= '+str(round(n,3)))
    labe=Label(fra,text=tx,bg="Lightblue",font="Arial 13")
    labe.place(x=90,y=80)

#Интерфейс   
root=Tk()
root.title('Решение интеграла')
fra=Frame(root,width=300,height=200,bg="Pink")
fra.pack()
lib=Label(fra,text="Введите количество испытаний:",font="Arial 12")
lib.place(x=5,y=20)
ent=Entry(fra, width=5)
ent.focus()
ent.place(x=250,y=22)
ent.bind('<Return>',P)


root.mainloop()





