#Read user input

n = int(input())
current = 1
is_current = False

#Logic

for i in range(1, n+1):
    for j in range(1, i + 1):

        if current > n:
            is_current = True
            break
        print(str(current) + ' ', end='')
        current += 1
    if is_current:
        break

    print()