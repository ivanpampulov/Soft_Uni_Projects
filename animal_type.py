#Input information
animal = input()
print_output = ""

#Logic

if animal == 'dog':
    print_output = 'mammal'

elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    print_output = 'reptile'

else:
    print_output = 'unknown'

#Print output

print(print_output)