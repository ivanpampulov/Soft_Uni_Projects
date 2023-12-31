#Input information

product = input()
city = input()
qty = float(input())
output = ''
#logic

if city == 'Sofia':
    if product == 'coffee':
        output = qty * 0.5
    elif product == 'water':
        output = qty * 0.8
    elif product == 'beer':
        output = qty * 1.20
    elif product == 'sweets':
        output = qty * 1.45
    elif product == 'peanuts':
        output = qty * 1.60

if city == 'Plovdiv':
    if product == 'coffee':
        output = qty * 0.4
    elif product == 'water':
        output = qty * 0.7
    elif product == 'beer':
        output = qty * 1.15
    elif product == 'sweets':
        output = qty * 1.30
    elif product == 'peanuts':
        output = qty * 1.50

if city == 'Varna':
    if product == 'coffee':
        output = qty * 0.45
    elif product == 'water':
        output = qty * 0.7
    elif product == 'beer':
        output = qty * 1.10
    elif product == 'sweets':
        output = qty * 1.35
    elif product == 'peanuts':
        output = qty * 1.55

#Output info

print(output)