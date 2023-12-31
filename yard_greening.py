area = float(input())

price_per_1m2 = 7.61
discount_in_perc = 18/100

price_before_discount = area * price_per_1m2
discount = price_before_discount * discount_in_perc
final_price = price_before_discount - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")