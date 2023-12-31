#read user input

total = int(input())
count_cash = 0
count_card = 0
total_money_card = 0
total_money_cash = 0
counter = 0
is_money = False

while True:
    if total_money_cash + total_money_card >= total:
        is_money = True
        break

    read_input = input()
    counter += 1

    if read_input == 'End':
        print('Failed to collect required money for charity.')
        break

    price = int(read_input)
    if counter % 2 == 0:
        if price < 10:
            print('Error in transaction!')
        else:
            print('Product sold!')
            count_card += 1
            total_money_card += price
        continue
    else:
        if price > 100:
            print('Error in transaction!')
        else:
            print('Product sold!')
            count_cash += 1
            total_money_cash += price
        continue

if is_money:
    print(f'Average CS: {total_money_cash / count_cash:.2f}')
    print(f'Average CC: {total_money_card / count_card:.2f}')
