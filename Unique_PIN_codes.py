#Read user input

PIN_1 = int(input())
PIN_2 = int(input())
PIN_3 = int(input())
flag = False

#Logic
for pin1 in range(1, PIN_1):
    for pin2 in range(2, PIN_2):
        for pin3 in range(1, PIN_3):
            if pin1 % 2 == 0 and pin3 % 2 == 0:
                if (PIN_2 % pin2) == 0:
                    flag = True
                    #if flag True not prime
                    continue
                continue
            else:
                print(f'{pin1} {pin2} {pin3}')
