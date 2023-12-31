#Input information

month = input()
count_nights = int(input())
price_studio = 0
price_apartment = 0

#Logic
if month == 'May' or month == 'October':
    if 7 < count_nights <= 14:
        price_studio = 50 - (50 * 0.05)
    elif count_nights > 14:
        price_studio = 50 - (50 * 0.30)
    else:
        price_studio = 50

    if count_nights > 14:
        price_apartment = 65 - (65 * 0.1)
    else:
        price_apartment = 65

if month == 'June' or month == 'September':
    if count_nights > 14:
        price_studio = 75.2 - (75.2 * 0.20)
    else:
        price_studio = 75.2

    if count_nights > 14:
        price_apartment = 68.70 - (68.70 * 0.10)
    else:
        price_apartment = 68.70

if month == 'July' or month == 'August':
    price_studio = 76

    if count_nights > 14:
        price_apartment = 77 - (77 * 0.10)
    else:
        price_apartment = 77

#Print user output

print(f'Apartment: {price_apartment * count_nights:.2f} lv.')
print(f'Studio: {price_studio * count_nights:.2f} lv.')