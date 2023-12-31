#Input information

groups = int(input())

#logic

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for i in range(1, groups+1):
    count_people = int(input())
    if count_people <= 5:
        g1 += count_people
    elif 6 <= count_people <= 12:
        g2 += count_people
    elif 13 <= count_people <= 25:
        g3 += count_people
    elif 26 <= count_people <= 40:
        g4 += count_people
    elif count_people >= 41:
        g5 += count_people

total = g1 + g2 + g3 + g4 + g5

#Print output
print(f'{(g1/total)*100:.2f}%')
print(f'{(g2/total)*100:.2f}%')
print(f'{(g3/total)*100:.2f}%')
print(f'{(g4/total)*100:.2f}%')
print(f'{(g5/total)*100:.2f}%')
