#Input information

cargo = int(input())
price_per_ton = 0
weight_bus = 0
weight_truck = 0
weight_train = 0
total_price = 0
total_weight = 0

#Logic
for i in range(cargo):
    weight = int(input())
    if weight <= 3:
        price_per_ton = 200
        weight_bus += weight
        total_price += price_per_ton * weight
    elif 4 <= weight <= 11:
        price_per_ton = 175
        weight_truck += weight
        total_price += price_per_ton * weight
    elif weight >= 12:
        price_per_ton = 120
        weight_train += weight
        total_price += price_per_ton * weight
    total_weight += weight


#Print user output

print(f'{total_price / total_weight:.2f}')
print(f'{weight_bus / total_weight * 100:.2f}%')
print(f'{weight_truck / total_weight * 100:.2f}%')
print(f'{weight_train / total_weight * 100:.2f}%')