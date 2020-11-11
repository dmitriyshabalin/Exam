#Большая доля мальчиков
f = open('klass.txt','r')
D = {}
sp = []
for s in f:
    mas = list(s[:-1].split())
    key = mas[0]
    m = int(mas[1])
    d = int(mas[2])
    pm = round(m*100/(m+d),2)
    D[key] = pm
    sp.append(pm)
f.close()
print(D)
print('Мальчиков больше в классах:')
for key in D:
    if D[key]>50:
        print(key)
