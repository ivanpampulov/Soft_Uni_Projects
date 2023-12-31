#Input information

hour = int(input())
weekday = input()
output = ""

#Logic
if weekday != 'Sunday' and 10 <= hour <= 18:
    output = 'open'

else:
    output = 'closed'

#Print output
print(output)