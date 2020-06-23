fname = input('Enter File Name: ')

try:
    fhand = open(fname)
except FileNotFoundError:
    print(f'file "{fname}" cannot be found in working directory')
    quit()

for line in fhand:
    print(line.upper().rstrip())