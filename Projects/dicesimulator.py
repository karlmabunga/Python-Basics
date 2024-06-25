import random


x = "y"

while x.lower() == 'y':
    num = random.randint(1,6)
    if num == 1:
        print('----------------')
        print('|              |')
        print('|              |')
        print('|      0       |')
        print('|              |')
        print('|              |')
        print('----------------')
    if num == 2:
        print('----------------')
        print('|              |')
        print('|              |')
        print('|    0     0   |')
        print('|              |')
        print('|              |')
        print('----------------')
    if num == 3:
        print('----------------')
        print('|       0      |')
        print('|              |')
        print('|       0      |')
        print('|              |')
        print('|       0      |')
        print('----------------')
    if num == 4:
        print('----------------')
        print('|              |')
        print('|  0        0  |')
        print('|              |')
        print('|              |')
        print('|  0        0  |')
        print('|              |')
        print('----------------')
    if num == 5:
        print('----------------')
        print('|  0         0 |')
        print('|              |')
        print('|       0      |')
        print('|              |')
        print('|  0         0 |')
        print('----------------')
    if num == 6:
        print('----------------')
        print('|  0        0  |')
        print('|              |')
        print('|  0        0  |')
        print('|              |')
        print('|  0        0  |')
        print('----------------')
    x = input('Would you like to roll the dice? (Y or N) ')
    if x.lower() != 'y' and x.lower() != 'n':
        print(f'Invalid response: "{x}" is not a valid response. Exit simulator')
    elif x.lower() == 'n':
        print('You have successfully exited the dice simulator :)')