
def oddNumbers(l, r):
    odd_numbers = []
    for i in range(l, r):
        if i % 2 == 1:
            odd_numbers.append(i)
    print(odd_numbers)



oddNumbers(2, 6)