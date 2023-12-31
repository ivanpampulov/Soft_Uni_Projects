#Read user input
import sys

n = int(input())

#Logic

sum = 0
max_num = -sys.maxsize
sum_others = 0

for i in range(n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum += num

#Print user output

if max_num == sum - max_num:
    print('Yes')
    print(f'Sum = {sum - max_num}')

else:
    print('No')
    sum_others = sum - max_num
    print(f'Diff = {abs(sum_others - max_num)}')