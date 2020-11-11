p = input("Введите буквы: ")
f = open('text.txt','r')
print('Список работников:')
for j in f:
    if j[:len(p)].lower() == p.lower():
        print(j,end='')
f.close()
