#read user input

number = int(input())

#logic
for i in range(1, number + 1):
    for j in range(1, number + 1):
        for k in range(1, number + 1):
            for l in range(1, number + 1):
                if i + j == k + l and number % (i + j) == 0:
                    print(f'{i}{j}{k}{l}')
