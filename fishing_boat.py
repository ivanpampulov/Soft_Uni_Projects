#Input information

budget = int(input())
season = input()
count_fisherman = int(input())
cost = 0
discount = 0
price_boat = 0
mid_cost = 0
add_discount = 0
final_cost = 0

#Logic
if season == 'Spring':
    price_boat = 3000
elif season == 'Summer' or season == 'Autumn':
    price_boat = 4200
elif season == 'Winter':
    price_boat = 2600

if count_fisherman <= 6:
    discount = 0.10
elif 7 < count_fisherman <= 11:
    discount = 0.15
elif count_fisherman > 12:
    discount = 0.25

mid_cost = price_boat - (price_boat * discount)

if count_fisherman %2 ==0 and season != 'Autumn':
    add_discount = 0.05

final_cost = mid_cost - (mid_cost * add_discount)

#Print user output

if budget - final_cost >=0:
    print(f'Yes! You have {budget-final_cost:.2f} leva left.')

else:
    print(f'Not enough money! You need {final_cost - budget:.2f} leva.')