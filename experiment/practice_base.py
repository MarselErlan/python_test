# # генераторы списков
# listone = [2, 3, 4]
# listtwo = [2*i for i in listone if i > 2]
# print(listtwo)

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

# # lambda-форма
# points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
# points.sort(key=lambda i: i['y'])
# print(points)

points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

# # модуль logging
# import os, platform, logging
# if platform.platform().startswith('windows'):
#     logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
# else:
#     logging_file = os.path.join(os.getenv('HOME'), 'test.log')
# print("сохраняем лог в", logging_file)
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename=logging_file,
#     filemode='w',
# )
# logging.debug("начало программы")
# logging.info("какие-то действия")
# logging.warning("программа умирает")

import os, platform, logging
if platform.platform().startswith('windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')
print("сохраняем лог в", logging_file)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w'
)
logging.debug('начало программы')
logging.info('какие-то действия')
logging.warning('программа умирает')

# # модуль sys
# import sys, warnings
# if sys.version_info[0] < 3:
#     warnings.warn("для выполнения этой программы необходима как минимум версия python 3.0", RuntimeWarning)
# else:
#     print("нормальное предложение")


import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn('для выполнения этой программы необходима как минимум версия python 3.0", RuntimeWarning')
else:
    print('нормальное предложение')

# # оператор with
# with open("poem.txt") as f:
#     for line in f:
#         print(line, end='      ')
#

# with open("poem.txt") as f:
#     for line in f:
#         print(line, end='    ')


# # Try .. Finally
# import time
# try:
#     f = open('poem.txt')
#     while True:
#         line = f.readline()
#         if len(line) == 0:
#             break
#         print(line, end=' ')
#         time.sleep(2)
# except KeyboardInterrupt:
#     print('!! вы отменили чтение файла.')
# finally:
#     f.close()
#     print('(отчистка: закрытые файла)')

import time
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='   ')
        time.sleep(2)
except KeyboardInterrupt:
    print('!! вы отменили чтение файла.')
finally:
    f.close()
    print('(отчистка: закрытые файла)')






# # вызов исключения
# class shortinputException(Exception):
#     '''пользовательский класс исключения.'''
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
# try:
#     text = input('введите что-нибудь --->')
#     if len(text) < 3:
#         raise shortinputException(len(text), 3)
# except EOFError:
#     print("ну зачем вы мне сделали EOF?")
# except shortinputException as ex:
#     print('ShortinputException: длина введенной строки -- {0}; ожидалось , как минимум, {1}'.format(ex.length, ex.atleast))
# else:
#     print('не было исключении.')


# # обработка искючений
# try:
#     text = input("введите что - нибудь --- > ")
# except EOFError:
#     print('ну зачем вы сделали мне EOF?')
# except KeyboardInterrupt:
#     print('вы отменили операцию.')
# else:
#     print('вы ввели {0}'.format(text))




# # pickle
# import pickle
# # имя файла в котором мы сохраним обьект
# shoplistfile = "shoplist.data"
# # список покупок
# shoplist = ["яблоки", "манго", "морковь"]
# # запись в файла
# f = open(shoplistfile, 'wb')
# pickle.dump(shoplist, f) #помещаем обьекта в файл
# f.close()
# del shoplist # уничтажаем переменную shoplist
# # считываем из хранилища
# f = open(shoplistfile, 'rb')
# shoplist = pickle.load(f)
# # загружаем обьект из файла
# print(shoplist)


# # файлы
# poem = '''
# программировать весело.
# если работа скучна,
# чтобы придать ей веселый тон -
# исполбзуй python!
#
# '''
# f = open('poem.txt', 'w')
# f.write(poem)
# f.close()
# f = open('poem.txt')
# while True:
#     line = f.readline()
#     if len(line) == 0:
#         break
#     print(line, end=' ')
# f.close()
#


# # ввод-вывод
# def reverse(text):
#     return text[::-1]
# def is_palindrrome(text):
#     return text == reverse(text)
# something = input("введите текст: ")
# if (is_palindrrome(something)):
#     print("да, это палиндром")
# else:
#     print("нет, это не палиндром")


# class SchoolMember:
#     '''представляет любого человека в школе.'''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('(создан SchoolMember: {0}'.format(self.name))
#     def tell (self):
#         '''вывести информация.'''
#         print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")
# class Teacher(SchoolMember):
#     '''представляет преподавателя.'''
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.salary = salary
#         print('(Создан Teacher: {0})'.format(self.name))
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Зарплата:"{0:d}"'.format(self.salary))
# class Student(SchoolMember):
#     '''Преставляет студента.'''
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('(Создан Student: {0}'.format(self.name))
#     def tell(self):
#         SchoolMember.tell(self)
#         print('оценка:"{0:d}"'.format(self.marks))
# t = Teacher('Mrs.Shrividay', 40, 30000)
# s = Student('Swaroop', 25, 75)
# print()
# members = [t, s]
# for members in members:
#     members.tell()




# # переменные класса и объекта
# class Robot:
#     '''Представляет робота с именем.'''
# #     переменная класса , содержащая количество роботов
#     population = 0
#     def __init__(self, name):
#         '''Инициализация данных.'''
#         self.name = name
#         print('(Инициализация {0})'.format(self.name))
# #         при создания этой личности, робот добавляется к переменной 'population'
#         Robot.population += 1
#     def __del__(self):
#         '''Я умираю.'''
#         print('{0} уничтожается!'.format(self.name))
#         Robot.population -= 1
#         if Robot.population == 0:
#             print('{0} был последним.'.format(self.name))
#         else:
#             print('Осталось {0:d} работающих роботов.'.format(Robot.population))
#     def sayHi(self):
#         '''приветствие робота.
#
#         да , они это могут.'''
#         print('приветствую! мои хозяева называют меня {0}.'.format(self.name))
#     def howMany():
#         '''выводит численность роботов.'''
#         print('у нас {0:d} роботов.'.format(Robot.population))
#     howMany = staticmethod(howMany)
# droid1 = Robot('R2-D2')
# droid1.sayHi()
# Robot.howMany()
#
# droid2 = Robot('C-3PO')
# droid2.sayHi()
# Robot.howMany()
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
# print("роботы закончили свою работы. Дайте уничтожим их.")
# del droid1
# del droid2
# Robot.howMany()


# #  метод ____init___
# class Person:
#      def __init__(self, name):
#          self.name = name
#      def say_hi(self):
#          print("привет! меня зовут", self.name)
# p = Person('Swaroop')
# p.say_hi()



# # классы
# class Person:
#     def sayHi(self):
#         print("привет ! как дела?")
# p = Person()
# p.sayHi()


# # еще о строках
# name = "Swaroop"
# if name.startswith("Swa"):
#     print('да, строки начинается на "Swa"')
# if 'a' in name:
#     print('да, она содержит строку "a"')
# if name.find('war') != -1:
#     print('да, она содержит строки "war"')
# delimiter = '_*_'
# mylist = ['бразилия', 'россия', 'индия', 'китай']
# print(delimiter.join(mylist))




