#read user input

daily_money = float(input())
turnover = float(input())
expenses = float(input())
gift_price = float(input())

#logic
total_money = ((5 * daily_money) + (5 * turnover)) - expenses

if total_money < gift_price:
    print(f'Insufficient money: {gift_price - total_money:.2f} BGN.')

else:
    print(f'Profit: {total_money:.2f} BGN, the gift has been purchased.')