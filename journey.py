#Input information
budget = float(input())
season = input()
destination = ''
location = ''
type_acc = ''
price = 0

#Logic

if budget <= 100:
    if season == 'summer':
        price = budget * 0.30
        location = 'Bulgaria'
        type_acc = 'Camp'
    elif season == 'winter':
        price = budget * 0.7
        location = 'Bulgaria'
        type_acc = 'Hotel'

elif 100 < budget <=1000:
    if season == 'summer':
        price = budget * 0.4
        location = 'Balkans'
        type_acc = 'Camp'
    elif season == 'winter':
        price = budget * 0.8
        location = 'Balkans'
        type_acc = 'Hotel'
elif budget > 1000:
    price = budget * 0.9
    location = 'Europe'
    type_acc = 'Hotel'

#Print user output

print(f'Somewhere in {location}')
print(f'{type_acc} - {price:.2f}')