# # ссылка
# print("простые присваивание")
# shoplist = ["яблоки", "манго", "морковь", "бананы"]
# mylist = shoplist
# del shoplist[0]
# print("shoplist:", shoplist)
# print("mylist:", mylist)
# print("копирование при помощи полной вырезки")
# mylist = shoplist[:]
# del mylist[0]
# print("shoplist:", shoplist)
# print("mylist:", mylist)



# # последовательности
# shoplist = ["яблоки", "манго", "морковь", "бананы"]
# name = "swaroop"
# # операция индексирования
# print("элемент 0 -", shoplist[0])
# print("элемент 1 -", shoplist[1])
# print("элемент 2 -", shoplist[2])
# print("элемент 3 -", shoplist[3])
# print("элемент -1 -", shoplist[-1])
# print("элемент -2 -", shoplist[-2])
# print("элемент 0 -", shoplist[0])
# # вырезка из списка
# print("элементы с 1 по 3:", shoplist[1:3])
# print("элементы с 2 до конца:", shoplist[2:])
# print("элементы с 1 по -1:", shoplist[1:-1])
# print("элементы от начала до конца:", shoplist[:])
# # вырезка из строки
# print("символы с 1 по 3:", name[1:3])
# print("символы  с 2 до конца:", name[2:])
# print("символы с 1 по -1:", name[1:-1])
# print("символы от начала до конца:", name[:])


# # словарь
# # "ab" - сокращение от "a"ddress"b"ook
# ab = {
#     "swaroop"  : "swaroop@swaroopch.com",
#     "larry"    : "larry@wall.org",
#     "matsumoto": "matz@ruby-lang.org",
#     "spammer"  : "spammer@hotmail.com"
# }
# print("адрес swaroop'a:", ab["swaroop"])
# # удаленные пары ключ-значение
# del ab["spammer"]
# print("\nв адресной книге {} контакта\n".format(len(ab)))
# for name, address in ab.items():
#     print("контакт {0} с адресом {1}".format(name, address))
# #     добавление пары ключ-значение
# ab["Guido"] = "guido@python.org"
# if 'Guido' in ab:
#     print("\nадрес  Guido:", ab["Guido"])

# # кортеж
# zoo = ("питон", "слон", "пингвин")
# print("количество животных в зоопарке -", len(zoo))
# new_zoo = "обезьяна", "верблюд", zoo
# print("количество клеток в зоопарке -", len(new_zoo))
# print("все животные в новом зоопарке:", new_zoo)
# print("последнее животное, привезенное из старого зоопарка -", new_zoo[2][2])
# print("количество животных в новом зоопарке -", len(new_zoo)-1 + len(new_zoo[2]))



# # мой список покупок
# shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
#
# print("я должен сделать", len(shoplist), 'покупки.')
#
# print("покупки:", end=" ")
# for item in shoplist:
#     print(item, end=" ")
#
# print("\nтакже нужно купить риса.")
# shoplist.append("рис")
# print("теперь мой список покупок таков:", shoplist)
#
# print("отсортирую-ка я свой список")
# shoplist.sort()
# print("отсортированный список покупок выглядит так:", shoplist)
#
# print("первое что мне нужно купить, это", shoplist[0])
# olditem = shoplist[0]
# del shoplist[0]
# print("я купил", olditem)
# print("теперь мой список покупок:", shoplist)


# # создание собственных модулей
# def sayhi():
#     print("привет! это говорит мой модуль.")
#


# # имя модулья -__name__
# if __name__ == '__main__':
#     print("это программа запущен сама по себе. ")
# else:
#     print("меня импортировали в другой модуль ")



# # оператор from ... import...
# from math import *
# n = int(input("введите диапозон:- "))
# p = [2, 3]
# a = 5
# while (count < n):
#     b = 0
#     for i in range(2, a):
#         if (i <= sqrt(a)):
#             if (a % i == 0):
#                 print(a, "непростое")
#             else:
#                 pass
#     if (b != 1):
#         print((a, "простое"))
#         p = p + [a]
#     count = count + 1
#     a = a + 1
# print(p)



# # модули
# import sys
# print("аргументы командной строки:")
# for i in sys.argv:
#     print(i)
# print("\n\nпеременная PYTHONPATH содержит", sys.path, "\n")




# # строки документации
# def printMax(x, y):
#     '''выврдите максимальное из двух чисел.
#     оба значение должны быть целыми числами.'''
#     x = int(x)
#     y = int(y)
#     if x > y:
#         print(x, "натбольше")
#     else:
#         print(y, "наибольше")
# printMax(3, 5)
# print(printMax.__doc__)


# # оператор  return
# def maximum(x, y):
#     if x > y:
#         return x
#     elif x == y:
#         return "число равны."
#     else:
#         return y
# print(maximum(5, 3))



# # только ключевые параметры
# def total(initial=5, *numbers, extra_number):
#     count = initial
#     for number in numbers:
#         count += number
#     count += extra_number
#     print(count)
# total(10, 1, 2, 3, extra_number=50)
# total(10, 1, 2, 3)



# # переменное число параметров
# def total(a=5, *numders, **phonebook):
#     print("a", a)
#     for single_item in numders:
#         print("single_item", single_item)
#     for first_part, second_part in phonebook.items():
#         print(first_part, second_part)
# print(total(10, 1, 2, 3, jack=1123, john=2231, inge=1560))


# # ключевые аргументы
# def func(a, b=5, c=10):
#     print("a равно", a, ", b равно", b, ", a c равно", c)
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)



# # значения аргументов по умолчанию
# def say(message, times = 1):
#     print(message * times)
# say("привет")
# say("мир", 7)



# #  зарезервирование слово "nonlocal"
# def func_outer():
#     x = 2
#     print("x равно", x)
#     def func_inner():
#         nonlocal x
#         x = 5
#     func_inner()
#     print("локальное x сменилось на", x)
# func_outer()



# # зарезервированноу слово "global"
# x = 50
# def func():
#     global x
#     print("x равно", x)
#     x = 2
#     print("замена глобальное значение", x)
# func()
# print("значение x составяет", x)


# # локальные переменные
# x = 50
# def func(x):
#     print("x равен", x)
#     x = 2
#     print("замена локального x на", x)
# func(x)
# print("x по-прежнему", x)


# # параметры функции
# def printMax(a, b):
#     if a > b:
#         print(a, "максимально")
#     elif a == b:
#         print(a, "равно", b)
#     else:
#         print(b, "максимально")
# printMax(3, 4)
# x = 5
# y = 7
# printMax(x, y)



# # фунции
# def sayHello():
#     print("привет, мир")
# sayHello()
#
# sayHello()


# # оператор continue
# while True:
#     s = input("введите что-нибудь : ")
#     if s == "выход":
#         break
#     if len(s) < 3:
#         print("слишком мало")
#         continue
#     print("введеннфя строка достаточной длины")



