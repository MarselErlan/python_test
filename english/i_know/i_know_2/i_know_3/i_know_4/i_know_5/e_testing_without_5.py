from english.i_know.i_know_2.i_know_3.i_know_4 import e_i_know_4
from random import choice
right = 0
wrong = 0
mistake = 0
common = 0
running = 1
while running:
    k = [value for value in e_i_know_4.slovar.values()]
    s = choice(k)
    print(s)
    testing = input('перевод? : ')
    if testing in e_i_know_4.slovar:
        value1 = e_i_know_4.slovar[testing]
        if s == value1:
            right += 1
            common += 1
            print(f"                           правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
            print(f'правилно! {testing} означает  : ' + value1)
            with open(r'/Users/macbookpro/PycharmProjects/python_test/english/i_know/i_know_2/i_know_3/i_know_4/e_i_know_4.py',
                      'a') as f:
                f.write(f'#"{testing}": "{value1}",\n')
                f.close()

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
        print(e_i_know_4.slovar.get("fwefe", "такого слова нет в словаре, попробуйту еще раз! "))
        d = dict.fromkeys([s])
        print(d)
        print("  \n  ")

    if testing == "1":
        break

"""
100-0-3
22-0-0
100-2-4
100-4-4
100-2-8
100-0-10
100-0-15
133-2-20
41-0-12
27-0-3
14-0-5
"""