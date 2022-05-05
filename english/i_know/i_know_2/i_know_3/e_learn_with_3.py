from english.i_know.i_know_2 import e_i_know_2
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(e_i_know_2.slovar.items()))
    enter2 = f'                                                       {e_for_choice[0]} * {e_for_choice[1]}    '
    enter3 = (e_for_choice[0])
    enter = input(enter2)
    if enter3 == enter:
        pass
        words += 1
        print('                                         ', words)
        with open(r'/Users/macbookpro/PycharmProjects/python_test/english/i_know/i_know_2/e_i_know_2.py',
                  'a') as f:
            f.write(f'#    "{e_for_choice[0]}": "{e_for_choice[1]}",\n')
            f.close()
            e_i_know_2.slovar.pop(e_for_choice[0])

    elif enter == "1":
        pass
    else:
        print("                                         error !!!")
#  нажми в терминале --> enter




"""



65
12.04}+103[16] + 100[8]
14.04} + 19[7] 
15.04} + 60[8]
16.04} + 70[5] + 90[7]
19.04} + 25[]
20.04} + 35[]
22.04} + 30[]


"""