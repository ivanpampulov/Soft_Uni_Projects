#read user input

total_money = 0

while True:
    money = input()
    if money == 'NoMoreMoney':
        break
    if float(money) < 0:
        print('Invalid operation!')
        break
    else:
        total_money += float(money)
        print(f'Increase: {float(money):.2f}')

print(f'Total: {total_money:.2f}')