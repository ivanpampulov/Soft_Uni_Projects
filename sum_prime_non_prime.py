
#is_valid = False
sum_prime = 0
sum_non_prime = 0

while True:
    user_input = input()

    if user_input != 'stop':
        numbers = int(user_input)

        if numbers < 0:
            print('Number is negative.')
            continue

        if numbers % 2 == 0 and numbers != 2:
            sum_non_prime += numbers
            continue

        elif numbers % 3 == 0 and numbers != 3:
            sum_non_prime += numbers
            continue

        else:
            sum_prime += numbers

    else:
        print(f'Sum of all prime numbers is: {sum_prime}')
        print(f'Sum of all non prime numbers is: {sum_non_prime}')
        break