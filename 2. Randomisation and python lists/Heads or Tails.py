import random as rd

random_coins_side = rd.randint(0, 1)

for i in range (0, 3):
    random_coins_side = rd.randint(0, 1)
    if (random_coins_side == 1):
        print('Heads')
    else:
        print('Tails')