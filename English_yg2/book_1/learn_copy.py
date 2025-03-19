from English_yg2.book_1 import dictionary_words
from random import choice
words = 0
running = 1
while running:
    e_for_choice = choice(list(dictionary_words.slovar.items()))
    enter2 = f'                                                       {e_for_choice[0]} * {e_for_choice[1]}   '
    enter3 = (e_for_choice[0])
    enter = input(enter2)
    if enter3 == enter:
        pass
        words += 1
        print('                                         ', words)
        with open(r'/english/i_know/e_i_know_1.py',
                  'a') as f:
            f.write(f'#    "{e_for_choice[0]}": "{e_for_choice[1]}",\n')
            f.close()
            dictionary_words.slovar.pop(e_for_choice[0])

    elif enter == "1":
        pass
    else:
        print("error !!!")
        with open(r'/English_yg2/book_1/dictionary_words.py',
                  'a') as f:
            f.write(f'#    "{e_for_choice[0]}": "{e_for_choice[1]}",\n')
            f.close()
        dictionary_words.slovar.pop(e_for_choice[0])
        print("  \n  ")
#  нажми в терминале --> enter




"""

14.09} +



"""