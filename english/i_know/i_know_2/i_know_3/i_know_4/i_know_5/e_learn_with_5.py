from english.i_know.i_know_2.i_know_3.i_know_4 import e_i_know_4
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(e_i_know_4.slovar.items()))
    enter2 = f'                                                       {e_for_choice[0]} * {e_for_choice[1]}   '
    enter3 = (e_for_choice[0])
    enter = input(enter2)
    if enter3 == enter:
        pass
        words += 1
        print('                                         ', words)
        with open(
                r'/Users/macbookpro/PycharmProjects/python_test/english/i_know/i_know_2/i_know_3/i_know_4/e_i_know_4.py',
                'a') as f:
            f.write(f'#    "{e_for_choice[0]}": "{e_for_choice[1]}",\n')
            f.close()
            e_i_know_4.slovar.pop(e_for_choice[0])

    elif enter == "1":
        pass
    else:
        print("error !!!")
#  нажми в терминале --> enter




"""
            continue more mugger respect crazy east rain weather
27.04} + 51[]





"""