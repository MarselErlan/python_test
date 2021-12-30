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



# class Person:
#     def __init__(self, name):
#         self.name = name
#     def sayHi(self):
#         print("hello! i am ", self.name)
#
# p = Person("Marsel")
# p.sayHi()
# p.sayHi()



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



class Person:
    def __init__(self, b,  i):
        self.i = i
        self.b = b
    def sayHi(self):
        if self.b == self.i:
            print("right")
        else:
            print("noo")

p = Person(b=10, i=int(input()))
p.sayHi()




