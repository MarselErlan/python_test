from english.i_know.i_know_2.i_know_3 import e_i_know_3
from random import choice
right = 0
wrong = 0
mistake = 0
common = 0
running = 1
while running:
    k = [value for value in e_i_know_3.slovar.values()]
    s = choice(k)
    print(s)
    testing = input('перевод? : ')
    if testing in e_i_know_3.slovar:
        value1 = e_i_know_3.slovar[testing]
        if s == value1:
            right += 1
            common += 1
            print(f"                           правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
            print(f'правилно! {testing} означает  : ' + value1)

            with open(r'/Users/macbookpro/PycharmProjects/python_test/english/i_know/i_know_2/i_know_3/e_i_know_3.py', 'a') as f:
                f.write(f'#    "{testing}": "{value1}",\n')
                f.close()
                e_i_know_3.slovar.pop(testing)
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
        print(e_i_know_3.slovar.get("fwefe", "такого слова нет в словаре, попробуйту еще раз! "))
        d = dict.fromkeys([s])
        print(d)
        print("  \n  ")


"""

103-0-5
72-0-5
100-3-8
73-2-17
51-0-9
50-1-2
40-3-6
50-1-12
23-0-7
25-0-2
31-0-3
50-1-8
33-1-9
35-0-12
26-1-17
10-0-0
21.04} + 29-0-6[] + 31-0-0 +  19-0-7[]
29.04} + 82-0-80[] + 50-2-79[]
30.04} + 31-1-15
"""