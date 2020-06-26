str = input('Enter a string: ')
substr = input('Enter a substring to look for in a string: ')
findex = str.find(substr)
print(str[findex:findex + len(substr)])
