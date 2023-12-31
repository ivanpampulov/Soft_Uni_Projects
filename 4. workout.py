from math import ceil

#read user input

training_days = int(input())
km_day_one = float(input())

#logic
total_km = 0
current_km = 0

for i in range(training_days + 1):


    if i == 0:
        current_km = km_day_one
        total_km += current_km
        continue

    increased = int(input())
    current_km = current_km + (current_km * increased/100)
    total_km += current_km

#print output

if total_km >= 1000:
    print(f"You've done a great job running {ceil(total_km - 1000)} more kilometers!")

else:
    print(f'Sorry Mrs. Ivanova, you need to run {ceil(1000 - total_km)} more kilometers')

