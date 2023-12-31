#Input information

age = float(input())
gender = input()
output = ''
#Logic

if gender == 'm':
    if age >= 16:
        output = 'Mr.'
    else:
        output = 'Master'

if gender == 'f':
    if age >= 16:
        output = 'Ms.'
    else:
        output = 'Miss'

#Print output

print(output)