# # оператор break
# while True:
#     s = input("введите что- нибудь : ")
#     if s == "выход":
#         break
#     print("длина строки :", len(s))
# print("завершение")



# # цикл for
# for i in range(1, 5):
#     print(i)
# else:
#     print("цикл for закончен")



# # оператор while
# number = 23
# running = True
# while running:
#     guess = int(input("введите целое число : "))
#     if guess == number:
#         print("поздравляю, вы угадали.")
#         running = False
#     elif guess < number:
#         print("нет, загаданное число больше этого.")
#     else:
#         print("нет, загаданное число немного меньше этого.")
# else:
#     print("цикл while закончен.")
# print("завершение")



# if True:
#     print("да, это верно")


# # оператор if
# number = 23
# guess = int(input("ведите целое число :"))
# if guess == number:
#     print("поздравляю, вы угадали, ")
#     print("(хотя и не выиграли никакого приза!)")
# elif guess < number:
#     print("нет, загаданное число немного больше этого.")
# else:
#     print("нет, загаданное число немного меньше этого.")
# print("завершвно")



# # выражения
# length = 5
# breadth = 2
# area = length * breadth
# print("площадь равна", area)
# print("периметр равен", 2 * length + breadth)



# # разбиение на фрагменты
# def chunk(my_list, size):
#     return [my_list[i:i + size] for i in range(0, len(my_list), size)]
# my_list = [1, 2, 3, 4, 5, 6]
# print(chunk(my_list, 2))



# # печать в ондой строке
# # fastest way
# import sys
# sys.stdout.write("call of duty")
# sys.stdout.write(" and black Ops ")
# print("Python", end=" ")
# print("programming")



# # поиск подстроки
# programmers = [
#     "I'm an expert Python Programmer",
#     "I'm an expert JavaScript Programmer",
#     "I'm an expert C++ Programmer",
# ]
# for p in programmers:
#     if p.find("Python"):
#         print(p)
# # # вариант2
# for p in programmers:
#     if "Python" in p:
#         print(p)


# # форматирование строки
# str1 = "python programming"
# str2 = "I'm a {}".format(str1)
# print(str2)
# # вариант2
# str1 = "python programming"
# str2 = f"I'm a {str1}"
# print(str2)



# # преобразование строк в верхном и нижном регистре
# str1 = "python programming"
# str2 = "IM A PROGRAMMER"
# print(str1.upper())
# print(str2.lower())



# # перемешение списка
# from random import shuffle
# my_list1 = [1, 2, 3, 4, 5, 6]
# my_list2 = ["a", "b", "c", "d"]
# shuffle(my_list1)
# shuffle(my_list2)
# print(my_list1)
# print(my_list2)


# # проверка палиндрамов
# def palindrome(data):
#     return data == data[::-1]
# print(palindrome("level"))
# print(palindrome("madaa"))



# # преобразование разделенного запятыми списка в строку
# my_list1 = ["python", "javascript", "c++"]
# my_list2 = ["java", "flutter", "swift"]
# print("my favourite programming languages are", ", ".join(my_list1))
# print(", ".join(my_list2))
# print(my_list2)



# # получение последнего элемента списка
# my_list = ["python", "javaScript", "c++", "java", "c#", "Dart"]
# # вариант1
# print(my_list[-1])
# # вариант2
# print(my_list.pop())
#

# # сортировка словаря
# orders = {
#     'pizza': 200,
#     'burger': 56,
#     'pepsi': 25,
#     'coffee': 14
# }
# sorted_dic = sorted(orders.items(), key=lambda x: x[1])
# print(sorted_dic)


# # сортировка списка
# my_list = ["leaf", "cherry", "fish"]
# my_list1 = ["d", "c", "b", "a"]
# my_list2 = [1, 2, 3, 4, 5]
#
# print(my_list.sort())
# print(my_list1.sort())
# print(sorted(my_list2, reverse=True))


# # анаграммы
# from collections import Counter
# def anagrams(str1, str2):
#     return Counter(str1) == Counter(str2)
# print(anagrams("abc1", "1bac"))



# # занятая память
# import sys
# var1 = "python"
# var2 = 100
# var3 = True
# print(sys.getsizeof(var1))
# print(sys.getsizeof(var2))
# print(sys.getsizeof(var3))


# размер в байтах
# def ByteSize(string):
#     return len(string.encode("utf8"))
# print(ByteSize("Python"))
# print(ByteSize("Data"))


# # фильтрация значений False
# def filtering(lst):
#     return list(filter(None, lst))
# lst = [None, 1, 3, 0, "", 5, 7]
# print(filtering(lst))


# # проверка дудбликатов
# def chek_duplicate(lst):
#     return len(lst) != len(set(lst))
# print(chek_duplicate([1, 2, 3, 4, 5, 4, 6]))
# print(chek_duplicate([1, 2, 3]))
# print(chek_duplicate([1, 2, 3, 4, 9]))


# # обмен значений между переменными
# a = 3
# b = 4
# a, b = b, a
# print(a, b)

# # вычисляем время выполнения
# import time
# start_time = time.time()
# def fun():
#     a = 2
#     b = 3
#     c = a + b
# end_time = time.time()
# fun()
# timetaken = end_time - start_time
# print("your program takes: ", timetaken)

# #  получаем гласные
# def get_vowels(String):
#     return [each for each in String if each in "aeiou"]
# print(get_vowels("animal"))
# print(get_vowels("sky"))
# print(get_vowels("football"))

# # обьединяем два словаря
# def merge(dic1, dic2):
#     dic3 = dic1.copy()
#     dic3.update(dic2)
#     return dic3
# dic1 = {1:"hello", 2:"world"}
# dic2 = {3:"python", 4:"programming"}
# print(merge(dic1, dic2))
# печатать строки
# n = 5
# string = "hello world"
# print(string * n)


# file = open('text.txt', 'r')
#
# file.close()

# from random import choice
# from datetime import  datetime
# from time import  sleep
#
# start = datetime.now()
# print(start)
# sleep(0.000000000000001)
# print((datetime.now() - start).seconds)
# print(datetime.now())

# from random import choice
# from datetime import datetime
# from time import sleep

#                таймер
# def timer (seconds):
#     while seconds != 0:
# #         sleep(1)
# #         print(seconds)
# #         seconds -= 1
# # timer(10)

# asked = []
# students = [2, 3, 4, 5, 8, 12, 13, 14, 15, 16, 17, 18, 19, 21]
#
# while len(students) != 0:
#     student = students.pop(students.index(choice(students)))
#     answer = input(f'отвечает студент под номером {student} ')
#     asked.append(student)
#     print(students)
#     print(asked)



# from joji7_1 import greeting as g
# import random
# from random import randint, choice, sample
# from random import randrange as r
#             вывод из списка
# names = ['azat', 'ruslan', 'medina']
# g(choice(names))


# print(r(1, 10, 4))
# print(r(1, 10, 4))


# lst = ['a', 'b', 'c', 'd']
# print(sample(lst, 3))
# print(choice(lst))
# print(random.choice(lst))

