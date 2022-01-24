from english import e_slovar63
words = 0
from random import choice
running = 1
while running:
    e_for_choice = choice(list(e_slovar63.slovar.items()))
    enter2 = f'say {e_for_choice[0]}, {e_for_choice[1]}'
    import os
    a = f'say {e_for_choice[0]}, {e_for_choice[1]}'
    os.system(a)
    enter = input(enter2)
    if enter2 == enter:
        words += 1
        print('                                                                                  ', words)
#  нажми в терминале --> enter
    elif enter == "1":
        break

