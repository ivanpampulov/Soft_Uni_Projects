#Input information

budget = float(input())
count_actors = int(input())
price_per_act = float(input())
price_decor = budget *0.10

#Logic
if count_actors >150:
    special_price = price_per_act * 0.9
    evaluation = budget - (count_actors * special_price + price_decor)

else:
    evaluation = budget - (count_actors * price_per_act + price_decor)

if evaluation <0:
    print('Not enough money!')
    print(f'Wingard needs {abs(evaluation):.2f} leva more.')

else:
    print('Action!')
    print(f'Wingard starts filming with {evaluation:.2f} leva left.')