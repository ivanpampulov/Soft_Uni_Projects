#Read user input

username = input()
password = input()

while True:
    user_password = input()
    if password == user_password:
        break

print(f'Welcome {username}!')