# print(random.randint(1, 5))
# print(randint(1, 5))from random import choice
# from datetime import  datetime
# from time import  sleep
#
# # start = datetime.now()
# # print(start)
# # sleep(0.000000000000001)
# # print((datetime.now() - start).seconds)
# # print(datetime.now())
#
# #                таймер
# # def timer (seconds):
# #     while seconds != 0:
# #         sleep(1)
# #         print(seconds)
# #         seconds -= 1
# # timer(10)
#
#
#
# asked = []
# students = [2, 3, 4, 5, 8, 12, 13, 14, 15, 16, 17, 18, 19, 21]
#
# while len(students) != 0:
#     student = students.pop(students.index(choice(students)))
#     answer = input(f'отвечает студент под номером {student} ')
#     asked.append(student)
#     print(students)
#     print(asked)
#
#
# # from joji7_1 import greeting as g
# # import random
# # from random import randint, choice, sample
# # from random import randrange as r
# #             вывод из списка
# # names = ['azat', 'ruslan', 'medina']
# # g(choice(names))
#
#
# # print(r(1, 10, 4))
# # print(r(1, 10, 4))
#
#
# # lst = ['a', 'b', 'c', 'd']
# # print(sample(lst, 3))
# # print(choice(lst))
# # print(random.choice(lst))
#
# # print(random.randint(1, 5))
# # print(randint(1, 5))from random import choice
# from datetime import  datetime
# from time import  sleep
#
# # start = datetime.now()
# # print(start)
# # sleep(0.000000000000001)
# # print((datetime.now() - start).seconds)
# # print(datetime.now())
#
# #                таймер
# # def timer (seconds):
# #     while seconds != 0:
# #         sleep(1)
# #         print(seconds)
# #         seconds -= 1
# # timer(10)
#
#
#
# asked = []
# students = [2, 3, 4, 5, 8, 12, 13, 14, 15, 16, 17, 18, 19, 21]
#
# while len(students) != 0:
#     student = students.pop(students.index(choice(students)))
#     answer = input(f'отвечает студент под номером {student} ')
#     asked.append(student)
#     print(students)
#     print(asked)
#
#
# # from joji7_1 import greeting as g
# # import random
# # from random import randint, choice, sample
# # from random import randrange as r
# #             вывод из списка
# # names = ['azat', 'ruslan', 'medina']
# # g(choice(names))
#
#
# # print(r(1, 10, 4))
# # print(r(1, 10, 4))
#
#
# # lst = ['a', 'b', 'c', 'd']
# # print(sample(lst, 3))
# # print(choice(lst))
# # print(random.choice(lst))
#
# # print(random.randint(1, 5))
# # print(randint(1, 5))from random import choice
# from datetime import  datetime
# from time import  sleep
#
# # start = datetime.now()
# # print(start)
# # sleep(0.000000000000001)
# # print((datetime.now() - start).seconds)
# # print(datetime.now())
#
# #                таймер
# # def timer (seconds):
# #     while seconds != 0:
# #         sleep(1)
# #         print(seconds)
# #         seconds -= 1
# # timer(10)
#
#
#
# asked = []
# students = [2, 3, 4, 5, 8, 12, 13, 14, 15, 16, 17, 18, 19, 21]
#
# while len(students) != 0:
#     student = students.pop(students.index(choice(students)))
#     answer = input(f'отвечает студент под номером {student} ')
#     asked.append(student)
#     print(students)
#     print(asked)
#
#
# # from joji7_1 import greeting as g
# # import random
# # from random import randint, choice, sample
# # from random import randrange as r
# #             вывод из списка
# # names = ['azat', 'ruslan', 'medina']
# # g(choice(names))
#
#
# # print(r(1, 10, 4))
# # print(r(1, 10, 4))
#
#
# # lst = ['a', 'b', 'c', 'd']
# # print(sample(lst, 3))
# # print(choice(lst))
# # print(random.choice(lst))
#
# # print(random.randint(1, 5))
# # print(randint(1, 5))from random import choice
# from datetime import  datetime
# from time import  sleep
#
# # start = datetime.now()
# # print(start)
# # sleep(0.000000000000001)
# # print((datetime.now() - start).seconds)
# # print(datetime.now())
#
# #                таймер
# # def timer (seconds):
# #     while seconds != 0:
# #         sleep(1)
# #         print(seconds)
# #         seconds -= 1
# # timer(10)
#
#
#
# asked = []
# students = [2, 3, 4, 5, 8, 12, 13, 14, 15, 16, 17, 18, 19, 21]
#
# while len(students) != 0:
#     student = students.pop(students.index(choice(students)))
#     answer = input(f'отвечает студент под номером {student} ')
#     asked.append(student)
#     print(students)
#     print(asked)
#
#
# # from joji7_1 import greeting as g
# # import random
# # from random import randint, choice, sample
# # from random import randrange as r
# #             вывод из списка
# # names = ['azat', 'ruslan', 'medina']
# # g(choice(names))
#
#
# # print(r(1, 10, 4))
# # print(r(1, 10, 4))
#
#
# # lst = ['a', 'b', 'c', 'd']
# # print(sample(lst, 3))
# # print(choice(lst))
# # print(random.choice(lst))
#
# # print(random.randint(1, 5))
# # print(randint(1, 5))from random import choice
# from datetime import  datetime
# from time import  sleep
#
# # start = datetime.now()
# # print(start)
# # sleep(0.000000000000001)
# # print((datetime.now() - start).seconds)
# # print(datetime.now())
#
# #                таймер
# # def timer (seconds):
# #     while seconds != 0:
# #         sleep(1)
# #         print(seconds)
# #         seconds -= 1
# # timer(10)
#
#
#
# asked = []
# students = [2, 3, 4, 5, 8, 12, 13, 14, 15, 16, 17, 18, 19, 21]
#
# while len(students) != 0:
#     student = students.pop(students.index(choice(students)))
#     answer = input(f'отвечает студент под номером {student} ')
#     asked.append(student)
#     print(students)
#     print(asked)
#
#
# # from joji7_1 import greeting as g
# # import random
# # from random import randint, choice, sample
# # from random import randrange as r
# #             вывод из списка
# # names = ['azat', 'ruslan', 'medina']
# # g(choice(names))
#
#
# # print(r(1, 10, 4))
# # print(r(1, 10, 4))
#
#
# # lst = ['a', 'b', 'c', 'd']
# # print(sample(lst, 3))
# # print(choice(lst))
# # print(random.choice(lst))
#
# # print(random.randint(1, 5))
# # print(randint(1, 5))


# from joji7_1 import greeting as g
# import random
# from random import randint, choice, sample
# from random import randrange as r
#             вывод из списка
# names = ['azat', 'ruslan', 'medina']
# g(choice(names))


# print(r(1, 10, 4))
# print(r(1, 10, 4))


# lst = ['a', 'b', 'c', 'd']
# print(sample(lst, 3))
# print(choice(lst))
# print(random.choice(lst))

