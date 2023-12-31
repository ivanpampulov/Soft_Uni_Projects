#Read user input

name = input()
level = 1
fails = 0
average = 0

while True:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails > 1:
            print(f'{name} has been excluded at {level} grade')
            break
        continue

    level += 1
    average += grade
    if level > 12:
        print(f'{name} graduated. Average grade: {average / 12:.2f}')
        break