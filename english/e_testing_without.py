from english import e_method_13
from random import choice
right = 0
wrong = 0
mistake = 0
common = 0
running = 1
while running:
    k = [value for value in e_method_13.slovar.values()]
    s = choice(k)
    print(s)
    testing = input('перевод? : ')
    if testing in e_method_13.slovar:
        value1 = e_method_13.slovar[testing]
        if s == value1:
            right += 1
            common += 1
            print(f"                           правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
            print(f'правилно! {testing} означает  : ' + value1)
            with open(r'/Users/macbookpro/PycharmProjects/python_test/english/e_method_13.py',
                      'a') as f:
                f.write(f'#"{testing}": "{value1}",\n')
                f.close()
            print(" \n ")


        elif s != value1:
            wrong += 1
            common += 1
            print(f"                           правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
            print("попробуйту еще раз!")
            print(f'неправилно! {testing} означает  : ' + value1)
            print(" \n ")

    else:
        mistake += 1
        common += 1
        print(f"                               правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
        print(e_method_13.slovar.get("fwefe", "такого слова нет в словаре, попробуйту еще раз! "))
        d = dict.fromkeys([s])
        print(d)
        print(" \n ")

    if testing == "1":
        break


"""
(0)----
(1)----
(2)----11+1+6+47+50+21+29+25
(3)----29+35+31+24+20+4
(4)----25+31+31+9+17+25+27+25
(5)----3+4+17+31+15+7+1+14
(6)----1+2+4+0+{25}+9+{36}+{18}+6+0+0+8+6+0+8+82+31
(7)----0+2+7+2+4+21+{37}
(8)----45+42+43+4+16+12+5
(9)----60+50+37+23
(10)----30+45+35+35
(11)----17+10+10+11+10
(12)----24+30+25+20+25+12+22+15+30
(13)----1+30+23+14+25+25
(14)----
(15)----

"""
