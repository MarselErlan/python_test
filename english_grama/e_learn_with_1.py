import e_slovar100
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(e_slovar100.slovar.items()))
    enter2 = f'                                                       {e_for_choice[0]} * {e_for_choice[1]}   '
    enter3 = (e_for_choice[0])
    enter = input(enter2)
    if enter3 == enter:
        pass
        words += 1
        print('                                         ', words)
        with open(r'/Users/macbookpro/PycharmProjects/python_test/english_grama/e_slovar100.py',
                  'a') as f:
            f.write(f'#    "{e_for_choice[0]}": "{e_for_choice[1]}",\n')
            f.close()
            e_slovar100.slovar.pop(e_for_choice[0])

    elif enter == "1":
        pass
    else:
        print("error !!!")
#  нажми в терминале --> enter




"""
30.04} + 21[]







                                    

"""