tax_per_year = int(input())

shoes = tax_per_year - (tax_per_year * 0.40)
tshirt = shoes - (shoes * 0.2)
ball = tshirt * 0.25
accessories = ball * 0.2

total = tax_per_year + shoes + tshirt + ball + accessories

print (total)