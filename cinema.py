#Input info

type = input()
count_rows = int(input())
count_columns = int(input())
output = 0

#Logic
if type == "Premiere":
    output = count_columns * count_rows * 12

elif type == 'Normal':
    output = count_columns * count_rows * 7.50

elif type == 'Discount':
    output = count_columns * count_rows * 5

print(f'{output:.2f}')