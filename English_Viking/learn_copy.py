from English_Viking import Tableware
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(Tableware.slovar.items()))
    enter2 = f'                                                       {e_for_choice[0]} * {e_for_choice[1]}   '
    enter3 = (e_for_choice[0])
    enter = input(enter2)
    if enter3 == enter:
        pass
        words += 1
        print('                                         ', words)
        with open(r'/Users/macbookpro/PycharmProjects/python_test/english/i_know/e_i_know_1.py',
                  'a') as f:
            f.write(f'#    "{e_for_choice[0]}": "{e_for_choice[1]}",\n')
            f.close()
            Tableware.slovar.pop(e_for_choice[0])

    elif enter == "1":
        pass
    else:
        print("error !!!")
#  нажми в терминале --> enter




"""

13.09} +10+



"""