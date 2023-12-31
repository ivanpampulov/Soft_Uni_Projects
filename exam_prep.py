#Read user input
count_grades = int(input())

#Logic
total_grade = 0
tasks = 0
last_problem = 0
bad_grades = 0

while True:
    task_name = input()

    if task_name == 'Enough':
        print(f'Average score: {total_grade / tasks:.2f}')
        print(f'Number of problems: {tasks}')
        print(f'Last problem: {last_problem}')
        break

    grade = int(input())
    if grade <= 4:
        bad_grades += 1
        if count_grades <= bad_grades:
            print(f'You need a break, {bad_grades} poor grades.')
            break

    last_problem = task_name
    total_grade += grade
    tasks += 1