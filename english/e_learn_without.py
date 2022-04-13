from english import e_method_13
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(e_method_13.slovar.items()))
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

71_0-----
250_1----
250_2----107+110+35+51+52+110
250_3----32+100+50+60+50+110
250_4----20+20+20+21+20+20+111
250_5----20+20+20+20+20
250_6----20+20+20+20+20+20+20+20+20+20
250_7----30+30+30+12+30
200_8----30+30+30+30
250_9----40+40+40
250_10---100+41+31+30+100
250_11---
250_12---100+40+40+40+40+40+40+40+40
250_13---41+40+40+40+40
250_14---
250_15---

"""