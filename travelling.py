#Logic

sum_budget = 0

while True:
    destination = input()
    if destination == 'End':
        break
        
    price = float(input())

    while True:
        budget = float(input())
        sum_budget += budget
        if sum_budget >= price:
            print(f'Going to {destination}!')
            sum_budget = 0
            break

