hours = input('Hours worked: ' )
pay_rate = input('What is your rate of pay: ')

try:
    hours_worked = float(hours)
    wage = float(pay_rate)
except:
    print(f'Error, Please enter a numeric input')
    quit()

if hours_worked > 40:
    regular_pay = hours_worked * wage
    over_time = (hours_worked - 40) * (wage * 0.5)
    total_pay = regular_pay + over_time
else:
    total_pay = hours_worked * wage
print(f'Pay: {total_pay}')




