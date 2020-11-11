#Рейтинг учащихся по среднему баллу
f = open('Имена и баллы.txt','r')
k = 0 #счетчик слов
d = {}
spb = [] #счетчик баллов
for s in f:
    if k%2 == 0:
        key = s[:-1] #убираем 'enter'
    else:
        p = s[:-1]
        sp = list(map(int, p.split()))
        srb = round(sum(sp)/len(sp),2)
        d[key] = srb
        spb.append(srb)
    k += 1
spb = sorted(spb) #сортируем в порядке возрастания
spb.reverse() #теперь в порядке убывания
print('Рейтинг учащихся по среднему баллу')
for b in spb: #цикл по отсортированному списку баллов
    for key in d: #цикл по ключу словаря
        if d[key] == b:
            print(key+'-'+str(d[key]))
f.close()
