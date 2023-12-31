#Input information

starting_amount = float(input())
living_year = int(input())
ivancho_years = 18
money_spend = 0

#logic
for i in range(1800, living_year+1):
    if i != 1800:
        ivancho_years += 1
    if i % 2 == 0:
        money_spend += 12000
    else:
        money_spend += 12000 + 50 * ivancho_years

#Print user output

if starting_amount >= money_spend:
    print(f'Yes! He will live a carefree life and will have {starting_amount-money_spend:.2f} dollars left.')

else:
    print(f'He will need {money_spend-starting_amount:.2f} dollars to survive.')


