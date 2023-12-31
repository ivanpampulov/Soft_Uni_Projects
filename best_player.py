#read user input
top_score = 0
mvp = 0

while True:
    player = input()

    if player == 'END':
        if top_score >= 3:
            print(f'{mvp} is the best player!')
            print(f'He has scored {top_score} goals and made a hat-trick !!!')
            break
        else:
            print(f'{mvp} is the best player!')
            print(f'He has scored {top_score} goals.')
            break

    goals_scored = int(input())

    if goals_scored >= 10:
        if goals_scored >= 3:
            print(f'{player} is the best player!')
            print(f'He has scored {goals_scored} goals and made a hat-trick !!!')
            break

    if goals_scored > top_score:
        top_score = goals_scored
        mvp = player



