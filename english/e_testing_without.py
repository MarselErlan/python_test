from english import e_method_6
from random import choice
right = 0
wrong = 0
mistake = 0
common = 0
running = 1
while running:
    k = [value for value in e_method_6.slovar.values()]
    s = choice(k)
    print(s)
    testing = input('перевод? : ')
    if testing in e_method_6.slovar:
        value1 = e_method_6.slovar[testing]
        if s == value1:
            right += 1
            common += 1
            print(f"                           правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
            print(f'правилно! {testing} означает  : ' + value1)

        elif s != value1:
            wrong += 1
            common += 1
            print(f"                           правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
            print("попробуйту еще раз!")
            print(f'неправилно! {testing} означает  : ' + value1)

    else:
        mistake += 1
        common += 1
        print(f"                               правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
        print(e_method_6.slovar.get("fwefe", "такого слова нет в словаре, попробуйту еще раз! "))
        d = dict.fromkeys([s])
        print(d)

    if testing == "1":
        break

"""
11
1
6
47
50
21
29

(2)
29
35
31
24
20

(3)
25
31
31
9
17
17
25
27


(4)
3
4
17
31
15
7
1
14

(5)
1
2
4
0-
{25}
9
{36}
{18}
6
0
0-
8
6
0
8-
82
31



"""