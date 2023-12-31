#Input information

budget = float(input())
videocards = int(input())
processors = int(input())
ram = int(input())

price_video = 250 * videocards
price_procc = 0.35 * price_video * processors
price_ram = 0.10 * price_video * ram
total = price_ram + price_procc + price_video

#Logic
if videocards > processors:
    final_total = total * 0.85

if budget - final_total > 0:
    print(f'You have {budget - final_total:.2f} leva left!')

else:
    print(f'Not enough money! You need {abs(budget - final_total):.2f} leva more!')