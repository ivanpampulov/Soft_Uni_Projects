#read user input

num1 = int(input())
num2 = int(input())


#Logic
for current_number in range(num1, num2+1):
    sum_even = 0
    sum_odd = 0
    number_to_str = str(current_number)

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            sum_odd += int(digit)
        else:
            sum_even += int(digit)

    if sum_odd == sum_even:
        print(current_number, end= ' ')