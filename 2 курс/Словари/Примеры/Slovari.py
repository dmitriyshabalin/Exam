#Страны и города в файле
from tkinter import *
def Job(b):
    with open ('Slovari.txt','r') as f:
        a = f.readline()
        a = eval(a)
    b = input()
    b = b[0].upper() + b[1:].lower()
    for k in b:
        if k.lower() not in 'йцукенгшщзхъфывапролджэячсмитьбю-':
            b = ''
            break
    vhodit = False
    if b != '':
        for k in a:
            if b in a[k]:
                print('Город принадлежит стране "',k,'"')
                vhodit = True
        if vhodit == False:
            while True:
                print('Добавить в словарь?')
                i = int(input('Если да, нажмите "1": '))
                if i == 1:
                    i = input('В какой стране находится город '+b+'? ')
                    if i in a:
                        a[i] += [b]
                    else:
                        a[i] = [b]
                    break
                else:
                    break
    with open('txt.txt','w') as f:
        f.write(str(a))
def ujo(a):
    print(a)
