# class Person:
#     pass
# Person.money =  150
# obj1 = Person()
# obj2 = Person()
# obj1.name = 'Bob'
# obj2.name = 'Masha'
# print(obj1.name, 'has', obj1.money, 'dollars.')
# print(obj2.name, 'has', obj2.money, 'dollars.')


# создание класса , методов и обьектов

# class Person():
#     name = ""
#     money = 0
#
# obj1 = Person()
# obj2 = Person()
#
# obj1.name = 'Bob'
# obj1.money = 150
#
# obj2.name = 'Masha'
#
# print(obj1.name, 'has', obj1.money, 'dollars.')
# print(obj2.name, 'has', obj2.money, 'dollars.')


# создание класса , методов и обьектов


# class Person():
#     name = ""
#     money = 0
#     def out(self):
#         print(self.name, 'has', self.money, 'dollars')
#     def changemoney(self, newmoney):
#         self.money = newmoney
#
# obj1 = Person()
# obj2 = Person()
# obj1.name = 'Bob'
# obj2.name = 'Masha'
# obj1.out()
# obj2.out()
# obj1.changemoney(150)
# obj1.out()

# создание класса , методов и обьектов


# class Critter():
#     ''' виртуальный питомец'''
#     def talk(self):
#         print('привет, я животное - экземпляр класса Critter.')
#
# crit = Critter()
# crit.talk()
# input("\n нажмите enter, чтобы выйти.")


# применение конструкторов


# class Critter():
#     '''виртуальный питомец '''
#     def __init__(self):
#         print('появилось на свет новое животное!')
#     def talk(self):
#         print('\n привет, я животное - экземпляр класса Critter.')
# crit1 = Critter()
# crit2 = Critter()
# crit1.talk()
# crit2.talk()


# применение атрибутов



# class Critter():
#     '''виртуальный питомец '''
#     def __init__(self, name):
#         print('появилось на свет новое животное!')
#         self.name = name
#     def __str__(self):
#         rep = 'обьект класса Critter\n'
#         rep += 'имя:' + self.name + "\n"
#         return rep
#     def talk(self):
#         print('привет. меня зовут', self.name, '\n')
#
# crit1 = Critter('Бобик')
# crit1.talk()
#
# crit2 = Critter('Мурзик')
# crit2.talk()
#
# print('вывод обьекта crit1 на экран:')
# print(crit1)
#
# print('доступ к атрибуту crit1.name:')
# print(crit1.name)
# input("\n нажмите enter, чтобы выйти.")


# применение атрибутов класса и статических методов


# class Critter():
#     '''виртуальный питомец '''
#     total = 0
#     @staticmethod
#     def status():
#         print('\nвсего животных сейчас', Critter.total)
#     def __init__(self, name):
#         print('появилось на свет новое животное!')
#         self.name = name
#         Critter.total += 1
#
# print(" Значение атрибута класса Critter.total :", end= " ")
# print(Critter.total)
#
# print('\nсоздаю животных.')
# crit1 = Critter('появилось на свет новое животное!')
# crit2 = Critter('появилось на свет новое животное!')
# crit3 = Critter('появилось на свет новое животное!')
#
# Critter.status()
# print('\nнахожу значение атрибута класса через обьект:', end= " ")
# print(crit1.total)
# input("\n нажмите enter, чтобы выйти.")


# инкапсуляция


# class A:
#     def _privat(self):
#         print('это закрытый метод!')
#
# a = A()
# a._privat()


# инкапсуляция



# class B:
#     def __private(self):
#         print('это закрытый метод!')
# b = B()
# b.__private()
# ''' доступ только  таким образом'''
# b._B__private()


# инкапсуляция


# class Critter ():
#     """ Виртуальный питомец """
#     def __init__(self, name, mood):
#         print(" Появилось на свет новое животное !")
#         self.name = name
#         self.__mood = mood
#     def talk(self):
#         print("\n Меня зовут ", self.name)
#         print(" Сейчас я чувствую себя ", self.__mood, "\n")
#     def __private_method (self):
#         print("Это закрытый метод!")
#     def public_method(self):
#         print("Это открытый метод!")
#         self.__private_method()
#
# crit = Critter(name="Бобик", mood="прекрасно")
# crit.talk()
# crit.public_method()
# input("\n Нажмите Enter, чтобы выйти.")


# доступ к атрибутам


# class Critter():
#     """ Виртуальный питомец """
#     def __init__(self, name):
#         print("Появилось на свет новое животное !")
#         self.__name = name
#     @ property
#     def name(self):
#         return self.__name
#     @ name.setter
#     def name(self, new_name):
#         if new_name == "":
#             print("Имя животного не может быть пустой строкой.")
#         else:
#             self.__name = new_name
#             print("Имя успешно изменено.")
#     def talk(self):
#         print("\n Привет, меня зовут ", self.name)
#
# crit = Critter("Бобик")
# crit.talk()
# print("\n Мое животное зовут :", end=" ")
# print(crit.name)
# print("\n Попробую изменить имя животного на Шарик...")
# crit.name = "Шарик"
# print("Мое животное зовут :", end=" ")
# print(crit.name)
# print("\n Попробую изменить имя животного на пустую строку...")
# crit.name = ""
# print("Мое животное зовут :", end=" ")
# print(crit.name)
# input("\n Нажмите Enter, чтобы выйти.")


