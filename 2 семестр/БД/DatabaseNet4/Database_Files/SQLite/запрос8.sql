﻿select ФИО, id_регистрации from Клиенты, Регистрация_работ where Клиенты.id_клиента = Регистрация_работ.id_клиента and Регистрация_работ.id_регистрации = '5';