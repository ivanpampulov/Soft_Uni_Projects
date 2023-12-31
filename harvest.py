#Input information

from math import ceil, floor

x = int(input())
grapes_per_sqm = float(input())
grapes_total = x * grapes_per_sqm
for_wine = grapes_total *0.4
grapes_per_wine = 2.5
needed_wine = int(input())
workers = int(input())

produced_wine = for_wine / grapes_per_wine
wine_per_worker = (produced_wine - needed_wine) /workers

if produced_wine < needed_wine:
    print(f'It will be a tough winter! More {floor(needed_wine - produced_wine)} liters wine needed.')

else:
    print(f'Good harvest this year! Total wine: {floor(produced_wine)} liters.')
    print(f'{ceil(produced_wine - needed_wine)} liters left -> {ceil(wine_per_worker)} liters per person.')