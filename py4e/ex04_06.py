hours_worked = input('Hours worked: ' )
pay_rate = input('What is your rate of pay: ')


def compute_pay(hours, rate):
    try:
        hours = float(hours_worked)
        rate = float(pay_rate)
    except:
        print(f'Error, Please enter a numeric input')
        quit()

    if hours > 40:
        regular_pay = hours * rate
        over_time = (hours - 40) * (rate * 0.5)
        total_pay = regular_pay + over_time
    else:
        total_pay = hours * rate
    return total_pay


print(f'Pay: {compute_pay(hours_worked, pay_rate)}')







