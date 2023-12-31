

price_kg_vegetables = float(input())
price_kg_fruits = float(input())
weight_vegetables = int(input())
weight_fruits = int(input())
bgn_to_eur = 1.94

turnover_vegies = price_kg_vegetables * weight_vegetables
turnover_fruits = price_kg_fruits * weight_fruits

total_bgn = turnover_fruits + turnover_vegies
total_eur = total_bgn / bgn_to_eur

print(f'{total_eur:.2f}')

