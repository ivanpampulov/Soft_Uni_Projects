#Input information
from math import ceil
skumriq_bgn = float(input())
caca_bgn = float(input())
palamud_kg = float(input()) * (skumriq_bgn + skumriq_bgn *0.6)
safrid_kg = float(input()) * (caca_bgn + caca_bgn *0.8)
midi_kg = int(input()) * 7.50

total_price = palamud_kg + safrid_kg + midi_kg

#Loigc

print(f'{total_price:.2f}')
