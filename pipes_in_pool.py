#Input information

v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

#Logic
water_in = (p1 + p2) * h

if v - water_in >=0:
    full_percentage = (water_in / v) * 100
    pipe1_perc = ((p1 * h) /water_in) * 100
    pipe2_perc = ((p2 * h) /water_in) * 100
    print(f'The pool is {full_percentage:.2f}% full. Pipe 1: {pipe1_perc:.2f}%. Pipe 2: {pipe2_perc:.2f}%.')

else:
    print(f'For {h:.2f} hours the pool overflows with {abs(v - water_in):.2f} liters.')