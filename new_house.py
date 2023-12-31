#Input information

flowers = input()
qty = int(input())
budget = int(input())
total = 0

#Logic

if flowers == "Roses":
    if qty > 80:
        total = (qty * 5) - (qty * 5 * 0.1)
    else:
        total = qty * 5

elif flowers == 'Dahlias':
    if qty > 90:
        total = (qty * 3.80) - (qty * 3.80 * 0.15)
    else:
        total = qty * 3.80

elif flowers == 'Tulips':
    if qty > 80:
        total = (qty * 2.80) - (qty * 2.80 * 0.15)
    else:
        total = qty * 2.80

elif flowers == 'Narcissus':
    if qty < 120:
        total = (qty * 3) + (qty * 3 * 0.15)
    else:
        total = qty * 3

elif flowers == 'Gladiolus':
    if qty < 80:
        total = (qty * 2.50) + (qty * 2.50 * 0.20)
    else:
        total = qty * 2.50

if (budget - total) >= 0:
    print(f'Hey, you have a great garden with {qty} {flowers} and {budget - total:.2f} leva left.')

else:
    print(f'Not enough money, you need {abs(budget - total):.2f} leva more.')
