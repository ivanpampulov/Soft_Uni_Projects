#Input information

count_open_tabs = int(input())
wage = float(input())

#Logic
tab_name = 0
fine = 0

for i in range(count_open_tabs):
    if wage <= fine:
        print('You have lost your salary.')
        break

    else:
        tab_name = input()
        if tab_name == 'Facebook':
            fine += 150
        elif tab_name == 'Instagram':
            fine += 100
        elif tab_name == 'Reddit':
            fine += 50

if wage > fine:
    print(f'{wage - fine}')