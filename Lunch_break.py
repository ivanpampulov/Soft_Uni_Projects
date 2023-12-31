#Input information
from math import ceil

name_of_movie = input()
length = int(input())
break_length = int(input())
time_for_lunch = 1/8 * break_length
time_for_rest = 1/4 * break_length

time_left = break_length - (time_for_lunch + time_for_rest + length)

if time_left >= 0:
    print(f'You have enough time to watch {name_of_movie} and left with {ceil(time_left)} minutes free time.')

else:
    print(f"You don't have enough time to watch {name_of_movie}, you need {ceil(abs(time_left))} more minutes.")