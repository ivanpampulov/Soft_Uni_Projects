name_actor = input()
init_grade = float(input())
referi_quantity = int(input())

for a in range(referi_quantity):

    name_referi = input()
    referi_grade = float(input())

    init_grade += len(name_referi) * referi_grade / 2

    if init_grade > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {init_grade:.1f}!")
        break

if init_grade <= 1250.5:
    print(f"Sorry, {name_actor} you need {(1250.5 - init_grade):.1f} more!")