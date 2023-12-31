pens = int(input())
markers = int(input())
liters = int(input())
discount = int(input())/100

price_pens = 5.80
price_markers = 7.20
price_liters = 1.2


total_price = pens * price_pens + markers * price_markers + liters * price_liters
discount = total_price * discount
final_price = total_price - discount

print (final_price)