# print(random.randint(1, 5))
# print(randint(1, 5))



# def greeting(name):
#     print(f'hello, {name}')
# # greeting('alan')


# while True:
#     try:
#         first_number = int(input('видите числа:'))
#         answer = input('введите знак: + - * / ')
#         second_number = int(input('Введите второе число :'))
#     except:
#         print('Идите числа!')
#         continue
#     if answer == "+":
#         print(first_number + second_number)
#     elif answer == "-":
#         print(first_number - second_number)
#     elif answer == "*":
#         print(first_number * second_number)
#     elif answer == "/":
#         print(first_number / second_number)
#     elif first_number == "0":
#         print('Программа завершилась')
#         break
#     else:
#         print('Или что-то не так!')
# words = ['pythom', 'oop', 'type']
#
# position = input('выведите индекс:')
# try:
#     words[position]
# except IndexError:
#     print('ой до часа нет')
# except TypeError:
#     print('Эти числа')



# numbers = [1, 2, 3, 4, 5, 6]
# words = ['apple', 'green', 'top', 'python']
# a = list(filter(lambda x: len(x) <= 3, words))

# print(a)
# c = 0
# while c ! = len(numbers - 1):
# b = list(map(lambda x: x.upper(), words))
# print(b)


# b = list(map(lambda x: x + 5, numbers))
# print(b)

# lst = ['world', 'python', 'apple']
# # def upletter(lst):
# #     for i in lst:
# #          print(i.title())
# # upletter(lst)
# up = lambda x: x.title()
# print (up(lst))


# lst = ['world', 'python', 'apple']
# def upletter(lst):
#     for i in lst:
#         return i.title()
# print(upletter(lst))


# def plus (x, y):
#     return x + y
# print(plus(2, 3))


# plus_l = lambda x, y: x + y
# print(plus_l(2, 3))





# a = [1, 2, 3, 4, 5]
# a5 = []
# def plus_each(lst, fn):
#     for i in lst:
#         a5.append(i + fn)
#
# plus_each(a, plus(2, 3))
# print(a5)


# numbers = [1, 2, 3, 4, 5]
# letters = ['a', 'b', 'c', 'd', 'e']
# words = {}
#
# c = 0
# # while True
# while c != len(numbers):
#
#     words[numbers[c]] = letters[c]
#     print(words)
#     c += 1
#





# univer = []
# tehnikum = []
# army = []
# abiturient = [
#     {'name': "akulai",'ОРТ': 105, 'gender': 'female'},
#     {'name': "dastan", 'ОРТ': 120, 'gender': 'male'},
#     {'name': "meerim", 'ОРТ': 99, 'gender': 'female'},
#     {'name': "askar", 'ОРТ': 0, 'gender': 'male'}
#
# ]
#
# def all_abiturients(lst):
#     for i in lst:
#         for k,v in i.items():
#             print(f'{k}: {v}')
#         print(' ')
#
# all_abiturients(abiturient)
#
# def seleccion(lst, u, t, a):
#     for i in lst:
#         if i['ОРТ'] >= 105:
#             u.append(i)
#         elif i['ОРТ'] < 105 and i['ОРТ'] > 0:
#             t.append(i)
#         elif i['ОРТ'] == 0 and i['gender'] == 'male':
#             a.append(i)
# seleccion(abiturient, univer, tehnikum, army)
#
# print('u', univer)
# print('t', tehnikum)
# print('a', army)



# def menu(**kwargs):
#     return kwargs
#
# monday = menu(breakfast='яичница', lunch='бифштекс', dinner='пельмени')
# print(monday)


# def numbers(*args):
#     # print(args)
#     # print(a)
#     return sum(args) / len(args)
#
# print(numbers(24, 20, 19, 25, 20))


# def square(a, b, c=4):
#     # print(a + b + c)
#     return a +  b + c
#
# # square(int(input('ширина?:')), int(input('высота?:')))
# # our = square(7, 3, 5)
# print(square(4, 6, 5) + square(10, 3, 5))
# # print(type(our))


# nominal = [20, 50, 100, 200, 500, 1000, 2000, 5000]
# persons = [
#     "T.M", "K.D", "T.S", "A.O", \
#     "C.K", "B", "m", "C.CH"
# ]
#
# banknotes = dict(zip( nominal, persons ))
# for i,l in banknotes.items():
#     print (f'{i} : {l}')
#
# print (banknotes)
#
# next_month = []





# next_moth = []
# data = [
#     {
#         'name': 'adilet',
#         'points': 40,
#         'test': 60,
#         'stanUp': True
#
#      },
#     {
#         'name': 'adilet',
#         'points': 40,
#         'test': 60,
#         'stanUp': True
#     },
# ]
# c = 0
# while c != len(data):
#     for i in data:
#         c += 1
#         # for k in i:
#         if i['points'] >= 40 and i['test'] >= 60 and i['stanUp'] == True:
#             next_moth.append(i)
#         else:
#             print(i['name'], 'не проходит!')
# print(next_moth)


# plov = {"мясо", "рис", "морковь"}
# kuurdak = {'мясо', 'картофель', 'лук'}
# print(plov.intersection(kuurdak))
# print(plov & kuurdak)
# print(plov.difference(kuurdak))
# print(plov - kuurdak)
# print(plov.symmetric_difference(kuurdak))
# print(plov ^ kuurdak)
# print(plov.union(kuurdak))
# print(plov | kuurdak)


# a = [1, 2, 3, 1, 3]
# set()
# set_1 = {'abc', 'oop', 'abc'}
# print(set_1)
# print(a)


# studen = {
#     'key': 'john',
#     'age': '20',
#     'phone': ['0555111333', '0700112233'],
#     2: 'id'
#
# }
# studen2 = {
#     'key': 'john',
#     'age': '20',
#     'phone': ['0555111333', '0700112233'],
#     'instagram': 'johny777'
#
#
# }
# for key, value in studen.items():
#     print(f'{key}: {value}')

# for value in studen.values():
#     print(f'{value}')


# print(studen.values())
# print(studen.keys())
#
# print(studen.items)


#
# print(studen['phone'][2][1])
# studen['age'] = 21
# studen['height'] = 1.76
# # del studen[2]
# # studen.pop(2)
# del studen['phone'][0]
# print(studen)

# print(studen['name'])
# print(studen['phone'][1])


# name = input('name')
# age = input('age')
# lst = []
# lst.append(name)
# lst.append(age)
#
# print(lst)

# ru = 'белый', 'синий', 'красный'
# gr = 'черный', 'красный', 'желтый'
#
# ourcolors = []
# while len(ourcolors) != 3:
#     clrs = input('ведите цвет!')
#     ourcolors.append(clrs)
#     print(clrs)
#
# if tuple(ourcolors) == ru:
#     print("это флаг России")
# elif tuple(ourcolors) == gr:
#     print("это флаг Германии")
# else:
#     print("эти цвета не совпадают с РФ или Германии")
# a = [1, 2, 3, 4, 5]
# colors = 'red', 'white', 'green'
# print('red' in colors)
# print('red' not in colors)
# print('white' in colors)


