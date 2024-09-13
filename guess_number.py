from random import randint as rnd


number = rnd(1, 5)

print(f'Угадай-ка, Викуля...')
print(f'Число..... от 1 до 5!')

while True:

    guess = int(input(f'Введи число, Викулик: '))

    if guess < number:
        print(f'Твоё число меньше того, что загадано.')

    elif guess > number:
        print(f'Твоё число больше того, что загадано.')
    else:
        break

print(f'Урааа, ты угадала!')
