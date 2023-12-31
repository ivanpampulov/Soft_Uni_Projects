count_chicken = int(input())
count_fish = int(input())
count_vegie = int(input())

price_chicken = 10.35
price_fish = 12.4
price_vegie = 8.15
price_delivery = 2.50

total_food = count_fish * price_fish + count_vegie * price_vegie + count_chicken * price_chicken
desert = total_food * 0.20

total_price = total_food + desert + price_delivery

print(round(total_price,2))