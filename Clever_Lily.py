#Input information

lili_years = int(input())
price_washing = float(input())
price_per_toy = int(input())

#logic

number_toys = 0
money = 0
money_from_toys = 0
total_money = 0

for i in range(1, lili_years+1):
    if i % 2 == 0:
        money += (i * 5) - 1
    else:
        number_toys += 1

money_from_toys = number_toys * price_per_toy

total_money = money_from_toys + money

#Print user output

if price_washing <= total_money:
    print(f'Yes! {total_money - price_washing:.2f}')

else:
    print(f'No! {price_washing - total_money:.2f}')