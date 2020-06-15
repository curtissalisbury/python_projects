hours = input('how many hours worked: ')
rate = input('what is your current pay rate: ')

# change string to int and calculate
pay = float(hours) * float(rate)
print(f'Your pay for this period is: {pay}')