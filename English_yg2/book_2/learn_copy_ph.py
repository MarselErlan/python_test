from English_yg2.book_2 import gram_2
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(gram_2.slovar.items()))
    enter2 = f'                                                       {e_for_choice[0]} * {e_for_choice[1]}   '
    enter3 = (e_for_choice[0])
    enter = input(enter2)
    if enter3 == enter:
        pass
        words += 1
        print('                                         ', words)
        gram_2.slovar.pop(e_for_choice[0])

    elif enter == "1":
        pass
    else:
        print("error !!!")
        with open(r'/Users/macbookpro/PycharmProjects/python_test/English_yg2/book_2/gram_2.py',
                  'a') as f:
            f.write(f'#    "{e_for_choice[0]}": "{e_for_choice[1]}",\n')
            f.close()
        gram_2.slovar.pop(e_for_choice[0])
        print("  \n  ")
#  нажми в терминале --> enter




"""

18.09} + 100
21.09} + 165




"""