# class FirstClass:
#     def setdata(self, value):
#         self.data = value
#     def display(self):
#         print(self.data)
#
# x = FirstClass()
# y = FirstClass()
#
# x.setdata("King Arthur")
# y.setdata(3.14159)
#
# x.display()
# y.display()
# x.data = "New value"
# x.display()
# x.anothername = "spam"
#
# class SecondClass(FirstClass):
#     def display(self):
#         print('Current value = "%"' % self.data)
#
# z = SecondClass()
# z.setdata(42)
# z.display()
# x.display()
#
#
#
# class ThirdClass(SecondClass):
#     def __init__(self, value):
#         self.data = value
#     def __add__(self, other):
#         return ThirdClass(self.data  + other)
#     def __str__(self):
#         return '[ThirdClass: %s]' % self.data
#     def mul(self, other):
#         self.data *= other
# a = ThirdClass('abc')
# a.display()
# print(a)
# b = a + 'xyz'
# b.display()
# print(b)
# a.mul(3)
# print(a)
#
# class res():
#     pass
# res.name = 'Bob'
# res.age = 40
# print(res.name)
# x = res()
# y = res()
# x.name, y.name
# x.name = 'Sue'
# res.name, x.name, y.name
#
# list(res.__dict__.keys())
# list(name for name in res.__dict__ if not name.startswith('__'))
# list(x.__dict__.keys())
# list(y.__dict__.keys())
# x.name, x.__dict__['name']
# x.age
# x.__dict__['age']
# x.__class__
# res.__bases__
#
# def uppername(obj):
#     return obj.name.upper()
# uppername(x)
# res.method = uppername()
# x.method()
# y.method()
# res.method(x)
# rec = ('Bob', 40.5, ['dev', 'mgr'])
# print(rec[0])
# res = {}
# res['name'] = 'Bob'
# res['age'] = 40.5
# res['jobs'] = ['dev', 'mgr']
#
# print(res['name'])
# class res:
#     pass
# res.name = 'Bob'
# res.age = 40.5
# res.jobs = ['dev', 'mgr']
#
# print(res.name)
#
# class res:
#     pass
# pers1 = res()
# pers1.name = 'Bob'
# pers1.jobs = ['dev', 'mgr']
# pers1.age = 40.5
#
# pers2 = res()
# pers2.name = 'Sue'
# pers2.jobs = ['dev', 'cto']
#
# pers1.name, pers2.name
#
# class Person:
#     def __init__(self, name, jobs, age=None):
#         self.name = name
#         self.jobs = jobs
#         self.age = age
#     def info(self):
#         return (self.name, self.jobs)
# res1 = Person('Bob', ['dev', 'mgr'], 40.5)
# res2 = Person('Sue', ['dev', 'cto'])
#
# res.jobs, res2.info()
#
# res = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
# res = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
# res = res('Bob', 40.5, ['dev', 'mgr'])
#
#
# class Person:
#     def __init__(self, name, job, pay):
#         self.name = name
#         self.job = job
#         self.pay = pay
#
# class Person:
#     def __init__(self, name, job=None, pay=()):
#         self.name = name
#         self.job = job
#         self.pay = pay
#
#
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
# bob = Person('Bob Smith')
# sue = Person('Sue Jones', job='dev', pay=100000)
# print(bob.name, bob.pay)
# print(sue.name, sue.pay)
#
# #
#
#
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
# if __name__=='__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     print(bob.name, bob.pay)
#     print(sue.name, sue.pay)
#
#
# import experiment_oop_2
#
# name = 'Bob Smith'
# name.split()
#
# name.split()[-1]
# pay = 100000
# pay *= 1.10
# print('%.2f' % pay)
#
# #
#
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
# if __name__=='__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     print(bob.name, bob.pay)
#     print(sue.name, sue.pay)
#     print(bob.name.split()[-1])
#     sue.pay *= 1.10
#     print('%.2f' % sue.pay)
#
#
# #
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaise(self, percent):
#         self.pay = int(self.pay * (1 + percent))
# if __name__=='__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     print(bob.name, bob.pay)
#     print(sue.name, sue.pay)
#     print(bob.lastName(), sue.lastName())
#     sue.giveRaise(.10)
#     print(sue.pay)
#
#
# @rangetest(percent=(0.0, 1.0))
# def giveRaise(self, percent):
#     self.pay = int(self.pay * (1 + percent))
#
#
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaise(self, percent):
#         self.pay = int(self.pay * (1 + percent))
#     def __repr__(self):
#         return '[Person: %s, %s]' % (self.name, self.pay)
# if __name__=='__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     print(bob)
#     print(sue)
#     print(bob.lastName(), sue.lastName())
#     sue.giveRaise(.10)
#     print(sue)
#
# class Manager(Person):
#     def giveRaise(self, percent, bonus=.10):
#         self.pay = int(self.pay * (1 + percent + bonus))
#
#
# class Manager(Person):
#     def giveRaise(self, percent, bonus=.10):
#         Person.giveRaise(self, percent + bonus)
#
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaise(self, percent):
#         self.pay = int(self.pay * (1 + percent))
#     def __repr__(self):
#         return '[Person: %s, %s]' % (self.name, self.pay)
#
# class Manager(Person):
#     def giveRaise(self, percent, bonus=.10):
#         Person.giveRaise(self, percent + bonus)
# if __name__=='__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     print(bob)
#     print(sue)
#     print(bob.lastName(), sue.lastName())
#     sue.giveRaise(.10)
#     print(sue)
#     tom = Manager('Tom Jones', 'mgr', 50000)
# Manager: __inint__
#     tom.giveRaise(.10)
#     print(tom.lastName())
#     print(tom)
#
# if __name__=='__main__':
#     ...
#     print('---all three--')
#     for obj in (bob, sue, tom):
#         obj.giveRaise(.10)
#         print(obj)
#
# class Person:
#     def lastName(self): ...
#     def giveRaise(self): ...
#     def __repr__(self): ...
# class Manager(Person):
#     def giveRaise(self, ...): ...
# tom = Manager()
# tom.lastName()
# tom.giveRaise()
# tom.someThingElse()
# print(tom)
#
#
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaise(self, percent):
#         self.pay = int(self.pay * (1 + percent))
#     def __repr__(self):
#         return '[Person: %s, %s]' % (self.name, self.pay)
# class Manager(Person):
#     def __init__(self, name, pay):
#         Person.__init__(self, name, 'mgr', pay)
#     def giveRaise(self, percent, bonus=.10):
#         Person.giveRaise(self, percent + bonus)
# if __name__=='__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     print(bob)
#     print(sue)
#     print(bob.lastName(), sue.lastName())
#     sue.giveRaise(.10)
#     print(sue)
#     tom = Manager('Tom Jones', 50000)
#     tom.giveRaise(.10)
#     print(tom.lastName())
#     print(tom)
#
#
# #
#
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaise(self, percent):
#         self.pay = int(self.pay * (1 + percent))
#     def __repr__(self):
#         return '[Person: %s, %s]' % (self.name, self.pay)
# class Manager:
#     def __init__(self, name, pay):
#         self.person = Person(name, 'mgr', pay)
#     def giveRaise(self, percent, bonus=.10):
#         self.person.giveRaise(percent + bonus)
#     def __getattr__(self, attr):
#         return getattr(self.person, attr)
#     def __repr__(self):
#         return str(self.person)
# if __name__=='__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     print(bob)
#     print(sue)
#     print(bob.lastName(), sue.lastName())
#     sue.giveRaise(.10)
#     print(sue)
#     tom = Manager('Tom Jones', 50000)
#     tom.giveRaise(.10)
#     print(tom.lastName())
#     print(tom)
#
#
# #
# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaise(self, percent):
#         self.pay = int(self.pay * (1 + percent))
#     def __repr__(self):
#         return '[Person: %s, %s]' % (self.name, self.pay)
# class Manager:
#     def __init__(self, name, pay):
#         self.person = Person(name, 'mgr', pay)
#     def giveRaise(self, percent, bonus=.10):
#         self.person.giveRaise(percent + bonus)
#     def __getattr__(self, attr):
#         return getattr(self.person, attr)
#     def __repr__(self):
#         return str(self.person)
# class Department:
#     def __init__(self, *args):
#         self.members = list(args)
#     def addMember(self, person):
#         self.members.append(person)
#     def giveRaises(self, percent):
#         for person in self.members:
#             person.giveRaise(percent)
#     def showall(self):
#         for person in self.members:
#             print(person)
# if __name__=='__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     tom = Manager('Tom Jones', 50000)
#     development = Department(bob, sue)
#     development.addMember(tom)
#     development.giveRaises(.10)
#     development.showall()
#
# #
#
#
# from person import Person
# bob = Person('Bob Smith')
# bob
# print(bob)
# bob.__class__
# bob.__class__.__name__
# list(bob.__dict__.keys())
# for key in bob.__dict__:
#     print(key, '=>', bob.__dict__[key])
#
# for key in bob.__dict__:
#     print(key, '=>', getattr(bob, key))
#
#
# from person import Person
# bob = Person('Bob Smith')
# bob.__dict__.keys()
# dir(bob)
# list(bob.__dict__.keys())
# dir(bob)
# len(dir(bob))
# list(name for name in dir(bob) if not name.startswith('__'))
#
#
# from classtools import AttrDisplay
# class Person(AttrDisplay):
#     ''' создает и обрабатывает записи о людях'''
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#     def giveRaise(self, percent):
#         self.pay = int(self.pay * (1 + percent))
# class Manager(Person):
#     '''настроенная версия Person со специальным требеваниями'''
#     def __init__(self, name, pay):
#         Person.__init__(self, name, 'mgr', pay)
#     def giveRaise(self, percent, bonus=.10):
#         Person.giveRaise(self, percent + bonus)
#
# if __name__=='__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     print(bob)
#     print(sue)
#     print(bob.lastName(), sue.lastName())
#     sue.giveRaise(.10)
#     print(sue)
#     tom = Manager('Tom Jones', 50000)
#     tom.giveRaise(.10)
#     print(tom.lastName())
#     print(tom)
#
#
# import person
# bob = person.Person(...)
# from person import Person
# bob = Person(...)
#
# from person import Person, Manager
# bob = Person('Bob Smith')
# sue = Person('Sue Jones', job='dev', pay=100000)
# tom = Manager('Tom Jones', 50000)
# import shelve
# db = shelve.open('persondb')
# for obj in (bob, sue, tom):
#     db[obj.name] = obj
# db.close()
#
# import glob
# glob.glob('person*')
# print(open('persondb.dir').read())
# print(open('persondb.dat', 'rb').read())
#
#
# import shelve
# db = shelve.open('persondb')
# len(db)
# list(db.keys())
# bob = db['Bob Smith']
# bob
# bob.lastName()
# for key in db:
#     print(key, '=>',  db[key])
# for key in sorted(db):
#     print(key, '=>', db[key])
#
#
#
# import shelve
# db = shelve.open('persondb')
# for key in sorted(db):
#     print(key, '\t=>', db[key])
# sue = db['Sue Jones']
# sue.giveRaise(.10)
# db['Sue Jones'] = sue
# db.close()
#
#
# class SharedData:
#     spam = 42
#
# x = SharedData()
# y = SharedData()
# x.spam, y.spam
# SharedData.spam = 99
# x.spam, y.spam, SharedData.spam
# x.spam, y.spam, SharedData.spam
#
# class MixedNames:
#     data = 'spam'
#     def __init__(self, value):
#         self.data = value
#     def display(self):
#         print(self.data, MixedNames.data)
# x = MixedNames(1)
# y = MixedNames(2)
# x.display(); y.display()
#
#
# #
#
# class NextClass:
#     def printer(self, text):
#         self.message = text
#         print(self.message)
# x = NextClass()
# x.printer('instance call')
# x.message
# NextClass.printer(x, 'class call')
# x.message
# NextClass.printer('bad call')
#
# class Super:
#     def method(self):
#         print('in Super.method')
# class Sub(Super):
#     def method(self):
#         print('starting Sub.method')
#         Super.method(self)
#         print('ending Sub.method')
# x = Super()
# x.method()
# x = Sub()
# x.method()
#
# class Super:
#     def method(self):
#         print('in Super.method')
#     def delegate(self):
#         self.action()
# class Inheritor(Super):
#     pass
# class Replacer(Super):
#     def method(self):
#         print('in Replacer.method')
#
# class Extender(Super):
#     def method(self):
#         print('starting Extender.method')
#         Super.method(self)
#         print('ending Extender.method')
# class Provider(Super):
#     def action(self):
#         print('in Provider.action')
# if __name__=='__main__':
#     for klass in (Inheritor, Replacer, Extender):
#         print('\n' + klass.__name__ + '...')
#         klass().method()
#     print('\nProvider...')
#     x = Provider()
#     x.delegate()
#
#
# class Super:
#     def delegate(self):
#         self.action()
#     def action(self):
#         assert False, 'action must be defined!'
# x = Super()
# x.delegate()
#
# class Super:
#     def delegate(self):
#         self.action()
#     def action(self):
#         raise NotImplementedError('action must be defined!')
# x = Super()
# x.delegate()
# class Sub(Super): Pass
# x = Sub()
# x.delegate()
# class Sub(Super):
#     def action(self): print('spam')
# x = Sub()
# x.delegate()
#
# from abc import ABCMeta, abstractmethod
# class Super(metaclass=ABCMeta):
#     @abstractmethod
#     def method(self, ...):
#         pass
# class Super:
#     __metaclass__=ABCMeta
#     @abstractmethod
#     def method(self, ...):
#         pass
#
# from abc import ABCMeta, abstractmethod
# class Super(metaclass=ABCMeta):
#     def delegate(self):
#         self.action()
#     @abstractmethod
#     def action(self):
#         pass
# x = Super()
# class Sub(Super): pass
# x = Sub()
# class Sub(Super):
#     def action(self): print('spam')
# x = Sub()
# x.delegate()
#
#
# x = 11
# def f():
#     print(x)
# def g():
#     x = 22
#     print(x)
# class C:
#     x = 33
#     def m(self):
#         x = 44
#         self.x = 55
#
#
# if __name__=='__main__':
#     print(x)
#     f()
#     g()
#     print(x)
#     obj = C()
#     print(obj.x)
#     obj.m()
#     print(obj.x)
#     print(C.X)
#     print(C.m.X)
#     print(g.X)
#
#
# import manynames
# X = 66
# print(X)
# print(manynames.X)
# manynames.f()
# manynames.g()
# print(manynames.C.X)
# I = manynames.C()
# print(I.X)
# I.m()
# print(I.X)
#
#
# x = 11
# def g1():
#     print(x)
# def g2():
#     global X
#     X = 22
# def h1():
#     X = 33
#     def nested():
#         print(X)
# def h2():
#     X = 33
#     def nested():
#         nonlocal X
#         X = 44
#
# x = 1
# def nester():
#     print(X)
#     class C:
#         print(X)
#         def method1(self):
#             print(X)
#         def method2(self):
#             X = 3
#             print(X)
#     I = C()
#     I.method1()
#     I.method2()
# print(X)
# nester()
# print('-' * 40)
#
# X = 1
# def nester():
#     X = 2
#     print(X)
#     class C:
#         print(X)
#         def method1(self):
#             print(X)
#         def method2(self):
#             X = 3
#             print(X)
#     I = C()
#     I.method1()
#     I.method2()
# print(X)
# nester()
# print('-' * 40)
#
#
#
# x = 1
# def nester():
#     X = 2
#     print(X)
#     class C:
#         X = 3
#         I.X
#         print(X)
#         def method1(self):
#             print(X)
#             print(self.X)
#         def methhod2(self):
#             X = 4
#             print(X)
#             self.X = 5
#             print(self.X)
#     I = C()
#     I.method1()
#     I.methhod2()
# print(X)
# nester()
# print('-' * 40)
#
# class Super:
#     def Hello(self):
#         self.data1 = 'spam'
# class Sub(Super):
#     def hola(self):
#         self.data2 = 'eggs'
# X = Sub()
# X.__dict__
# X.__class__
# Sub.__bases__
# Super.__bases__
# y = Sub()
# X.hello()
# X.__dict__
# x.hola()
# X.__dict__
# list(Sub.__dict__.keys())
# list(Super.__dict__.keys())
# y.__dict__
# X.data1, X.__dict__['data']
# X.data3 = 'toast'
# X.__dict__
# X.__dict__['data3'] = 'ham'
# X.data3
#
# def classtree(cls, indent):
#     print('.' * indent + cls.__name__)
#     for supercls in cls.__bases__:
#         classtree(supercls, indent + 3)
# def instancetree(inst):
#     print('Tree of %s' % inst)
#     classtree(inst.__class__, 3)
# def selftest():
#     class A: pass
#     class B(A): pass
#     class C(A): pass
#     class D(B, C): pass
#     class E:  pass
#     class F(D, E):  pass
#     instancetree(B())
#     instancetree(F())
# if __name__=='__main__': selftest()
# class Emp: pass
# class Person(Emp): pass
# bob = Person()
# import classtree
# classtree.instancetree(bob)
#
#
# " I am docstr.__doc__"
# def funs(args):
#     "I am: docstr.func.__doc__"
#     pass
# class spam:
#     "I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__"
#     def method(self):
#         "I am: spam.method.__doc__ or self.method.__doc__"
#         print(self.__doc__)
#         print(self.method.__doc__)
#
#
# import docstr
# docstr.__doc__
# docstr.func.__doc__
# docstr.spam.__doc__
# docstr.spam,method.__doc__
# x = docstr.spam()
# x.method()
# help(docstr)