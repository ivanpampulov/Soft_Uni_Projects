#Read user input

book = input()

#Logic
counter = 0

while True:
    current_book = input()

    if current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {counter} books.')
        break

    if current_book == book:
        print(f'You checked {counter} books and found it.')
        break
    counter += 1