from time import sleep
simv = '┼'
a = simv
Dlina = 6
for k in range(Dlina):
    print(' ' * (Dlina - len(a) // 2)+ a + ' ' * (Dlina - len(a) //2))
    a += simv*2
'''(►_◄)'''
