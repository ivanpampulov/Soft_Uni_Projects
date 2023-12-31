#Input information
time_first = int(input())
time_second = int(input())
time_third = int(input())

#Logic

total_minutes = (time_first + time_second + time_third) //60
total_seconds = (time_first + time_second + time_third) %60

if total_seconds < 10:
    print(f'{total_minutes}:0{total_seconds}')

else:
    print(f'{total_minutes}:{total_seconds}')

