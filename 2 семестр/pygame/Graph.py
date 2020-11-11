import pygame
import math

def f_graph(x1):
    y1 = math.log10(x1)
    return(y1)

a = 1
b = 100

grModeX = 800
grModeY = 600
pygame.init()
screen = pygame.display.set_mode([grModeX,grModeY])

sx = grModeX/(b-a)
h = 1/sx
xmid = grModeX // 2
ymid = grModeY // 2

x = a
maxF = f_graph(x)
minF = maxF

while x <= b:
    y = f_graph(x)
    print(y)
    if y < minF:
        minF = y
    if y > maxF:
        maxF = y
    x = x + h
    print(x)
    

sy = grModeY/(maxF - minF)

pygame.draw.line(screen, [255,255,255],[0,ymid],[grModeX,ymid])

pygame.draw.line(screen, [255,255,255],[xmid,0],[xmid,grModeY])


x = a

while x <= b:
    y = f_graph(x) - 1
    screen.set_at([xmid + round(sx*x), ymid-round(sy*y)],[255,255,255])
    x = x + h
    pygame.time.delay(10)
    pygame.display.flip()

pygame.time.delay(2000)

pygame.quit()








