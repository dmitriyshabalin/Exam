from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def insertText():
    global file_name
    file_name = fd.askopenfilename()
    f = open(file_name,encoding="utf-8")
    s = f.read()
    text.insert(1.0, s)
    f.close()

def correctText():
    answer = mb.askyesno(title="Уважаемый, Иван Анатольевич", message="Перенести данные?")
    if answer == True:
        st = text.get(1.0,END).split('\n')
        p = 0
        for i in st:
            print(i)
            p+=1
            if p%2 != 0:
                i = i+'\n'
                text2.insert(END,i)

def extractText():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*") ))
    f = open(file_name, 'w')
    s = text2.get(1.0, END)
    f.write(s)
    f.close()
            

#Интерфейс

root = Tk()
root.title("Нечетные строки")

fra = Frame(root,width=778,height=250)
fra.grid(row=0,column=0)

text = Text(fra,width=43, height=15)
text.place(x=2,y=2)

b1 = Button(fra,text="Открыть",width=8,command=insertText)
b1.place(x=355,y=1)

b2 = Button(fra,text=">",width=8,command=correctText)
b2.place(x=355,y=100)

b3 = Button(fra,text="Сохранить",width=8,command=extractText)
b3.place(x=355,y=223)

text2 = Text(fra,width=43, height=15)
text2.place(x=425,y=2)


root.mainloop()
