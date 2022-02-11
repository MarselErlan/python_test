from english import e_slovar32
words = 0
from random import choice
running = 1
while running:
    e_for_choice = choice(list(e_slovar32.slovar.items()))
    enter2 = f'{e_for_choice[0]}, {e_for_choice[1]}'
    enter = input(enter2)
    if enter2 == enter:
        pass
    elif enter == "1":
        break
    else:
        words += 1
        print('                                                                     ', words)
#  нажми в терминале --> enter


