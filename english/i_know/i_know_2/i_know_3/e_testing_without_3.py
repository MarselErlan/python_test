from english.i_know.i_know_2 import e_i_know_2
from random import choice
right = 0
wrong = 0
mistake = 0
common = 0
running = 1
while running:
    k = [value for value in e_i_know_2.slovar.values()]
    s = choice(k)
    print(s)
    testing = input('перевод? : ')
    if testing in e_i_know_2.slovar:
        value1 = e_i_know_2.slovar[testing]
        if s == value1:
            right += 1
            common += 1
            print(f"                           правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
            print(f'правилно! {testing} означает  : ' + value1)
            print("  \n  ")

        elif s != value1:
            wrong += 1
            common += 1
            print(f"                           правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
            print("попробуйту еще раз!")
            print(f'неправилно! {testing} означает  : ' + value1)
            print("  \n  ")

    else:
        mistake += 1
        common += 1
        print(f"                               правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
        print(e_i_know_2.slovar.get("fwefe", "такого слова нет в словаре, попробуйту еще раз! "))
        d = dict.fromkeys([s])
        print(d)
        print("  \n  ")

    if testing == "1":
        break

"""
100-4-18
107-6-25
113-3-15
155-6-39
127-3-31
37-1-13
30-2-8
85-0-21
20-0-9
20-0-8
47-1-15
18-0-8
7-0-4

"""