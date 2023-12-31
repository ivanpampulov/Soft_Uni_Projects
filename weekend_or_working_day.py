#User input

day_of_week = input()
output_info = 'Error'
#Logic

if day_of_week == "Monday":
    output_info = 'Working day'

elif day_of_week == "Tuesday":
    output_info = 'Working day'

elif day_of_week == "Wednesday":
    output_info = 'Working day'

elif day_of_week == "Thursday":
    output_info = 'Working day'

elif day_of_week == "Friday":
    output_info = 'Working day'

elif day_of_week == "Saturday":
    output_info = 'Weekend'

elif day_of_week == "Sunday":
    output_info = 'Weekend'

#Print output

print(output_info)