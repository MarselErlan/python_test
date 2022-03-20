from english import e_method_6
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(e_method_6.slovar.items()))
    enter2 = f'                                                       {e_for_choice[0]}  *  {e_for_choice[1]}'
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



250_1----107+110+35+51+52
250_2----32+100+50+60+50
250_3----20+20+20+21+20+20
250_4----20+20+20+20+20
250_5----20+20+20+20+20+20+20+20+20+20


"""