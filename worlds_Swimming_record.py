#Input information
from math import floor

record = float(input())
distance = float(input())
speed_per_meter = float(input())

time = distance * speed_per_meter
delay = floor(distance /15)
final_time = (delay * 12.5) + time

if final_time <record:
    print(f'Yes, he succeeded! The new world record is {final_time:.2f} seconds.')

else:
    print(f'No, he failed! He was {abs(record-final_time):.2f} seconds slower.')