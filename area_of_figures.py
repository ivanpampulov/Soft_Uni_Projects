#Input information

type = input()
area = 0

#Logic
if type == "square":
    square_a = float(input())
    area = square_a * square_a

if type == "rectangle":
    rect_a = float(input())
    rect_b = float(input())
    area = round((rect_a * rect_b), 3)

if type == "circle":
    from math import pi
    radius = float(input())
    area = radius * radius * pi

if type == "triangle":
    base = float(input())
    height = float(input())
    area = (base * height) /2

print(f"{area:.3f}")