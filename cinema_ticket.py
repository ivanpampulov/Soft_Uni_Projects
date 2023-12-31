# Logic while True is OP xD
count_seats = 0
total_seats = 0
standard = 0
kids = 0
students = 0

while True:
    is_full = False
    is_ended = False

    name_of_movie = input()

    if name_of_movie == "Finish":
        break

    while True:
        free_seats = int(input())

        while True:
            type_of_seat = input()

            if type_of_seat == "End":
                total_seats += count_seats
                print(f'{name_of_movie} - {count_seats / free_seats * 100:.2f}% full.')
                is_ended = True
                break

            if type_of_seat == "kid":
                count_seats += 1
                kids += 1
            elif type_of_seat == 'standard':
                count_seats += 1
                standard += 1
            elif type_of_seat == "student":
                count_seats += 1
                students += 1

            if count_seats >= free_seats:
                total_seats += count_seats
                is_full = True
                print(f'{name_of_movie} - 100.00% full.')
                break

        count_seats = 0

        if is_full:
            break

        if is_ended:
            break

    count_seats = 0

print(f'Total tickets: {total_seats}')
print(f'{students / total_seats * 100:.2f}% student tickets.')
print(f'{standard / total_seats * 100:.2f}% standard tickets.')
print(f'{kids / total_seats * 100:.2f}% kids tickets.')