#Input information
days = int(input())
nights_spend = days - 1
type_of_room = input()
grade = input()

price_room = 18
price_apartment = 25
price_pres_apart = 35
total = 0
final_paid = 0

#Logic
if type_of_room == 'room for one person':
    total = price_room * nights_spend

if type_of_room == 'apartment' and days < 10:
    total = price_apartment * nights_spend - (price_apartment * nights_spend) * 0.3

elif type_of_room == 'apartment' and 10 <= days < 15:
    total = price_apartment * nights_spend - (price_apartment * nights_spend) * 0.35

elif type_of_room == 'apartment' and days >= 15:
    total = price_apartment * nights_spend - (price_apartment * nights_spend) * 0.5

if type_of_room == 'president apartment' and days < 10:
    total = price_pres_apart * nights_spend - (price_pres_apart * nights_spend) * 0.1

elif type_of_room == 'president apartment' and 10 <= days < 15:
    total = price_pres_apart * nights_spend - (price_pres_apart * nights_spend) * 0.15

elif type_of_room == 'president apartment' and days >= 15:
    total = price_pres_apart * nights_spend - (price_pres_apart * nights_spend) * 0.2

if grade == 'positive':
    final_paid = total + (total * 0.25)

else:
    final_paid = total - (total * 0.10)

print(f'{final_paid:.2f}')