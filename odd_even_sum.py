#Input information

n = int(input())
sum1 = 0
sum2 = 0
#logic

for i in range(n):
    num1 = int(input())
    if i % 2 == 0:
        sum1 += num1
    else:
        sum2 += num1

if sum1 == sum2:
    print('Yes')
    print(f'Sum = {sum2}')

else:
    print('No')
    print(f'Diff = {abs(sum1 - sum2)}')