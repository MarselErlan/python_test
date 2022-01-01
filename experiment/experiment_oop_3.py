# class

# class Person:
#     pass
#
# p = Person
# print(p)



# class Person:
#     print("hello")
#
# p = Person()
# print(p)



# class Person:
#     a = int(input())
#     b = 10
#     if a == b:
#         print("right")
#     else:
#         print("noo")



# class Person:
#     def sayHi(self):
#         print('hello')
#
# p = Person()
# p.sayHi()
# p.sayHi()



# class Person:
#     def sayHi(self):
#         a = int(input())
#         b = 10
#         if a == b:
#             print("right")
#         else:
#             print("noo")
#
#
# p = Person()
# p.sayHi()
# p.sayHi()


# class Person:
#     def sayHi(self):
#         second = int(input())
#         minutes = second // 60
#         hours = minutes // 60
#         days = hours // 24
#         print(days, hours, minutes,)
#
#
# p = Person()
# p.sayHi()


# class Person:
#     def sayHi(self):
#         second = int(input())
#         minutes = second // 60
#         hours = minutes // 60
#         days = hours // 24
#         print(days, hours, minutes,)
#
#
# p = Person()
# p.sayHi()


# class Person:
#     def sayHi(self):
#         i = 5
#         while i < 15:
#             print(i)
#             i = i + 2
# p = Person()
# p.sayHi()
# p.sayHi()


# метод инит



class Person:
    def __A__(self, name):
        self.name = name
    def sayHi(self):
        print("hello! i am ", self.name)

p = Person("Marsel")
p.sayHi()
p.sayHi()



# class Person:
#     def __init__(self, name, i):
#         self.name = name
#         self.i = i
#     def sayHi(self):
#         while self.i < 15:
#             print(self.i)
#             self.i = self.i + 2
#         print("hello! i am ", self.name)
#
# p = Person("Marsel",i=int(input()))
# p.sayHi()
# p.sayHi()


# class Person:
#     def __init__(self, i):
#         self.i = i
#     def sayHi(self):
#         b = 10
#         if b == self.i:
#             print("right")
#         else:
#             print("noo")
#
# p = Person(i=int(input()))
# p.sayHi()



# class Person:
#     def __init__(self, b,  i):
#         self.i = i
#         self.b = b
#     def sayHi(self):
#         if self.b == self.i:
#             print("right")
#         else:
#             print("noo")
#
# p = Person(b=10, i=int(input()))
# p.sayHi()

# class Person:
#     def __init__(self, b, a):
#         self.b = b
#         self.a = a
#     def sayHi(self):
#         self.a = 100
#         print(self.b)
#         print(self.a)
#
#
# p = Person(b=[64, 23, 89, 6, 1, 12, 33], a=None)
# p.sayHi()



# переменные класса и обьекта





# class Robot:
#     population = 0
#     def __init__(self, name):
#         self.name = name
#         print('(инициализация {0})'.format(self.name))
#         Robot.population += 1
#     def __del__(self):
#         print('{0} уничтожается!'.format(self.name))
#         Robot.population -= 1
#         if Robot.population == 0:
#             print('{0} был последним.'.format(self.name))
#         else:
#             print('осталось {0:d} работающих роботов.'.format(Robot.population))
#
#     def sayHi(self):
#         print('приветствую! мои хозяева называют меня {0}.'.format(self.name))
#
#
#
# droid1 = Robot('R1-D2')
# droid1.sayHi()
# droid2 = Robot('C-3PO')
# droid2.sayHi()
# droid3 = Robot('joji_1')
# droid3.sayHi()
# droid4 = Robot('joji_2')
# droid4.sayHi()
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
# print("Роботы закончили свою работу. давайте уничтожим их.")
# del droid1
# del droid2
# del droid3
# del droid4



a = True + 4
print(a)