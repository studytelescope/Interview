import random


def weird_func(x: int):
    if x < 0:
        return 'Сообщение 1'
    elif x == 0:
        if random.randint(0, 99) < 37:
            return 'Сообщение 2'
    else:
        if random.randint(0, 99) < 5:
            return 'Сообщение 3'

    return ''


mess_2 = 0
mess_3 = 0

for i in range(0, 10000000):
    if weird_func(0) == 'Сообщение 2':
        mess_2 += 1
    if weird_func(1) == 'Сообщение 3':
        mess_3 += 1

print(mess_2, ', ', mess_3)