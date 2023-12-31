#User input

n = int(input())

#logic

max_value = 0
min_value = 0

for i in range(n):
    num = int(input())
    if i == 0:
        max_value = num
        min_value = num
    if num > max_value:
        max_value = num
    elif num < min_value:
        min_value = num

print(f'Max number: {max_value}')
print(f'Min number: {min_value}')