# nominal = (1, 3, 5, 10, 20, 100, 200, 500, '1k', '2k', '5k', 1)
# a = [1, 2, 3, 4, 5]
# tpl = tuple(a)
# print(tpl)
# tpl = list(tpl)
# print(tpl)

# nominal = (1, 3, 5, 10, 20, 100, 200, 500, '1k', '2k', '5k', 1)
# tpl = tuple("abcde")
# names = "adil", "adios", "max"
# red, white, blue = 'colors', 'colors', 'colors'
# # print(nominal.count(1))
# # print(nominal.index(1))
#
# a, b = 1, 2
# print(a)
# print(b)
# print(red)
# print(white)
# print(blue)
#

# data_types = ['hello', 'name', 123, 5, True, False, 2.5, 3.9]
# strings = list()
# while len(strings) != 5:
#     word = input("enter something")
#     strings.append(word)
#     print(strings)s
# print(strings)
# for i in range(1, 5+1):
#     strings.append(i)
# print(strings)
# print(len(data_types))
# # for i in data_types:
# #     # if i == 'hello' or i == 'name':
# #     if type(i) == str:
# #         strings.append(i)
# #     else:
# #         print(i)
#
# print(data_types)
# print(strings)


# # создания списка
# data_types = ['hello', 'name', 123, 5, True, False, 2.5, 3.9]
# # пустой список
# strings = list('12345')
# data_types.append(strings)
# data_types.extend(strings)
# data_types += strings
# data_types[0] = 'goodbuy '
# #  вывод индекса
# print(data_types[7])

# # выводит отрезок списка
# print(data_types[0:4])
# # выводить отрезок через один шаг
# print(data_types[0:-1:2])

# # - отрезок можно присвоит к переменной
# strings.append(data_types[0:4])
# print(strings)

# data_types.append("abc")
# data_types.insert(1, 25)
# data_types.remove('name')
# deleted_obj = data_types.pop(-1)
# strings.append(data_types.pop(-1))
# strings.append(data_types.pop(-2))
# del data_types[0], data_types[3],
# print(strings)
# print(data_types)
# for letter in "django":
#     if letter == "g" or letter == "d":
#         continue
#     print("curent letter:" + letter)
# print("finish")




# rounds = 0
# while 1:
#     rounds += 1
#     print(rounds)
#     # if rounds == 3:
#     #     print("next")
#     #     continue
#     if rounds == 5:
#         print("stop")
#         break



# apples = 10
# good_aplles = 0
# bad_apples = 0
#
#
# while apples != 0:
#     apples -= 1
#     answer = input("good or bad")
#     if answer == "good":
#         good_aplles += 1
#     else:
#         bad_apples += 1
#     print("apples: {}".format(apples))
#     print("good: {}".format(good_aplles))
#     print("bad: {}".format(bad_apples))


# while True:
#     color = input("введите цвет сфетофора:")
#     if color == "red":
#         print("stop")
#     elif color == "green":
#         print("go")
#     else:
#         print("look an situation")
#         break


# for i in range(1, 5):
#     print(i, end=' ')

# counter = 0
# while counter != 10:
#     counter += 1
#     print(counter, end='_')

# color = "off"
# if color == "red":
#     print("stop")
# elif color == "green":
#     print("go")
# else:
#     print("look at situation")


# day = int(input("день рождения: "))
# month = int(input("месяц рождения: "))
#
#
# if day >= 21 and day <= 31 and month == 3 or 0 > day <= 20 and month == 4:
#     print("овень (21 марта - 20 апрель)")

# print(0 or 5  or -3 and 5)


# for letter in 'django':
#     if letter == 'g' or letter == 'd':
#         continue
#
#     print('current letter: ' + letter)
# print(letter)



#
# a = dict(zip('abcdef', list(range(6))))
# for key, val in a.items():
#     print(key, val)



# a = dict(zip('abcdef', list(range(6))))
# for key in a:
#     print(key, a[key])


# a = {'ab': 'ba', 'aa': 'aa', 'bb': 'bb', 'ba': 'ab'}
#
# key = 'ac'
# if key in a:
#     del a[key]
#
# try:
#     del a[key]
# except KeyError:
#     print('There is no element with key "' + key + '" in dict')
# print(a)


# capitals = {'Rassia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
# capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')
# capitals = dict([('Russia', 'Moscow'), ('Ukraine', 'kiev'),('USA', 'Washington')])
# capitals = dict(zip(['Russia', 'Ukraine', 'USA'], ['Moscow', 'Kiev', 'Washington']))
# print((capitals))


# capitals = dict()
# capitals['Russia'] = 'Moscow'
# capitals['Ukraine'] = 'kiev'
# capitals['USA'] = 'Washington'
#
# countries = ['Russia', 'France', 'USA', 'Russia']
#
# for country in countries:
#     if country in capitals:
#         print('столица страны ' + country + ': ' + capitals[country])
#     else:
#         print('в базе нет страны с названем ' + country)



# a = {1, 2, 3}
# print(1 in a, 4 not in a)
# a.add(4)


# primes = {2, 3, 5, 7, 11}
# for num in primes:
#     print(num)



# a = {1, 2, 3}
# b = {3, 2, 3,  1}
# print(a == b)



# A = {1, 2, 3}
# A = set('qwerty')
# print(A)



# n = 4
# a = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]
# for row in a:
#     print(' '.join([str(elem) for elem in row]))




# n = 4
# a = [0] * n
# for i in range(n):
#     a[i] = [2] * i + [1] + [0] * (n - i - 1)
# for row in a:
#     print(' '.join([str(elem) for elem in row]))




# n = 4
# a = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(0, i):
#         a[i][j] = 2
#     a[i][i] = 0
# for row in a:
#     print(' '.join([str(elem) for elem in row]))



# for i in range(0):
#     a[i][i] = 1



# n = 4
# a = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i < j :
#             a[i][j] = 0
#         elif i > j:
#             a[i][j] = 2
#         else:
#             a[i][j] = 1
# for row in a:
#     print(' '.join([str(elem) for elem in row]))



# n = int(input())
# a = [[int(j) for j in input().split()] for i in range(n)]



# n = int(input())
# a = []
# for i in range(n):
#     row = input().split()
#     for i in range(len(row)):
#         row[i] = int(row[i])
#     a.append(row)



# n = int(input())
# a = []
# for i in range(n):
#     a.append([int(j) for j in input().split()])



# n = 3
# m = 4
# a = [[0] * m for i in range(n)]



# n = 3
# m = 4
# a = []
# for i in range(n):
#     a.append([0] * m)




# n = 3
# m = 4
# a = [0] * n
# for i in range(n):
#     a[i] = [0] * m



# n = 3
# m = 4
# a = [[0] * m] * n
# a[0][0] = 5
# print(a[1][0])


# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# s = 0
# for row in a:
#     for elem in row:
#         s += elem
#
# print(s)



# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# s = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         s += a[i][j]
# print(s)



 # ????for row in a:
 #    print(' '.ljust([str(elem) for elem in row]))



# a =[[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for row in a:
#     for elem in row:
#         print(elem, end=' ')
#     print()



# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()



# a = [[1, 2, 3], [4, 5, 6]]
# print(a[0])
# print(a[1])
# b = a[0]
# print(b)
# print(a[0][2])
# a[0][1] = 7
# print(a)
# print(b)
# b[2] = 9
# print(a[0])
# print(b)



# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))



# def short_story():
#     print("у попа была собака, он ее любил.")
#     print("она съела кусок мяса, он ее убил,")
#     print("в землю закопал и надпись написал:")
#     short_story()
# #



# def factorial(n):
#     res = 1
#     for i in range(2, n + 1):
#         res *= i
#     return res
#
# n = int(input())
# f = factorial(n)



# def factorial(n):
#     global f
#     res = 1
#     for i in range(2, n + 1):
#         res *= i
#     f = res
#
# n = int(input())
# factorial(n)



# def f():
#     global a
#     a = 1
#     print(a)
# a = 0
# f()
# print(a)





# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
#
# for i in range(1, 6):
#     print(i, '! = ', factorial(i), sep='')



# def f():
#     a = 1
#     print(a)
# a = 0
# f()
# print(a)

# создали функцию
# def f():
# оставили функцию пустум
#     print(a)
# вызвали (а)
#
# a = 1
# потом (а) приравнили на (1)
# и вызвали функцию
# f()



# def max(*a):
#     res = a[0]
#     for val in a[1:]:
#         if val > res:
#             res = val
#     return res
# print(max(3, 5, 4))



# def max(a, b):
#     if a >b:
#         return a
#     else:
#         return b
# def max3(a, b, c):
#     return max(max(a, b), c)
#
# print(max3(3, 5, 4))



# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(max(3, 5))
# print(max(5, 3))
# print(max(int(input()), int(input())))


# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
#
# print(factorial(3))
# print(factorial(5))



# res = 1
# for i in range(1, 4):
#     res *= i
# print(res)
#
#
# res = 1
# for i in range(1, 6):
#     res *= i
# print(res)



# A = [1, 2, 3, 4, 5]
# A[2:4] = [7, 8, 9]


# сначала водиш цифру и потом можеш водить столько же
# a = [input() for i in range(int(input()))]



# from random import randrange
# n = 5
# a = [randrange(1, 10) for i in range(n)]



# n = 5
# a = [i ** 2 for i in range(1, n + 1)]



# n = 5
# a = [i ** 2 for i in range(n)]




# a = [0 for i in range(5)]


# n = 5
# a = [0] * n

# списки
# a = [1, 2, 3]
# print(' '.join([str(i) for i in a]))



# a = ['red', 'green', 'blue']
# print(' '.join(a))
# print(''.join(a))
# print('***'.join(a))


# a = '192.186.0.1'.split('.')



# a = [int(s) for s in input().split()]


# a = input().split()
# for i in range(len(a)):
#     a[i] = int(a[i])




# s = input()
# a = s.split()


# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)



# a = [1, 2, 3, 4, 5, ]
# for elem in a:
#     print(elem, end=' ')



# a = [1, 2, 3, 4, 5]
# for i in range(len(a)):
#     print(a[i])


# a = [0] * int(input())
# for i in range(len(a)):
#     a[i] = int(input())



# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# d = b * 3
# print([7, 8] + [9])
# print([0, 1] * 3)



# a = []
# for i in range(int(input())):
#     a.append(int(input()))
# print(a)



# a = []
# n = int(input())
# for i in range(n):
#     new_element = int(input())
#     a.append(new_element)
# print(a)



# Rainbow = ['Red', 'Orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# print(Rainbow[0])
# Rainbow[0] = 'красный'
# print('выведем радугу')
# for i in range(len(Rainbow)):
#     print(Rainbow[i])



# Primes = [2, 3, 5, 7, 11, 13]
# Rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']



# a = 1
# b = 2
# a, b = b, a
# print(a, b)



# a = 1
# b = 2
# tmp = a
# a = b
# b = tmp
# print(a, b)



# a, b = 0, 1
# print(a)
# print(b)


# n = int(input())
# print('длина списка равна', len(str(n)))



# n = int(input())
# length = 0
# while n != 0:
#     length += 1
#     n //= 10
# print('длина числа равна', length)



# n = int(input())
# length = 0
# while True:
#     length += 1
#     n //= 10
#     if n == 0:
#         break
# print('длина числа равна', length)



# for i in range(3):
#     for j in range(5):
#         if j > i:
#             break
#         print(i, j)



# n = int(input())
# for i in range(n):
#     a = int(input())
#     if a < 0:
#         print('встретилось отрицатильное число', a)
#         break
# else:
#     print('ни одного отрицатильного чилсо не встретилось')



# a = int(input())
# while a != 0:
#     if a < 0:
#         print('встретилось отрицателное число', a)
#         break
#     a = int(input())
# else:
#     print('ни одного отрицательного число не встретилось')



# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print('цикл окончен, i =', i)



# n = int(input())
# length = 0
# while n > 0:
#     n //= 10
#     length += 1
# print(length)



# i = 1
# while i <= 10:
#     print(i ** 2)
#     i += 1



# print('Abracadabra'.count('a'))
# print(('a' * 10).count('aa'))



# print('Abrakadabra'.replace('a', 'A', 2))



# print('Hello'.replace('l', 'L'))



# s = 'Hello'
# print(s.find('l'))
# print(s.rfind('l'))






# s = 'Hello'
# print(s.find('e'))
# print(s.find('ll'))
# print(s.find('L'))








# s = 'abcdefghijklm'
# print(s[0:10:2])
# for i in range(0, 10, 2):
#     print(i, s[i])





#
# s = 'abcdefg'
# print(s[1])
# print(s[-1])
# print(s[1:3])
# print(s[1:-1])
# print(s[:3])
# print(s[2:])
# print(s[:-1])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])









# s = input()
# print(len(s))
# t = input()
# number = int(t)
# u = str(number)
# print(s * 3)
# print(s + ' ' + u)









# print(1, 2, 3)
# print(4, 5, 6)
# print(1, 2, 3, sep=',', end='.')
# print(4, 5, 6, sep=',', end='.')
# print()
# print(1, 2, 3, sep=' ', end='--')
# print(4, 5, 6, sep=' * ', end='.')










# sum = 0
# n = 5
# for i in range(1, n + 1):
#     sum += i
# print(sum)








# for i in range(4):
#     print(i)
#     print(i ** 2)
# print('конеч цикла')






# for i in 1, 2, 3, "one", 'two', 'three':
#     print(i)






# # номерация картежей
# i = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
#     print('#', i, 'color of rainbow is ', color, sep ='' )
#     i += 1








# from math import *
#
# x = 7 / 2
# y = ceil(x)
# print(y)






