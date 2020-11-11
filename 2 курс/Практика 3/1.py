from easygui import *

x = msgbox("Работа функции msgbox() модуля EasyGUI", "О программе", "Закрыть","python.gif")
print(x, type(x))
'''
y = ccbox("Сообщение", "Заголовок окна", ("Продолжить", "Закончить"))
print(y, type(y))
z = ynbox("Хорошо себя чувствуете?", "Тест", ("ДА", "НЕТ"))
print(z, type(z))
q = buttonbox("Сообщение", "Заголовок", ("1", "2", "3"), ("python.gif", "python.gif"))
print(q, type(q))
w = indexbox("Сообщение", "Заголовок", ("1", "2", "3"))
print(w, type(w))
e = boolbox("Сообщение", "Заголовок", ("Да", "Нет"))
print(e, type(e))
r = choicebox("Сообщение","Заголовок", ("Первый","Второй", "Третий"), preselect=1)
print(r, type(r))
t = multchoicebox("Сообщение", "Заголовок", ("Первый", "Второй", "Третий")) 
print(t, type(t))
u = enterbox("Введите ваш login", "Авторизация", default = "user", strip = "True")
print(u, type(u))
i = integerbox("Введите ваш возраст", "Авторизация", default = "17", lowerbound = 1, upperbound = 100)
print(i, type(i))
o = multenterbox("Укажите ваши данные", "Авторизация", fields = ("Фамилия", "Имя", "Возраст"),
                 values = ("Каракуц", "Татьяна", "18"))
print(o, type(o))
p = passwordbox("Введите пароль", "Авторизация")
print(p, type(p))
a = multpasswordbox("Укажите Ваши данные", "Регистрация", ("Фамилия","Имя","Возраст"))
print(a, type(a))
s = textbox("Введите текст","Создание текста",text="Привет",codebox=False)
print(s, type(s))
d = codebox("Собщение","Заголовок окна",text="")
print(d, type(d))
f = diropenbox("Сообщение","Заголовок окна","work")
print(f, type(f))
g = fileopenbox(title="Заголовок",default="*",filetypes="*.py",multiple=False)
print(g, type(g))
h = filesavebox("","Выбор файла",default="",filetypes="*")
print(h, type(h))
'''















