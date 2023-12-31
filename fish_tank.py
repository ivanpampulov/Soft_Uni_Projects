length = int(input())
width = int(input())
height = int(input())
percent = float(input())/100

volume = length * width * height
cubic_decimeter = volume / 1000
other = cubic_decimeter * percent

total_water = cubic_decimeter - other

print(total_water)