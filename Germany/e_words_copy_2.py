from english.i_know import e_i_know_1
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(e_i_know_1.slovar.items()))
    enter2 = f'                                                           *                    {e_for_choice[0]}  \n'
    enter3 = (e_for_choice[0])
    enter = input(enter2)
    if enter3 == enter:
        pass
        words += 1
        print('                                                                                      ', words)

    elif enter == "1":
        pass
    else:
        print("                                                                                              error !!!")
#  нажми в терминале --> enter
"""
13.04.} + 100[14]
15.04} +  100[] + 60[5] + 200[] + 30[] + 40[]
16.04} + 80[]
18.04} + 75[] + 155[]
19.04} + 60[]
22.04} + 101[]
23.04} + 81[] + 
25.04} + 80[]
"""