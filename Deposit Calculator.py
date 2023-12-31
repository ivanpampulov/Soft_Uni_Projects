deposit_amount = float(input())
term_of_deposit = int(input())
ann_interest_rate = float(input())/100

sum = deposit_amount + term_of_deposit * ((deposit_amount * ann_interest_rate)/12)

print(sum)