import time
n = '\n'*40
h = input('Simvol: ')
for k in range(15):
    print(h)
    time.sleep(0.5)
    print(n)
    h = ' ' + h
