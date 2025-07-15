# validate user input exercise:
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("enter your username (no more than 12 characters, no spaces and no digits): ")
if len(username) > 12 or username.find(" ") != -1 or not username.isalpha():
    print("invalid username")
else:
    print(f"valid username. Welcome, {username}!")