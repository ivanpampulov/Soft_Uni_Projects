#Read user input

n = int(input())
counter = 0

#Logic
for i in range(0, n+1):
    for j in range(0, n+1):
        for k in range(0, n+1):
            result = i + j + k
            if result == n:
                counter += 1

print(counter)