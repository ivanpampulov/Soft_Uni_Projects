#Input information

norm = 30000
holidays = int(input())
working_days = 365 - holidays
working_days_play = working_days * 63
holidays_play = holidays * 127

#Logic
total_play = working_days_play + holidays_play
difference = norm - total_play
hours = abs(difference) //60
minutes = abs(difference) %60

if difference < 0:
    print('Tom will run away')
    print(f'{abs(hours)} hours and {abs(minutes)} minutes more for play')

else:
    print('Tom sleeps well')
    print(f'{abs(hours)} hours and {abs(minutes)} minutes less for play')