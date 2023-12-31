#Input information

x = float(input())
y = float(input())
h = float(input())

expense_green = 3.4
expense_red = 4.3

front_and_back = (x * x * 2) - (1.2 * 2)
both_sides = (x * y * 2) - (1.5 * 1.5 * 2)
total_green = front_and_back + both_sides

roof_front_and_back = x * y * 2
roof_both_sides = ((x * h) /2) * 2
total_red = roof_both_sides + roof_front_and_back

green_paint = total_green / expense_green
red_paint = total_red / expense_red

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')