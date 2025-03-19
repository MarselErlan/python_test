from Germany import e_i_know_2
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(e_i_know_2.slovar.items()))
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
            e_i_know_2.slovar.pop(e_for_choice[0])

    elif enter == "1":
        pass
    else:
        print("error !!!")
#  нажми в терминале --> enter




"""

13.04} + 300[31] + 100[19]
14.04} + 35[48] + 22[45] + 100[13]
15.04} + 100[12] + 60[6] + 60[] + 45[]
16.04} + 80[]
18.04} + 40[] + 55[]
19.04} + 31[]
22.04} + 31[]
23.04} + 31[] + 31[]






                                    

"""