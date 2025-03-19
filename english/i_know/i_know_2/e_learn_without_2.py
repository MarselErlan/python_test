from english.i_know import e_i_know_1
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(e_i_know_1.slovar.items()))
    enter2 = f'                                                       {e_for_choice[0]} * {e_for_choice[1]}    '
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


40+481+400
13.04} + 43[17]
15.04} + 200[] + 60[3] + 108[] + 100[] + 46[]
16.04} + 100[]
18.04} + 80[] + 100[]
19.04} + 85[]
22.04} + 111[]

'
23.04} + 100[] + 50[]
25.04} + 100[]
19.05} +33[]
23.05} +101[]
26.05} + 101[]



"""