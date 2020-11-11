# определение согласных, невходящих в слова
from tkinter import *
def Exit(event):
    root.destroy()
def Glih(event):
    f = tx.get(1.0)
    g = ('б','в','г','д','ж','з','к','л','м','н','п','р','с','т','ф','х','ш','щ','ц','ч')
    s = ''
    for k in g:
        if k not in f:
            s = s + k  + ' '
    lb = Label(fra, text = s, height = 1, width = 30, font = '18')
    lb.place(x = 10, y = 340)
    lob = Label (fra, text = 'Согласные буквы, которые не входят в ваш текст:')
    lob.place(x = 10, y = 315)

#Интерфейс
root = Tk()
fra = Frame(root,width = 400,height = 400,bg = 'lightblue')
fra.grid(row = 0,column = 0)
tx = Text(fra,width = 47, height = 15)
'''
f = open('text.txt', 'r')
f.close()
'''
tx.place(x = 10,y = 10)
tx.focus()
bt1 = Button(fra, text = 'Найти', bg = 'pink')
bt1.place(x = 170, y = 280)
bt1.bind('<Button-1>', Glih)
bt2 = Button(fra, text = 'Выход', bg = 'pink')
bt2.place(x = 170, y = 375)
bt2.bind('<Button-1>', Exit)
root.mainloop()
        

