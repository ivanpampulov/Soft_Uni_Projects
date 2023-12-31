#read user input

start = int(input())
finish = int(input())
magic_number = int(input())
is_found = False

#Logic
counter = 0
for i in range(start, finish + 1):
    if is_found:
        break

    for j in range(start, finish + 1):
        counter += 1
        sum = i + j
        if sum == magic_number:
            is_found = True
            print(f'Combination N:{counter} ({i} + {j} = {magic_number})')
            break

if not is_found:
    print(f'{counter} combinations - neither equals {magic_number}')