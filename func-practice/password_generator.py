import random

import string


letters_lower = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)
digits = list(string.digits)


def password_generator():
    n = int(input('Сколько знаков будет в Вашем пароле? '))
    password = []
    for i in range(3):
        password.append(random.choice(letters_upper))
    for i in range(4):
        password.append(random.choice(digits))
    for i in range(n-7):
        password.append(random.choice(letters_lower))
    if n < 8:
        print('Пароль должен содержать не менее 8 символов.')
    elif n > 100:
        print('Ваш пароль слишком длинный.')
    else:
        for i in range(n):
            print(''.join(random.choice(password)), end='')


password_generator()
    
