import pygame #Импорт модуля
pygame.init()

kol = [1,2,3,4,5,6,7,8,9,10]

while True:
    print("Введите число страниц(от 1 до 10)!!!")
    kol_iter = int(input()) #Кол-во страниц
    if kol_iter in kol:

        screen = pygame.display.set_mode([950,550]) #Расширение экрана
        pygame.display.set_caption('Копир') # Загаловок окна

        screen.fill([255,255,255]) # Цвет экрана

        kopir = pygame.image.load("print.jpg") # Добавление картинки
        screen.blit(kopir, [250, 30])
        pygame.display.flip()


        y = 500 #Положение страниц слева
        stopka = 10 #Изначальная высота стопки готовых страниц
        y_pos = y #Позиция стопки готовых страниц
        pol = kol_iter * 10 - 10 #Высота изначальной стопки 
        y_nach = y - pol #Положение по y изначальной стопки

        while kol_iter != 0: #Кол-во итераций(в звисимости от страниц)

            x = 20 #Положение страницы по x
            y_st = 400 #Положение страницы по y

            screen.fill([200,200,200],[20,y_nach,200,pol]) #Изначальная стопка

            #for i in range(9):
            while y_st > 10: #Движение страницы вверх
                screen.fill([200,200,200],[20,y_st,200,10])
                pygame.display.flip()
                pygame.time.delay(300)

                screen.fill([255,255,255],[20,y_st,200,10])

                y_st -= 30

            #for j in range(7):
            while x < 720: #Движение страницы вправо
                screen.fill([200,200,200],[x,y_st,200,10])
                pygame.display.flip()
                pygame.time.delay(300)

                screen.fill([255,255,255],[x,y_st,200,10])

                x += 100

            #for i in range(8):
            while y_st < 450: #Движение страницы вниз
                screen.fill([200,200,200],[x,y_st,200,10])
                pygame.display.flip()
                pygame.time.delay(300)

                screen.fill([255,255,255],[x,y_st,200,10])

                y_st += 30
                
            
            screen.fill([200,200,200],[x,y_pos,200,stopka]) #Стопка готовых страниц
            pygame.display.flip()
            pygame.time.delay(300)

            screen.fill([255,255,255],[20,y_nach,200,pol]) #Стереть изначальную стопку страниц

            y_nach += 10 #Изменение положения изначальной стопки
            pol -= 10 #Изменение высоты изначальной стопки

            kol_iter -= 1 #Минус страница
            stopka += 10 #Увеличиваем высоту стопки готовых страниц
            y_pos -= 10 #Изменяем положение стопки с готовыми страницми
            

    pygame.time.delay(3000)
    pygame.quit() #Выход из программы

