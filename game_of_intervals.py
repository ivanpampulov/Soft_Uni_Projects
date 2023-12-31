#Input information

moves = int(input())

#Logic
result = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

for i in range(moves):
    number = int(input())
    if 0 <= number <= 9:
        result += number * 0.2
        num1 += 1
    elif 10 <= number <= 19:
        result += number * 0.3
        num2 += 1
    elif 20 <= number <= 29:
        result += number * 0.4
        num3 += 1
    elif 30 <= number <= 39:
        result += 50
        num4 += 1
    elif 40 <= number <= 50:
        result += 100
        num5 += 1
    elif number < 0 or number > 50:
        result = result/2
        num6 += 1

#Print user output
print(f'{result:.2f}')
print(f'From 0 to 9: {num1 / moves * 100:.2f}%')
print(f'From 10 to 19: {num2 / moves * 100:.2f}%')
print(f'From 20 to 29: {num3 / moves * 100:.2f}%')
print(f'From 30 to 39: {num4 / moves * 100:.2f}%')
print(f'From 40 to 50: {num5 / moves * 100:.2f}%')
print(f'Invalid numbers: {num6 / moves * 100:.2f}%')