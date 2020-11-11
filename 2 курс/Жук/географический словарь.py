# Города и страны
#def Goroda(event):
with open('geografy.txt', 'r') as file:
    qw = file.readline()
    qw = eval(qw)
f = input('Введите город: ')
s = 0
for g in qw:
    if f in qw[g]:
        print(g)
        s = 1
        break
#print(Goroda)
if s == 0:
    print('Такого города нет, добавьте этот город')
    h = input('Введите страну в которой находится город ' + f +' ' )
    with open ('geografy.txt', 'w') as file:
        file.write(str(h))
    
