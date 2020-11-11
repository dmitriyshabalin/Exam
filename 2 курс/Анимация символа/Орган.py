from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import calendar
import datetime
from menul import *

days = []
now = datetime.datetime.now()
year = now.year
month = now.month
def kakal(event):
    def prew():
        
        global month, year
        month -= 1
        if month == 0:
            month = 12
            year -= 1
        fill()

    def next():
        global month, year
        month += 1
        if month == 13:
            month = 1
            year += 1
        fill()


    def fill():
        info_label['text'] = calendar.month_name[month] + ', ' + str(year)
        month_days = calendar.monthrange(year, month)[1]
        if month == 1:
            prew_month_days = calendar.monthrange(year-1, 12)[1]
        else:
            prew_month_days = calendar.monthrange(year, month - 1)[1]
        week_day = calendar.monthrange(year, month)[0]
        for n in range(month_days):
            days[n + week_day]['text'] = n+1
            days[n + week_day]['fg'] = 'black'
            if year == now.year and month == now.month and n == now.day:
                days[n + week_day]['background'] = 'green'
            else:
                days[n + week_day]['background'] = 'lightgray'
        for n in range(week_day):
            days[week_day - n - 1]['text'] = prew_month_days - n
            days[week_day - n - 1]['fg'] = 'gray'
            days[week_day - n - 1]['background'] = '#f3f3f3'
        for n in range(6*7 - month_days - week_day):
            days[week_day + month_days + n]['text'] = n+1
            days[week_day + month_days + n]['fg'] = 'gray'
            days[week_day + month_days + n]['background'] = '#f3f3f3'

    root = Tk()
    root.title('Calendar')


    prew_button = Button(root, text='<', command=prew)
    prew_button.grid(row=0, column=0, sticky='nsew')
    next_button = Button(root, text='>', command=next)
    next_button.grid(row=0, column=6, sticky='nsew')
    info_label = Label(root, text='0', width=1, height=1, font=('Verdana', 16, 'bold'), fg='blue')
    info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')
    for n in range(7):
        lbl = Label(root, text=calendar.day_abbr[n], width=1, height=1, 
                    font=('Verdana', 10, 'normal'), fg='darkblue')
        lbl.grid(row=1, column=n, sticky='nsew')
    for row in range(6):
        for col in range(7):
            lbl = Label(root, text='0', width=4, height=2, 
                        font=('Verdana', 16, 'bold'))
            lbl.grid(row=row+2, column=col, sticky='nsew')
            days.append(lbl)
    fill()
    root.mainloop()


def blan(event): 
    class MyWin(QtWidgets.QMainWindow):
        
        def __init__(self, parent=None):
            QtWidgets.QWidget.__init__(self, parent)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            
            self.ui.actionExit.triggered.connect(self.close)

            self.ui.actionSave.triggered.connect(self.saveToFile)
            
            self.ui.actionOpen.triggered.connect(self.showDialog)


        def closeEvent(self,e):
            pass

        def saveToFile(self):
            res = QtWidgets.QMessageBox.question(self,"Confirm Dialog",
            "Save text before quit?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.No)
            if res == QtWidgets.QMessageBox.Yes:
                options = QtWidgets.QFileDialog.Options()
                self.fileName, _= QtWidgets.QFileDialog.getSaveFileName(self,'Save To File','','Text Files(*.html)',options=options)
                if self.fileName:
                    self.writeFile = open(self.fileName, 'w', encoding='utf-8')
                self.writeFile.write(self.ui.TextEdit.toHtml())  
                self.writeFile.close()
                self.ui.statusbar.showMessage('Save to %s' %self.fileName)
            else:
                e.ignore()

        def showDialog(self):
            fil = QFileDialog.getOpenFileName(self, 'Open', '/menul')[0]
            f = open(fil, 'r',encoding='utf-8')
            
            with f:
                data = f.read()
                self.ui.TextEdit.setText(data)
                    


    if __name__=="__main__":
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyWin()
        myapp.show()
        sys.exit(app.exec_())
        
def kalkulator(event):
    def cool(key):
        
        if key=="=":
            st="+-1234567890//*"
            
            if ent.get()[0]not in st:
                
                ent.insert(END,"Ошибка")
                messagebox.showerror("Ошибка","error")
            try:
                
                res=eval(ent.get())
                ent.insert(END,"="+str(res))
                
            except:
                ent.insert(END,"Ошибка")
                messagebox.showerror("Ошибка","error")
                
        elif key=="C":
            
            ent.delete(0,END)
            
        elif key=="+/-":
            
            if "=" in ent.get():
                ent.delete(0,END)
            try:
                if ent.get()[0]=="-":
                    ent.delete(0)
                else:
                    ent.insert(0,"-")
            except IndexError:
                pass
        else:
            if "=" in ent.get():
                ent.delete(0,END)
            ent.insert(END,key)
            
   
                
    root2=Tk()
    root2.title("Калькулятор")
    
    frak=Frame(root2,width=220,height=200,bg="#8AA9A5")
    frak.pack()
    butlist=["7","8","9","+","-",
             "4","5","6","*","/",
             "1","2","3","=","+/-",
             "0",".","C"]
    r=10
    c=40
    
    for i in butlist:
        
        cmd=lambda x=i: cool(x)
        ttk.Button(frak,text=i,command=cmd,width=5).place(x=r,y=c)
        r+=40
        
        if r>170:
            r=10
            c+=25
            
    ent=Entry(frak,width=28)
    ent.place(x=20,y=5)
    
    root2.mainloop()

    
    
    
   
#main
root=Tk()
root.title("Органайзер")
fra=Frame(root,width=400,height=500, bg="lightpink")

but=Button(fra,text="Калькулятор")
but.bind("<1>",kalkulator)
but.place(x=20,y=130)

but1=Button(fra,text="Календарь")
but1.bind("<1>",kakal)
but1.place(x=140,y=130)


but2=Button(fra,text="Блакнот")
but2.place(x=20,y=280)
but2.bind("<1>",blan)

fra.pack()
root.mainloop()
            
