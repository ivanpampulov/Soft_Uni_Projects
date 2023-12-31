#Input information

weekday = input()
output = ''

#Logic

if weekday == 'Monday' or weekday == "Tuesday" or weekday == 'Friday':
    output = 12

elif weekday == "Wednesday" or weekday == 'Thursday':
    output = 14

elif weekday == 'Saturday' or weekday == 'Sunday':
    output = 16

#Print user output

print(output)