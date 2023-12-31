#read user input

count_man = int(input())
count_woman = int(input())
tables = int(input())
is_full = False
counter = 0

#logic

for i in range(1, count_man + 1):
    for j in range(1, count_woman + 1):
        counter += 1
        if counter == tables:
            is_full = True
            break
        print(f'({i} <-> {j})', end=' ')

if is_full:
    print(f'({i} <-> {j})', end=' ')