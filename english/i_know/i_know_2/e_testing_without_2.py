from english.i_know import e_i_know_1
from random import choice
right = 0
wrong = 0
mistake = 0
common = 0
running = 1
while running:
    k = [value for value in e_i_know_1.slovar.values()]
    s = choice(k)
    print(s)
    testing = input('перевод? : ')
    if testing in e_i_know_1.slovar:
        value1 = e_i_know_1.slovar[testing]
        if s == value1:
            right += 1
            common += 1
            print(f"                           правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
            print(f'правилно! {testing} означает  : ' + value1)
            with open(r'/Users/macbookpro/PycharmProjects/python_test/english/i_know/e_i_know_1.py',
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
        print(e_i_know_1.slovar.get("fwefe", "такого слова нет в словаре, попробуйту еще раз! "))
        d = dict.fromkeys([s])
        print(d)
        print("  \n  ")

    if testing == "1":
        break



"""
42-7-22
46-11-26
49-10-35
72-7-36
81-10-55
114-14-78
40-6-177
40-2-68
75-17-201
40-6-60
"""
"""


100-9-99
101-10-126
67-6-122
37-5-67


"""