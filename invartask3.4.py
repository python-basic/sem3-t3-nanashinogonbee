from string import ascii_uppercase as au
from string import ascii_lowercase as al

my_str = input('Enter a string: ')

res = my_str.maketrans(
        f'{au[13:]}{al[13:]}{au[:13]}{al[:13]}',
        f'{au[:13]}{al[:13]}{au[13:]}{al[13:]}')

print(f'{my_str.translate(res)}')
