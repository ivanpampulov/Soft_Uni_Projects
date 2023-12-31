#Input information

period = int(input())
doctors = 7
examined = 0
not_examined = 0

#logic
for i in range(1, period +1):
    patients = int(input())
    if i % 3 == 0:
        if not_examined > examined:
            doctors += 1
    if doctors - patients >= 0:
        examined += patients
    else:
        not_examined += patients - doctors
        examined += doctors

#Print user output
print(f'Treated patients: {examined}.')
print(f'Untreated patients: {not_examined}.')