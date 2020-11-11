from tkinter import*
import pygame
pygame.init()


def col(event):
    a=pygame.mixer.Sound("a.wav")
    a.play()



w=Tk()
w.title("Звучание")
w.geometry("150x50")
Label(w,text="Нажмите клавишу:)").pack()
w.bind("<Key>",col)
w.mainloop()
