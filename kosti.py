import random


def kubik():
    input('Нажми Enter что бы бросить кубик')

    num = random.randrange(1, 6)

    print('Вам выпала цифра:', num)

    answer = input("Хотите перебросить кубик? (y/n) ")

    if answer == 'y':
        print('Вам выпала цифра:', num)
    elif answer == 'n':
        print('Ну и пошел ты нафек')

    input()


kubik()
