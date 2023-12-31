#Input information

points = int(input())
bonus = 0
add_bonus = 0
add_bonus_2 = 0
total_points = 0

#Logic
if points %2 == 0:
    add_bonus = 1

if points % 10 == 5:
    add_bonus_2 = 2

if points <=100:
    bonus = 5 + add_bonus_2 + add_bonus
    total_points = bonus + points
    print(bonus)
    print(total_points)

elif points >1000:
    bonus = points * 0.10 + add_bonus_2 + add_bonus
    total_points = bonus + points
    print (bonus)
    print(total_points)

else:
    bonus = points * 0.20 + add_bonus_2 + add_bonus
    total_points = bonus + points
    print(bonus)
    print(total_points)


