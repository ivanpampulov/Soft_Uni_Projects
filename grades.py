#Input information

students = int(input())

#logic
grade2 = 0
grade3 = 0
grade4 = 0
grade5 = 0
for_average = 0

for i in range(students):
    grade = float(input())
    if 2 <= grade <= 2.99:
        grade2 += 1
        for_average += grade
    elif 3 <= grade <= 3.99:
        grade3 += 1
        for_average += grade
    elif 4 <= grade <= 4.99:
        grade4 += 1
        for_average += grade
    elif grade >=5.00:
        grade5 += 1
        for_average += grade

#print user output

print(f'Top students: {grade5 / students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {grade4 / students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {grade3 / students * 100:.2f}%')
print(f'Fail: {grade2 / students * 100:.2f}%')
print(f'Average: {for_average / students:.2f}')