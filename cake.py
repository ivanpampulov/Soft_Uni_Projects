#Read user input

width = int(input())
length = int(input())

total_pieces = width * length
#total_taken = 0

while total_pieces > 0:
    command = input()

    if command == 'STOP':
        print(f'{total_pieces} pieces are left.')
        break

    total_pieces -= int(command)

if command != 'STOP':
    print(f'No more cake left! You need {abs(total_pieces)} pieces more.')




