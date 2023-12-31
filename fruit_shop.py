#Input information

fruit = input()
weekday = input()
qty = float(input())
output = 0
is_input_correct = True

#Logic
if weekday == 'Monday' or weekday == 'Tuesday' or weekday == 'Wednesday' or weekday == 'Thursday'\
        or weekday == 'Friday':
    if fruit == 'banana':
        output = qty * 2.50
    elif fruit == 'apple':
        output = qty * 1.20
    elif fruit == 'orange':
        output = qty * 0.85
    elif fruit == 'grapefruit':
        output = qty * 1.45
    elif fruit == 'kiwi':
        output = qty * 2.70
    elif fruit == 'pineapple':
        output = qty * 5.50
    elif fruit == 'grapes':
        output = qty * 3.85
    else:
        is_input_correct = False

elif weekday == 'Saturday' or weekday == 'Sunday':
    if fruit == 'banana':
        output = qty * 2.7
    elif fruit == 'apple':
        output = qty * 1.25
    elif fruit == 'orange':
        output = qty * 0.90
    elif fruit == 'grapefruit':
        output = qty * 1.60
    elif fruit == 'kiwi':
        output = qty * 3
    elif fruit == 'pineapple':
        output = qty * 5.60
    elif fruit == 'grapes':
        output = qty * 4.20
    else:
        is_input_correct = False

else:
    is_input_correct = False

if is_input_correct:
    print(f'{output:.2f}')
else:
    print('error')