# мое животное


# class Critter():
#     """ Виртуальный питомец """
#     def __init__(self, name, hunger=0, boredom=0):
#         self.name = name
#         self.hunger = hunger
#         self.boredom = boredom
#     def __pass_time(self):
#         self.hunger += 1
#         self.boredom += 1
#
#     @property
#     def mood(self):
#         unhappiness = self.hunger + self.boredom
#         if unhappiness < 5:
#             m = " прекрасно "
#         elif 5 <= unhappiness <= 10:
#             m = " неплохо "
#         elif 11 <= unhappiness <= 15:
#             m = " так себе "
#         else:
#             m = " ужасно "
#         return m
#
#     def talk(self):
#         print("Меня зовут ", self.name, end=" ")
#         print(" и сейчас я чувствую себя ", self.mood, "\n ")
#         self.__pass_time()
#     def eat(self, food = 4):
#         print("М ppp. Спасибо.")
#         self.hunger -= food
#         if self.hunger < 0:
#             self.hunger = 0
#         self.__pass_time()
#
#     def play(self, fun=4):
#         print(" Уиии !")
#         self.boredom -= fun
#         if self.boredom < 0:
#             self.boredom = 0
#         self.__pass_time()
# def main():
#     crit_name = input("Как вы назовете свое животное ?:")
#     crit = Critter(crit_name)
#     choice = None
#     while choice != "0":
#         print\
#         ("""
#         Мое животное
#         0 – Выйти
#         1 – Узнать о самочувствии животного
#         2 – Покормить животное
#         3 – Поиграть с животным
#         """)
#         choice = input(" Ваш выбор : ")
#         print()
#         if choice == "0":
#             print("До свидания.")
#         elif choice == "1":
#             crit.talk()
#         elif choice == "2":
#             crit.eat()
#         elif choice == "3":
#             crit.play()
#         else:
#             print("\n Извините, в меню нет пункта ", choice)
# main()



# наследование


# class Person:
#     def __init__( self, n):
#         self.name= n
#     def write(self):
#         print (self.name)
# class Student(Person):
#     def __init__(self, gr, n):
#         Person.__init__(self, n)
#         self.group = gr
#     def write(self):
#         print(self.name, self.group)
# p = Person("Petya")
# p.write()
# s = Student(23, "Vasya")
# s.write()



# полиморфизм



# class T1:
#     n=10
#     def total(self, N):
#         self.total = int(self.n) + int(N)
# class T2:
#     def total(self,s):
#         self.total = len(str(s))
# t1 = T1()
# t2 = T2()
# t1.total(45)
# t2.total(45)
# print(t1.total)
# print(t2.total)


# Банк



# class Person(): # родительский класс
#     def __init__(self, fio): # метод-конструктор
#         self.fio = fio
#         #print("Person", self.fio, "created")
#     def __str__(self): # возвращает строку, которая
#         return self.fio # содержит значение атрибута fio
#
#
# class Sotrudnik(Person): # дочерний класс
#     def __init__(self, fio, job_title): # унаследовал атрибут
#         Person.__init__(self, fio) # родительского класса fio
#         self.job_title = job_title
#         print(self.job_title,"-", self.fio, "\n" )
#     def kredit(self, client):
#         client.dolg()
#         print(self.fio, " оформил кредит \n")
#     def vklad(self, client):
#         client.dohod()
#         print(self.fio, " оформил вклад \n ")
#
# class Client(Person):
#     def __init__(self, fio, sum_vklada, sum_kr):
#         Person.__init__(self, fio)
#         self.sum_vklada = sum_vklada
#         self.sum_kr = sum_kr
#         print("Клиент:", self.fio, " Сумма кредита:", self.sum_kr,
#             "Сумма вклада:", self.sum_vklada, "\n")
#     def dohod(self, persent=0.03):
#         self.sum_vklada = float(self.sum_vklada * (1 + persent))
#     def dolg(self, persent=0.18, amount=0):
#         self.sum_kr = float(self.sum_kr * (1 + persent))
#         self.sum_kr -= amount
#     def out(self):
#         print(" Клиент:", self.fio, " Сумма долга:", self.sum_kr)
#         print(" Клиент:", self.fio, " Доход:", self.sum_vklada)
#
#
# name_s = input("Введите ФИО сотрудника:")
# job_s = input("Введите должность:")
# name_c = input("Введите ФИО клиента:")
# svk = int(input("Введите сумму вклада:"))
# skr = int(input("Введите c умму кредита:"))
# obj1 = Sotrudnik(name_s, job_s)
# obj2 = Client(name_c, svk, skr)
# obj1.vklad(obj2)
# obj1.kredit(obj2)
# obj2.out()
# input("\n\n Нажмите Enter чтобы выйти.")



