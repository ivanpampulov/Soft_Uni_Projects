#Input information
price_trip = float(input())
qty_puzzle = int(input())
qty_doll = int(input())
qty_teddy_bears = int(input())
qty_minion = int(input())
qty_truck = int(input())

puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

total = qty_puzzle * puzzle_price + qty_doll * doll_price + qty_teddy_bears * teddy_bear_price\
               + qty_minion * minion_price + qty_truck * truck_price

total_qty = qty_truck + qty_doll + qty_minion + qty_puzzle + qty_teddy_bears


if total_qty >= 50:
    final_price = total - (total *0.25)
    rent = final_price *0.10
    total_income = final_price - rent

elif total_qty <50:
    rent = total *0.10
    total_income = total - rent

if total_income - price_trip <0:
    print(f'Not enough money! {abs((total_income - price_trip)):.2f} lv needed.')

else:
    print(f"Yes! {(total_income - price_trip):.2f} lv left.")