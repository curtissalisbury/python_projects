hours = input('Hours worked: ' )
pay_rate = input('What is your rate of pay: ')

hours_worked = float(hours)
wage = float(pay_rate)

if hours_worked > 40:
    more_than = hours_worked - 40
    over_time = more_than * (wage * 0.5)


total_pay = (hours_worked * wage) + over_time

print(total_pay)