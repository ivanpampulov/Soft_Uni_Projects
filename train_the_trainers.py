#read user input

jury = int(input())
total = 0
while_average = 0
counter = 0

while True:
    presentation = input()

    if presentation == 'Finish':
        print(f"Student's final assessment is {while_average / counter:.2f}.")
        break

    for grades in range(jury):
        grade = float(input())
        counter += 1
        total += grade
    average = total / jury
    while_average += total
    total = 0


    print(f'{presentation} - {average:.2f}.')



