import e_slovar100
from random import choice
right = 0
wrong = 0
mistake = 0
common = 0
running = 1
while running:
    k = [value for value in e_slovar100.slovar.values()]
    s = choice(k)
    print(s)
    testing = input('перевод? : ')
    if testing in e_slovar100.slovar:
        value1 = e_slovar100.slovar[testing]
        if s == value1:
            right += 1
            common += 1
            print(f"                           правильные  {right}   неправильные  {wrong}   нет таких слов  {mistake}")
            print(f'правилно! {testing} означает  : ' + value1)
            with open(r'/Users/macbookpro/PycharmProjects/python_test/english_grama/e_slovar100.py',
                      'a') as f:
                f.write(f'#    "{testing}": "{value1}",\n')
                f.close()
            e_slovar100.slovar.pop(testing)
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
        print(e_slovar100.slovar.get("fwefe", "такого слова нет в словаре, попробуйту еще раз! "))
        d = dict.fromkeys([s])
        print(d)
        print("  \n  ")






"""



"""