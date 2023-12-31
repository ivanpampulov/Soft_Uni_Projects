#read user input

fat = int(input())
proteins = int(input())
carbons = int(input())
total_calories = int(input())
water = int(input())

#logic
weight_fat = (total_calories * (fat / 100)) / 9
weight_proteins = (total_calories * (proteins / 100)) / 4
weight_carbons = (total_calories * (carbons / 100)) / 4

total_weight = weight_fat + weight_carbons + weight_proteins

calories_per_gram = total_calories / total_weight

calories = ((100 - water) /100) * calories_per_gram

print(f'{calories:.4f}')