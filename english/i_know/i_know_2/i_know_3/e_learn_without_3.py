from english.i_know.i_know_2 import e_i_know_2
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(e_i_know_2.slovar.items()))
    enter2 = f'                                                       {e_for_choice[0]} * {e_for_choice[1]}'
    enter = input(enter2)
    if enter2 == enter:
        pass
    elif enter == "1":
        break
    else:
        words += 1
        print('                                         ', words)
#  нажми в терминале --> enter




"""



271+400+420+1000



"""