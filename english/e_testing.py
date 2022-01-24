from english import e_slovar63

right = 0
wrong = 0
mistake = 0
from random import choice
running = 1
while running:
    k = [value for value in e_slovar63.slovar.values()]
    s = choice(k)
    import os
    a = f'say {s}'
    print(a)
    os.system(a)
    testing = input('перевод? : ')
    if testing in e_slovar63.slovar:
        value1 = e_slovar63.slovar[testing]
        if s == value1:
            right += 1
            print("                                                        правильных ответов")
            print('                                                       ', right)
            print(f'правилно! {testing} означает  : ' + value1)

        elif s != value1:
            wrong += 1
            print("                                                       неправильных ответов")
            print('                                                       ', wrong)
            print("попробуйту еще раз!")

    else:
        mistake += 1
        print("                                                               количество не существующих слов")
        print('                                                              ', mistake)
        print(e_slovar63.slovar.get("fwefe", "такого слова нет в словаре, попробуйту еще раз! "))

    if testing == "1":
        break

#     if comp > user:
#         print("вы проиграли!")
#         cash -= bet
#         print(cash)
#         with open("results.txt", "a") as file:
#             file.write(f"\nк:{comp}, ю:{user} ставка: {bet} проиграш! остаток: {cash}")
#     elif comp < user:
#         print("вы победили!")
#         cash += bet
#         print(cash)
#         with open("results.txt", "a") as file:
#             file.write(f"\nк:{comp}, ю:{user} ставка: {bet} победа! остаток: {cash}")
#     else:
#         print("ничья")
#         print(cash)
#         with open("results.txt", "a") as file:
#             file.write(f"\nк:{comp}, ю:{user} ставка: {bet} ничья!:  остаток: {cash}")
# with open("results.txt", "a") as file:
#     file.write(f"\nвремя игры: {datetime.now() - start}")

# from random import choice
# k = [value for value in slovar.values()]
# s = k.pop(k.index(choice(k)))
# print(s)
#
# prob = input('перевод? : ')
# testing = prob
#
# if testing in slovar:
#     value1 = slovar[testing]
#     if s == value1:
#         print('провилно!  : ' + value1)
# else:
#     print(slovar.get("fwefe", "попробуйту еще раз!"))






# f = open('my_file.txt', 'w')
# f.write(slovar[value])


# print(slovar.get("fwefe", "нет токого слова!"))
# try:
# except KeyError:
#     print()

# print(slovar["hello"])

#
# from random import choice
# from datetime import  datetime
# from time import  sleep
#
# start = datetime.now()
# print(start)
# sleep(0.000000000000001)
# print((datetime.now() - start).seconds)
# print(datetime.now())
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