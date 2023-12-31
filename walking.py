#read user input

target = 10000

#logic

steps_over_goal = 0
daily_steps = 0

while True:
    steps = input()

    if steps == 'Going home':
        steps = int(input())
        daily_steps += steps

        if daily_steps >= target:
            print('Goal reached! Good job!')
            print(f'{daily_steps - target} steps over the goal!')
            break

        elif daily_steps < target:
            print(f'{target - daily_steps} more steps to reach goal.')
            break

    daily_steps += int(steps)

    if daily_steps >= target:
        print('Goal reached! Good job!')
        print(f'{daily_steps - target} steps over the goal!')
        break










