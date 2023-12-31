naylon_needed = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())

price_naylon = 1.50
price_paint = 14.50
price_thinner = 5
price_bags = 0.4

sum_naylon = (naylon_needed + 2) * price_naylon
sum_paint = (paint * price_paint) * 0.10 + (paint * price_paint)
sum_thinner = thinner * price_thinner
total_materials = price_bags + sum_thinner + sum_paint + sum_naylon
work = (total_materials * 0.30) * working_hours

total_project = total_materials + work

print(f"{total_project}")
