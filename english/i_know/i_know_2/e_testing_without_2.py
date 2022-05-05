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
                f.write(f'#    "{testing}": "{value1}",\n')
                f.close()
            e_i_know_1.slovar.pop(testing)
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
13.04} + 30[7] +30[22] 
14.04} + 40[] 
15.04} + 65[12] + 30-0-24[6]  + 50-0-20[] + 25-1-3[] 30-0-7[]
16.04} + 30-0-104[] 37-1-38
18.04} +  23-0-55[]
19.04} + 20-0-22[]
22.04} + 19-3-26[]
23.04} + 24-0-43[]
25.04} + 14-1-22[]

"""