#read user input

day_stais = int(input())
room_type = input()
grade = input()

nights = day_stais - 1

#logic
if room_type == 'room for one person':
    cost_per_stay = nights * 18

elif room_type == 'apartment' and 10 > nights:
    total_cost = nights * 25
    discount = total_cost * 0.30
    cost_per_stay = total_cost - discount

elif room_type == 'apartment' and 10 <= nights <= 15:
    total_cost = nights * 25
    discount = total_cost * 0.35
    cost_per_stay = total_cost - discount

elif room_type == 'apartment' and nights > 15:
    total_cost = nights * 25
    discount = total_cost * 0.5
    cost_per_stay = total_cost - discount

elif room_type == 'president apartment' and 10 > nights:
    total_cost = nights * 35
    discount = total_cost * 0.10
    cost_per_stay = total_cost - discount

elif room_type == 'president apartment' and 10 <= nights <= 15:
    total_cost = nights * 35
    discount = total_cost * 0.15
    cost_per_stay = total_cost - discount

elif room_type == 'president apartment' and nights > 15:
    total_cost = nights * 35
    discount = total_cost * 0.20
    cost_per_stay = total_cost - discount

if grade == 'positive':
    final_cost = cost_per_stay * 0.25 + cost_per_stay

else:
    final_cost = cost_per_stay - cost_per_stay * 0.1

print(f'{final_cost:.2f}')