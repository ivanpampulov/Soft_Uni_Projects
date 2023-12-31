#read user input

starting_number = int(input())
ending_number = int(input())

#logic
for i in range(starting_number, ending_number + 1):
    for j in range(starting_number, ending_number + 1):
        for k in range(starting_number, ending_number + 1):
            for l in range(starting_number, ending_number + 1):
                if i % 2 == 0 and l % 2 == 1:
                    if i > l:
                        if (j + k) % 2 == 0:
                            print(f'{i}{j}{k}{l}', end=" ")

                elif i % 2 == 1 and l % 2 == 0:
                    if i > l:
                        if (j + k) % 2 == 0:
                            print(f'{i}{j}{k}{l}', end=" ")