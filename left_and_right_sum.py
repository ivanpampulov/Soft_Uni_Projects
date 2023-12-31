#user input

n = int(input())
sum1 = 0
sum2 = 0

for i in range(1, n+1):
    num1 = int(input())
    sum1 += num1

for i in range(1, n+1):
    num2 = int(input())
    sum2 += num2

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
else:
    print(f'No, diff = {abs(sum1 - sum2)}')