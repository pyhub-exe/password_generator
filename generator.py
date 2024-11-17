import random

def generator():
    global password
    letters = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('1234567890')
    spec = list('!&@$^$*_#-+=~`')
    passcomb = [letters, numbers, spec]
    password = ''
    print('                                     Генератор паролей by kita v.1.0')
    print('Введите длину пароля')
    length = int(input())


    for i in range(length):
        chosed = passcomb[random.randint(0,2)]
        chosedsym = chosed[random.randint(0, len(chosed) - 1)]
        if chosedsym.isalpha():
            if random.randint(1,2) == 2:
                chosedsym = chosedsym.upper()
            else:
                chosedsym = chosedsym.lower()
        password += chosedsym



    print(f'Ваш новый пароль: {password}')

generator()

