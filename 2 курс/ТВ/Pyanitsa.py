from turtle import *
t = Turtle()
t.screen.setup(800, 800)
t.shape("turtle")
t.stamp()
t.color('black')
from random import randint
import math
q = 0
h = 0
z = 0
#z = int(input('Введите количество опытов: '))
#h = z
#while z!= 0:
x = 0
y = 0
N = 10
t.left(90)
while N != 1:
    r = (randint(0,99))
    if r < 25:
        x = x+1
        t.goto(h+30,z)
        h = 30
    elif r < 50:
        x = x-1
        t.goto(h,z)
    elif r < 75:
        y = y+1
        t.goto(h,z+30)
        z = 30
    else:
        y = y-1
        t.goto(h,z)
    N = N-1
print(x)
print(y)
if math.fabs(x) + math.fabs(y) <= 2:
    print('Успешно')
    q += 1
else:
    print('Он ушёл дальше, чем два квартала')
    #z = z-1
#p = h - q
#t = p*100/h
#l = 100 - t
#print('Пройдено успешно: ',l,'%')
#turtle.reset()


t.screen.exitonclick()
t.screen.mainloop()



        
