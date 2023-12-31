#Read user input

dishwashing = int(input())
total_detergent = dishwashing * 750
counter = 1
total_dishes = 0
total_pots = 0

#Logic

while total_detergent > 0:
    dishes = input()

    if dishes != 'End':
        dishes = int(dishes)
        if counter % 3 == 0:
            total_detergent -= 15 * dishes
            total_pots += dishes
        else:
            total_detergent -= 5 * dishes
            total_dishes += dishes
        counter += 1

    else:
        print('Detergent was enough!')
        print(f'{total_dishes} dishes and {total_pots} pots were washed.')
        print(f'Leftover detergent {abs(total_detergent)} ml.')
        break

if total_detergent <= 0:
    print(f'Not enough detergent, {abs(total_detergent)} ml. more necessary!')

