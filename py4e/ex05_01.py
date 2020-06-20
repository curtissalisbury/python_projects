"""
Write a program which repeatedly reads numbers until the user enters 'done'.
Once 'done' is entered, print out the total, count, and average of the numbers.
If the user enters anything out than a number, detect their mistake using
try and except and print an error message and skip to the next number
"""
number = 0
total = 0.0
while True:
    string_value = input('Enter a number: ')
    if string_value == 'done':
        break
    try:
        float_value = float(string_value)
    except ValueError:
        print('Invalid Input Enter a Number')
        continue

    number = number + 1
    total = total + float_value

print('ALL DONE')
print(total, number, total/number)