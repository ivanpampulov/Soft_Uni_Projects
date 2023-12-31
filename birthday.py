#read user input

rent = float(input())
budget = 0

#logic
cake = rent * 0.2
drinks = cake - (cake * 0.45)
animation = rent / 3

budget = rent + cake + drinks + animation

print(budget)