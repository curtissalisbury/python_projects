fname = input('Enter File Name: ')

try:
    fhand = open(fname)
except:
    print('Enter a valid filename', fhand)
    quit()

for line in fhand:
    print(line.upper().rstrip())