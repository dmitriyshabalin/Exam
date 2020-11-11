#!Summ
x=0
s=0
while x!='Стоп':
    x=input("Введите число ")
    if x=="Стоп":
        break
    else:
        x=int(x)
        s+=x
print(s)