# from math import  ceil
#
# x = 7 / 2
# y = ceil(x)
# print(y)
#
#
# import math
#
# x = math.ceil(4.2)
# y = math.ceil(4.8)
# print(x)
# print(y)



# x = float(input())
# print(x)






# print(17 / 3)
# print(17 // 3)
# print(17 % 3)





# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print("первая четверть")
# elif x > 0 and y < 0:
#     print("четвертая четверть")
# elif y > 0:
#     print("вторая четверть")
# else:
#     print("третья четверть")








# a = int(input())
# b = int(input())
# if a % 10 == 0 or b % 10 == 0:
#     print("Yes")
# else:
#     print("No")









# x = int(input())
# y = int(input())
# if x > 0:
#     if y > 0:
#         print("первая четверть")
#     else:
#         print("четвертая четверть")
# else:
#     if y > 0:
#         print("вторая четверть")
#     else:
#         print("третья четверть")






# x = int(input())
# if x < 0:
#     x = -x
#     print(x)







# x = int(input())
# if x > 0:
#     print(x)
# else:
#     print(-x)






# a = input()
# b = input()
# s = a + b
# print(s)






# first = 5
# second = 7
# print(first * second)
# first = "5"
# second = "7"
# print(first * second)







# a = int(input())
# b = int(input())
# s = a + b
# print(s)






# print("kak vas zovut?")
# name = input()
# print("hello, " + name + "!")







# print(5 + 10)
# print(3 * 7, (17 - 2) * 8)
# print(2 ** 16)
# print(37 / 3)
# print(37 // 3)
#
# print(37 % 3)






# edibles = ["отбивное", "пельмени", "мяса", "орехи"]
#
# for food in edibles:
#     if food == "пельмени":
#         print("я не ем пельмени!")
#         break
#     print("отлично, вкусно " + food)
# else:
#     print("отлично, что не было пельмени!")
# print("ужин окончен.")






# i = 5 ;  print(i)
#                          форматирование
# print('{0:.3}'.format(1/3))

# print('{0},{1},{2}'.format('a', 'b', 'c'))
#
# print('{},{},{}'.format('a', 'b', 'c'))
#
# print('{2},{1},{0}'.format('a', 'b', 'c'))
#
# print('coordinates:{latitude},{longitude}'.format(latitude='37.24N', longitude=' -115.81W'))




#
# age = 24
# name = 'erlan'
# rost = 178
# ves = 76
#
#
#
#
#
# print("тебе __ {}" " твой вес -->{}"" тебя зовут  ++ {}" " твой рост --{}.".format(age, ves, name, rost))
# print(age)
# print('{age} лет и твой рост  {rost}''{name} это же ты и вес  {ves}'.format(age='25', rost='180 ', name='marsel', ves='72'))
# print('{name} правильно ? вес  {ves}'.format(name='marsel', ves='72'))
# print('привет, %s!\n тебе %d лет!' % (name, age))
#            # Placeholder_str -->%s
#            # Placeholder_int-->%d
#            # Placeholder_float-->%f





# print('{0}{1}{0}'.format('abra', 'cad'))








#                                Словарь
# person = {
#          'name': 'jessy',
#          'age': 21
# }
# print('Имя: {name}\nВозрасте: {age}'.format(name=person['name'], age=person['age']))





#             Можно сделать так:Словарь
# human = {
#          'name': 'jessy',
#          'age': 21
# }
#
# print('Имя: {person[name]}\nВозрасте: {person[age]}'.format(person=human))






# input_str = 'jessi'
# # jessy******   <
# # ******jessy   >
# # ***jessy***   ^
#
# print('{0:*^10}'.format(input_str))





# input_str = 'jessi'
# length = 10
#
# # print('Настройка строки:' + str(len(input_str)))
# # print('Результат деления по модулю:' + str(len(input_str) % 2))
# if (len(input_str) % 2):
#       length += 1
# print(('{0:*^'+str(length)+'}').format(input_str))
#




# s = '''это многострочные строка.
#                                       ....   ....   ....   ....   .    .    ....   ....     :
#           .        .                  :      :  :   :  :   :      :  . :    :      :  :     :
#        .    .   .     .               :      :  :   :..:   :      : .  :    :...   :  :     :
#      .        .         .             :...   :  :   :  :   :...   .    :    :..:   :..:     .
#    .                      .
#      .                   .
#        .               .
#          .          .
#            .     .
#              . .
#               .
#
# Это вторая её строка.'''
# print(s)
# a = input("Пишите ваше имя?")
# print(a + " Это вам")







# '{0:.3}'.format(1/3)
# '0.333'
# '{0:_^11}'.format('hello')
# '___hello___'
# '{name} Подписал {book}'.format(name='swaroop', book='a byte ofpython')
# 'swaroop Подписал a byte ofpython'







# age = 26
# name = 'swaroop'
# print('возраст {0} -- {1}.'.format(name, age))
# print('почему {0} забавляется с этим python?'.format(name))






# print("hello"    "world")




# def append_to_list(value, my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append(value)
#     print(my_list, id(my_list))

# def append_to_dict(key, value, my_dict=None):
#     if my_dict is None:
#         my_dict = {}
#     my_dict[key] = value
#     print(my_dict)
#
# append_to_dict(10, 100)
# append_to_dict(20, 200)
# append_to_dict(20, 200, {'a':111})
# append_to_list(77)
# append_to_list(99)
# append_to_list(111)
# append_to_list(111, [])



# s_strok = ''
# s_list = []
# s_number = 0
#
# a = [5, 3, 'hello', [3, 4], ' world', [5], 10.5]
# for i in a:
#     if isinstance(i,str):
#         s_strok = s_strok + i
#     elif isinstance(i, list):
#         s_list = s_list + i
#     # elif isinstance(i, int) or isinstance(i, float):
#     elif isinstance(i,(int,float)):
#         s_number = s_number + i
# print(s_strok)
# print(s_list)
# print(s_number)

#
#
# f = lambda x: 'like' if x > 100 else 'subsribe'
# d = lambda x: 'like' if x > 100 else ('subsribe' if x > 0 else 'follow me')
#
# print(d(10))
#
#
#
#
#
#                                  # Изменения в словаре
# heroes = {
#     'spider-men': 80,
#     'batman': 65,
#     'super': 85,
#     'wonder woman': 70,
#     'flash': 70,
#     'iron man': 65,
#     'thor': 90,
#     'aquaman': 65,
#     'capitain America': 65,
#     'hulk': 87,
#
# }
# # выводить толко значение и сортирует
# for i in sorted(heroes.values()):
#     print(i)
#  сортирует по ключу
# for i in sorted(heroes):
#     print(i,heroes[i])
# # сортирует по ключу
# for i in sorted(heroes.items()):
#     print(i)
# # сортирует по значением
# for i in sorted(heroes.items(),key=lambda para: para[1]):
#     print(i)
# # сортирует по значением если в значении есть похожие то будет уже по ключу сортировать
# for i in sorted(heroes.items(), key=lambda para: (para[1], para[0])):
#     print(i)
