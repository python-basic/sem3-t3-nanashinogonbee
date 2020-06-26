import random
rmin = 0
rmax = 99
rand = random.randint(rmin, rmax)
print('''I generated a random number from {} to {}.
Try to guess it.
'''.format(rmin, rmax))
while True:
    try:
        prompt = int(input('Your answer: '))
        if prompt != rand:
            if prompt < rand:
                print('Your number is smaller.')
            if prompt > rand:
                print('Your number is greater.')
        else:
            break
    except ValueError:
        print('Something you\'ve entered was not a number. Try again.')
print('Correct! The number is {}.'.format(rand))

