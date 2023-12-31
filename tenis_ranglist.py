#Input information
from math import floor

tournaments = int(input())
starting_points = int(input())

#Logic
winning = 0
winning_points = 0

for i in range(1, tournaments +1):
    stage = input()
    if stage == 'W':
        starting_points += 2000
        winning += 1
        winning_points += 2000
    elif stage == 'F':
        starting_points += 1200
        winning_points += 1200
    elif stage == 'SF':
        starting_points += 720
        winning_points += 720

#Print output
print(f'Final points: {starting_points}')
print(f'Average points: {floor(winning_points / tournaments)}')
print(f'{winning / tournaments * 100:.2f}%')